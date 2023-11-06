import pytest
from basic_calculations import addieren, subtrahieren, multiplizieren

def test_addieren_success():
    ergebnis = addieren(3, 3)
    assert ergebnis == 6


def test_subtrahieren():
    ergebnis = subtrahieren(3, 1)
    assert ergebnis == 2

def test_multiplizieren_success():
    ergebnis = multiplizieren(3, 1)
    assert ergebnis == 3