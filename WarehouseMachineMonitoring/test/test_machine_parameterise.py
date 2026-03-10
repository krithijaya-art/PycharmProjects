import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from machine_monitor import check_temperature

@pytest.mark.parametrize("temperature, expected", [
    (65, "OK"),
    (80, "Cooling Needed"),
    (95, "Stop Immediately"),
    (70, "OK"),
    (90, "Cooling Needed")
])

def test_check_temperature(temperature, expected):
    assert check_temperature(temperature) == expected