from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    unique_job_types = set()
    for object in data:
        if object['job_type'] != '':
            unique_job_types.add(object['job_type'])
    return unique_job_types

    """"""
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """


def filter_by_job_type(jobs, job_type):
    filter = []
    for job in jobs:
        if job['job_type'] == job_type:
            filter.append(job)
    return filter
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """


def get_unique_industries(path):
    data = read(path)
    unique_industries = set()
    for object in data:
        if object['industry'] != "":
            unique_industries.add(object['industry'])
    return unique_industries
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """


def filter_by_industry(jobs, industry):
    filter = []
    for object in jobs:
        if object['industry'] == industry:
            filter.append(object)
    return filter
    """Filters a list of jobs by industry
    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """


def get_max_salary(path):
    data = read(path)
    max_salary_arr = set()
    for object in data:
        if object['max_salary'].isnumeric():
            max_salary_arr.add(int(object['max_salary']))
    return max(max_salary_arr)
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    pass


def get_min_salary(path):
    data = read(path)
    min_salary_arr = set()
    for object in data:
        if object['min_salary'].isnumeric():
            min_salary_arr.add(int(object['min_salary']))
    return min(min_salary_arr)
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    pass


def matches_salary_range(job, salary):
    if type(salary) != int:
        raise ValueError('salary must be a int')
    elif 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError('some values are missing')
    elif type(job['min_salary']) != int or type(job['max_salary']) != int:
        raise ValueError("we only work with integers, my friend!")
    elif job['min_salary'] > job['max_salary']:
        raise ValueError("What are you doing?")
    else:
        return job['min_salary'] <= salary <= job['max_salary']
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """


def filter_by_salary_range(jobs, salary):
    filter = []
    for object in jobs:
        try:
            if matches_salary_range(object, salary):
                filter.append(object)
        except ValueError:
            print('Hey Dude, we got some wrong input')
    return filter

    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
