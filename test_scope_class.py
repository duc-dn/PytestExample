import pytest

@pytest.fixture(scope="class", autouse=True)
def log_setup_and_teardown():
    print("\nSetting up before any tests in class")
    yield
    print("\nTearing down after all tests in class")

class TestExample:
    def test_example_1(self):
        print("Executing test_example_1")
        assert True

    def test_example_2(self):
        print("Executing test_example_2")
        assert True


# collected 2 items                                                                                                                                           

# test_scope_class.py::TestExample::test_example_1 
# Setting up before any tests in class
# Executing test_example_1
# PASSED
# test_scope_class.py::TestExample::test_example_2 Executing test_example_2
# PASSED
# Tearing down after all tests in class
