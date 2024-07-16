import pytest

@pytest.fixture(autouse=True, scope='module')
def log_setup_and_teardown():
    print("\nSetting up before test")
    yield
    print("\nTearing down after test")

def test_example_1():
    print("\nExecuting test_example_1")
    assert True

def test_example_2():
    print("\nExecuting test_example_2")
    assert True
