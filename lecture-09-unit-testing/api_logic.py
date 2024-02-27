from typing import Dict

import requests


def get_current_time():
    response = requests.get("http://worldtimeapi.org/api/timezone/Asia/Kolkata")
    if response.status_code == 200:
        output: Dict = response.json()
        return output.get("datetime")
    else:
        raise Exception("Not able to fetch time")


time = get_current_time()
print(time)
