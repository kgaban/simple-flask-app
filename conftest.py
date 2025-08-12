import pytest


@pytest.fixture(autouse=True)
def hello_world():
    print("TESTING CONFTEST")
