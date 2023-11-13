import pytest

from geometric_calculations import area_square, area_rectangle,area_circle

def test_area_square_success():
    ergebnis = area_square(2)
    assert ergebnis == 4

def test_area_rectangle_success():
    ergebnis = area_rectangle(2,5)
    assert ergebnis == 10

def test_area_circle_success():
    assert round(area_circle(4), 2) == 50.27
