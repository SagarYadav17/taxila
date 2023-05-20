import requests
import schedule
import time
from os import environ

BASE_URL = environ.get("BASE_URL", "https://cms.taxilastone.com")


def call_apis():
    # Make API calls here
    requests.get(f"{BASE_URL}/")
    requests.get(f"{BASE_URL}/banner-images/?from=cron")
    requests.get(f"{BASE_URL}/kitchen-category/?from=cron")
    requests.get(f"{BASE_URL}/inspiration-category/?from=cron")
    requests.get(f"{BASE_URL}/material-category/?from=cron")
    requests.get(f"{BASE_URL}/video-category/?from=cron")
    requests.get(f"{BASE_URL}/media-category/?from=cron")
    requests.get(f"{BASE_URL}/homepage/?from=cron")
    requests.get(f"{BASE_URL}/videos/?from=cron")
    requests.get(f"{BASE_URL}/media/?from=cron")
    requests.get(f"{BASE_URL}/inspiration/?from=cron")
    requests.get(f"{BASE_URL}/kitchen/?from=cron")
    requests.get(f"{BASE_URL}/material/?from=cron")
    requests.get(f"{BASE_URL}/teams/?from=cron")
    requests.get(f"{BASE_URL}/static-content/?from=cron")


schedule.every(2).minutes.do(call_apis)

while True:
    schedule.run_pending()
    time.sleep(1)
