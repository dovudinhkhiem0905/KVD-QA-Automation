import os

import requests


BASE_URL = os.getenv("KVD_BASE_URL", "https://kvdinsurance.com")


def test_homepage_is_reachable():
    assert BASE_URL, "Set KVD_BASE_URL before running tests, e.g. https://your-site.com"

    response = requests.get(BASE_URL, timeout=10)

    assert response.status_code == 200
    assert "KVD Insurance" in response.text
