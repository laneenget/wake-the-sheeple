import unittest 
from unittest import TestCase
from unittest.mock import patch, call

from back.api.iss_api import get_lat_lng, get_time

@patch('back.api.iss_api.get_data_from_iss')
def test_iss_data_parsing_latlon(self, mock_loc):
    mock_lat = '-10'
    mock_lon = '10'
    example_api_response = {'message': 'success', 'iss_position': {'longitude': mock_lon, 'latitude': mock_lat}, 'timestamp': 1583202024}
    mock_loc.side_effect = [example_api_response]
    lat, lon, = get_lat_lng()
    self.assertEqual(mock_lon, lon)
    self.assertEqual(mock_lat, lat)

@patch('back.api.iss_api.get_data_from_iss')
def test_iss_data_parsing_date_time(self, mock_time):
    mock_timestamp = 1583202024
    mock_translated_time = '2020-03-03 02:20:24'
    example_api_response = {'message': 'success', 'iss_position': {'longitude': -10, 'latitude': 10}, 'timestamp': mock_timestamp}
    mock_time.side_effect = [example_api_response]
    dateTime = get_time()
    self.assertEqual(mock_translated_time,dateTime)