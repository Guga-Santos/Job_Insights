from src.counter import count_ocurrences


def test_counter():
    test = count_ocurrences('src/jobs.csv', 'jobs')
    assert test == 306
