import os
import requests


BASE_URL = os.getenv("KVD_BASE_URL", "https://kvdinsurance.com")


def test_quote_api_rejects_malformed_json():
    response = requests.post(
        f"{BASE_URL}/api/quote",
        data="{bad json",
        headers={"Content-Type": "application/json"},
        timeout=10,
    )

    print("Status:", response.status_code)
    print("Response:", response.text)
    
    assert response.status_code == 400