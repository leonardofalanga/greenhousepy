from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock

from mock import GPIO
from mock.seesaw import Seesaw
from src.greenhouse import Greenhouse, GreenhouseError


class TestGreenhouse(TestCase):

    @patch.object(Seesaw, 'moisture_read')
    def test_measure_soil_moisture_valid_range(self, mock_moisture_read):
        mock_moisture_read.return_value = 300
        gn= Greenhouse()
        self.assertEqual(gn.measure_soil_moisture, 300)
