from flask import Blueprint, Flask, render_template, request, send_file

from .insights import (filter_by_industry, filter_by_job_type,
                       filter_by_salary_range, get_max_salary, get_min_salary,
                       get_unique_industries, get_unique_job_types)
from .jobs import read
from .more_insights import (build_jobs_urls, get_int_from_args, get_job,
                            slice_jobs)

bp = Blueprint("client", __name__, template_folder="templates")


@bp.route("/.images/job.png")
def flask_image():
    return send_file("../.images/job.png", mimetype="image/png")


@bp.route("/")
def index():
    md = """
<p align="center">
    <img src="/.images/job.png" alt="Logo da Aplicação" width="800"/>
</p>
<h2 align="center">
    Boas-vindas ao Job Insights<br><br>
</h2>
        """
    return render_template("index.jinja2", md=md)


@bp.route("/job/<index>")
def job(index):
    data = read('src/jobs.csv')
    job = get_job(data, index)
    return render_template('job.jinja2', job=job)


@bp.route("/jobs")
def list_jobs():
    first_job = get_int_from_args("first_job", 0)
    amount = get_int_from_args("amount", 20)
    salary = get_int_from_args("salary", None)
    industry = request.args.get("industry", None)
    job_type = request.args.get("job_type", None)

    jobs = read(path="src/jobs.csv")
    if industry:
        jobs = filter_by_industry(jobs, industry)
    if job_type:
        jobs = filter_by_job_type(jobs, job_type)
    if salary:
        jobs = filter_by_salary_range(jobs, salary)

    jobs = slice_jobs(jobs, first_job, amount)

    build_jobs_urls(jobs)

    ctx = {
        "jobs": jobs,
        "industries": sorted(get_unique_industries("src/jobs.csv")),
        "job_types": sorted(get_unique_job_types("src/jobs.csv")),
        "previous_job_type": job_type,
        "previous_first": first_job,
        "previous_amount": amount,
        "previous_industry": industry,
        "previous_salary": salary,
        "min_salary": get_min_salary("src/jobs.csv"),
        "max_salary": get_max_salary("src/jobs.csv"),
    }

    return render_template("list_jobs.jinja2", ctx=ctx)


def init_app(app: Flask):
    app.register_blueprint(bp)
