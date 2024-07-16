#### Example about autouse=True in Fixture of Pytest
```
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
```

```
(venv) ➜  PytestAdvanced pytest -s -v
==================================================================== test session starts ====================================================================
platform linux -- Python 3.10.12, pytest-8.2.2, pluggy-1.5.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/ducdn/Desktop/PytestAdvanced
collected 2 items                                                                                                                                           

test_1.py::test_example_1 Setting up the database
Executing test_example_1
PASSEDTearing down the database

test_1.py::test_example_2 Setting up the database
Executing test_example_2
PASSEDTearing down the database


===================================================================== 2 passed in 0.00s =====================================================================
```
- You can see that `setup_database` is automatically applied before and after test function. This is help us avoid loop code and make sure env for testing is settup consitenly.
---
```
Nếu truyền đối số như ví dụ của tôi thì cần phải truyền fixture như một đối số của function test. Right? 
Và lúc này dùng autouse=True không còn ý nghĩa lắm. Right?
```
- Đúng vậy, nếu bạn truyền fixture như một đối số của hàm test, việc sử dụng autouse=True sẽ không còn nhiều ý nghĩa. 
- Khi bạn truyền fixture như một đối số, bạn đã rõ ràng về việc fixture nào sẽ được áp dụng cho hàm test đó. 
- Sức mạnh của autouse=True là tự động áp dụng fixture mà không cần truyền đối số
- Giúp đơn giản hóa mã trong những trường hợp cần thiết lập một môi trường chung cho tất cả các hàm test.
