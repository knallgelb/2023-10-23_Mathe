import pytest

from geometric_calculations import area_rectangle, area_square, area_circle

def test_area_rectangle():
    assert area_rectangle(4,2) == 8

def test_area_square():
    assert area_square(4) == 16

def test_area_circle():
    assert round(area_circle(3), 2) == 28.27
