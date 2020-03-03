import requests
from datetime import datetime


def getData():
    url = 'http://api.open-notify.org/iss-now.json'
    data = requests.get(url).json()
    return data

def get_lat_lng():
    data = getData()

    lat = data['iss_position']['latitude']
    lng = data['iss_position']['longitude']

    return lat, lng

def get_time():
    data = getData()

    timestamp =  data['timestamp']
    dateTime = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    return dateTime

def getAllData():

    lat, lng = get_lat_lng()
    dateTime = get_time()
     
    return lat, lng, dateTime