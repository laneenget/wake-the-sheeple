import requests
from datetime import datetime


def get_data_from_iss():
    url = 'http://api.open-notify.org/iss-now.json'
    data = requests.get(url).json()
    return data

def get_lat_lng():
    data = get_data_from_iss()

    lat = data['iss_position']['latitude']
    lon = data['iss_position']['longitude']

    return lat, lon

def get_time():
    data = get_data_from_iss()

    timestamp =  data['timestamp']
    date_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    return date_time

def getAllData():

    lat, lon = get_lat_lng()
    date_time = get_time()
     
    return lat, lon, date_time