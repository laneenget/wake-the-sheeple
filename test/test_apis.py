import unittest 
from unittest import TestCase
from unittest.mock import patch, call

from back.api.air_quality_api import return_aq
from back.api.earthquake_api import return_quake
from back.api.iss_api import get_lat_lng


class TestAPIs(TestCase):
    
    @patch('back.api.air_quality_api.get_aq')
    def test_aq_data_parsing(self, mock_aq):
        mock_quality = "Bad"
        example_api_response = {'success': True, 'error': None, 'response': [{'id': None, 'loc': {'lat': 50.55583, 'long': 81.85833}, 'place': {'name': "ūst'-talovka", 'state': None, 'country': 'kz'}, 'periods': [{'dateTimeISO': '2020-03-03T07:00:00+06:00', 'timestamp': 1583197200, 'aqi': 59, 'category': mock_quality, 'color': 'FFFF00', 'method': 'airnow', 'dominant': 'pm2.5', 'pollutants': [{'type': 'o3', 'name': 'ozone', 'valuePPB': 33, 'valueUGM3': 68, 'aqi': 30, 'category': 'good', 'color': '00E400'}, {'type': 'pm2.5', 'name': 'particle matter (<2.5µm)', 'valuePPB': None, 'valueUGM3': 16, 'aqi': 59, 'category': 'moderate', 'color': 'FFFF00'}, {'type': 'pm10', 'name': 'particle matter (<10µm)', 'valuePPB': None, 'valueUGM3': 29, 'aqi': 27, 'category': 'good', 'color': '00E400'}, {'type': 'co', 'name': 'carbon monoxide', 'valuePPB': 137, 'valueUGM3': 157, 'aqi': 2, 'category': 'good', 'color': '00E400'}, {'type': 'no2', 'name': 'nitrogen dioxide', 'valuePPB': 7, 'valueUGM3': 14, 'aqi': 6, 'category': 'good', 'color': '00E400'}, {'type': 'so2', 'name': 'sulfur dioxide', 'valuePPB': 19, 'valueUGM3': 51, 'aqi': 26, 'category': 'good', 'color': '00E400'}]}], 'profile': {'tz': 'Asia/Almaty', 'sources': [{'name': 'CAMS'}], 'stations': None}}]}
        mock_aq.side_effect = [example_api_response]
        quality = return_aq()
        self.assertEqual(mock_quality, quality)


    @patch('back.api.earthquake_api.get_earthquake')
    def test_eq_data_parsing(self, mock_eq):
        mock_magnitude = 1.2
        example_api_response = {'success': True, 'error': None, 'response': [{'loc': {'long': -66.7465, 'lat': 17.9801}, 'report': {'id': 'pr2020063000', 'timestamp': 1583198248, 'dateTimeISO': '2020-03-02T21:17:28-04:00', 'mag': mock_magnitude, 'type': 'minor', 'depthKM': 13, 'depthMI': 8.08, 'region': '3km WSW of Tallaboa, Puerto Rico', 'location': '3km WSW of Tallaboa, Puerto Rico'}, 'place': {'name': 'tallaboa', 'state': '', 'country': 'pr'}, 'profile': {'tz': 'America/Puerto_Rico'}, 'relativeTo': {'lat': 17.9801, 'long': -66.7465, 'bearing': 180, 'bearingENG': 'S', 'distanceKM': 0, 'distanceMI': 0}}]}
        mock_eq.side_effect = [example_api_response]
        mag = return_quake()
        self.assertEqual(mock_magnitude, mag)

    @patch('back.api.iss_api.getData')
    def test_iss_data_parsing_latlon(self, mock_loc):
        mock_lat = '-10'
        mock_lon = '10'
        mock_timestamp = '1583202024'
        mock_translated_time = '2020-03-03 02:20:24'
        example_api_response = {'message': 'success', 'iss_position': {'longitude': mock_lon, 'latitude': mock_lat}, 'timestamp': mock_timestamp}
        mock_loc.side_effect = [example_api_response]
        lat, lon, = get_lat_lng()
        self.assertEqual(mock_lon, lon)
        self.assertEqual(mock_lat, lat)

    
