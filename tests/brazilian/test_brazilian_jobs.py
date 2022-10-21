from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    test = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    for object in test:
        assert 'title' and 'salary' and 'type' in object
        assert 'titulo' and 'salario' and 'tipo' not in object        
