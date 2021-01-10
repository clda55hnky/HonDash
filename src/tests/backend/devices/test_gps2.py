from time import sleep
from unittest import mock
from unittest.mock import patch

from backend.devices.gps2 import Gps


class TestGps:

    def test_valid(self):
        with mock.patch("backend.devices.gps2.gpsd.connect") as m_connect:
            m_connect.return_value = "g"
            gps = Gps()
            assert gps.status is False
