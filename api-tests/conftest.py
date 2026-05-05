import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json", "Accept": "application/json"})
    yield s
    s.close()