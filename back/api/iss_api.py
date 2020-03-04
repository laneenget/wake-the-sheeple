"""
    iss_api.py
    This file handles the ISS (International Space Station) API
"""
import requests
from datetime import datetime

def get_data_from_iss():
    url = 'http://api.open-notify.org/iss-now.json'
    data = requests.get(url).json()
    return data


# Pull latitude and longitude from API request
def get_lat_lng():
    data = get_data_from_iss()

    lat = data['iss_position']['latitude']
    lon = data['iss_position']['longitude']

    return lat, lon


# Pull dateTime from API request
def get_time():
    data = get_data_from_iss()

    timestamp =  data['timestamp']
    date_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    return date_time

# Called from main to get latitude, longitude and dateTime and return it all
def get_all_data():

    lat, lon = get_lat_lng()
    date_time = get_time()
     
    return lat, lon, date_time