from datetime import datetime
import os
import pytz
import requests
import math
API_KEY = '0b13dd1cb3e210ac85fa8d4bc29a5f64'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=fr&appid={}')
#API_URL = ('https://api.openweathermap.org/data/3.0/onecall?{}&mode=json&exclude=hourly,daily&appid={}')
def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
        print("testwind:{}".format(data['weather']))
    except Exception as exc:
        print(exc)
        data = None
    return data