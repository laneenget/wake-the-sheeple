import unittest 
from unittest import TestCase
from unittest.mock import patch, call

from back.api.air_quality_api import *
from back.api.earthquake_api import *
from back.api.iss_api import *

@patch('')