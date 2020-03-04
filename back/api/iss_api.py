"""
    iss_api.py
    This file handles the ISS (International Space Station) API
"""
import requests
from datetime import datetime


# Get data from ISS API request
def getData():
    url = 'http://api.open-notify.org/iss-now.json'
    data = requests.get(url).json()
    return data


# Pull latitude and longitude from API request
def get_lat_lng():
    data = getData()

    lat = data['iss_position']['latitude']
    lng = data['iss_position']['longitude']

    return lat, lng


# Pull dateTime from API request
def get_time():
    data = getData()

    timestamp =  data['timestamp']
    dateTime = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    return dateTime


# Called from main to get latitude, longitude and dateTime and return it all
def getAllData():

    lat, lng = get_lat_lng()
    dateTime = get_time()
     
    return lat, lng, dateTime