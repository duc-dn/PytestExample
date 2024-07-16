import pytest

@pytest.fixture(autouse=True)
def setup_database():
    print("Setting up the database")
    yield
    print("Tearing down the database")

def test_example_1():
    print("Executing test_example_1")
    assert True

def test_example_2():
    print("Executing test_example_2")
    assert True
