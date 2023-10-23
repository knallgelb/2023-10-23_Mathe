import pytest

from basic_calculations import addieren

def test_addieren_success():
    ergebnis = addieren(3, 3)
    assert ergebnis == 6
