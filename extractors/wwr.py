from bs4 import BeautifulSoup
import requests


def extract_jobs_for_remoteok(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("tr", class_="job")
        for job in jobs:
            anchor = job.find('a')
            link = anchor['href']
            company = job.find("h3", itemprop="name")
            position = job.find("h2", itemprop="title")
            location = job.find("div", class_="location")
            if company:
                company = company.string.replace(",", " ").strip()
            if position:
                position = position.string.replace(",", " ").strip()
            if location:
                location = location.string.replace(",", " ").strip()
            if company and position and location:
                job = {
                    'company': company,
                    'position': position,
                    'location': location,
                    'link': f"https://remoteok.com{link}"
                }
                results.append(job)
    else:
        print("Can't get jobs.")
    return results


def extract_jobs_for_weworkremotely(term):
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={term}"
    request = requests.get(url)

    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        job_section = soup.find('section', class_="jobs")
        jobs_potatoes = job_section.find_all('li')
        jobs_tomatoes = jobs_potatoes[:-1]

        for job_tomato in jobs_tomatoes:
            anchors = job_tomato.find_all('a')
            anchor = anchors[-1]
            link = anchor['href']
            company = job_tomato.find('span', class_="company")
            position = job_tomato.find('span', class_="title")
            location = job_tomato.find('span', class_="region company")

            if company:
                company = company.string.replace(",", " ").strip()
            if position:
                position = position.string.replace(",", " ").strip()
            if location:
                location = location.string.replace(",", " ").strip()
            if link and company and position and location:

                job_info = {
                    'company': company,
                    'position': position,
                    'location': location,
                    'link': f"https://weworkremotely.com/{link}"
                }
                results.append(job_info)

    else:
        print("cannot take job informations.")
    return results
