import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from machine_monitor import check_temperature


def test_ok_temperature():
    assert check_temperature(65) == "OK"


def test_cooling_needed():
    assert check_temperature(80) == "Cooling Needed"


def test_stop_immediately():
    assert check_temperature(95) == "Stop Immediately"


def test_boundary_ok():
    assert check_temperature(70) == "OK"


def test_boundary_cooling():
    assert check_temperature(90) == "Cooling Needed"