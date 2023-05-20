import requests
import schedule
import time
from os import environ
from datetime import datetime


BASE_URL = environ.get("BASE_URL", "https://cms.taxilastone.com")


def call_apis():
    # Make API calls here
    requests.get(f"{BASE_URL}/")
    requests.get(f"{BASE_URL}/banner-images/")
    requests.get(f"{BASE_URL}/kitchen-category/")
    requests.get(f"{BASE_URL}/inspiration-category/")
    requests.get(f"{BASE_URL}/material-category/")
    requests.get(f"{BASE_URL}/video-category/")
    requests.get(f"{BASE_URL}/media-category/")
    requests.get(f"{BASE_URL}/homepage/")
    requests.get(f"{BASE_URL}/videos/")
    requests.get(f"{BASE_URL}/media/")
    requests.get(f"{BASE_URL}/inspiration/")
    requests.get(f"{BASE_URL}/kitchen/")
    requests.get(f"{BASE_URL}/material/")
    requests.get(f"{BASE_URL}/teams/")
    requests.get(f"{BASE_URL}/static-content/")


schedule.every(2).minutes.do(call_apis)

while True:
    print(datetime.now())
    schedule.run_pending()
    time.sleep(10)
