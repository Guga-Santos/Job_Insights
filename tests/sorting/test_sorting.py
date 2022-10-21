from src.sorting import sort_by

jobs = [
    {'min_salary': 2000, 'max_salary': 3000, 'date_posted': '2018-06-05'},
    {'min_salary': 3000, 'max_salary': 4000, 'date_posted': '2020-06-05'},
    {'min_salary': 4000, 'max_salary': 5000, 'date_posted': '2015-06-05'},
    {'min_salary': 1000, 'max_salary': 2000, 'date_posted': '2019-06-05'},
]

min_order = [jobs[3], jobs[0], jobs[1], jobs[2]]
max_order = [jobs[2], jobs[1], jobs[0], jobs[3]]
date_order = [jobs[1], jobs[3], jobs[0], jobs[2]]


def test_sort_by_criteria():
    sort_by(jobs, 'min_salary')
    assert jobs == min_order

    sort_by(jobs, 'max_salary')
    assert jobs == max_order

    sort_by(jobs, 'date_posted')
    assert jobs == date_order
