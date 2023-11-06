import pytest

from basic_calculations import addieren, subtrahieren, multiplizieren, dividieren

def test_addieren_success():
    ergebnis = addieren(3, 3)
    assert ergebnis == 6


def test_subtrahieren():
    ergebnis = subtrahieren(3, 1)
    assert ergebnis == 2

def test_multiplizieren_success():
    ergebnis = multiplizieren(23, 3)
    assert ergebnis == 69

def test_dividieren():
    ergebnis = dividieren(8, 4)
    assert ergebnis == 2
