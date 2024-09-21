from flask import Flask, render_template, request, redirect
from extractors.wwr import extract_jobs_for_remoteok, extract_jobs_for_weworkremotely

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    remoteok = extract_jobs_for_remoteok(keyword)
    weworkremotely = extract_jobs_for_weworkremotely(keyword)
    jobs = remoteok + weworkremotely
    length = len(jobs)

    return render_template("search.html",
                           keyword=keyword,
                           jobs=jobs,
                           length=length)


app.run("0.0.0.0", debug=True)
