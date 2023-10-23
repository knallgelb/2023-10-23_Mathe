import pytest

from basic_calculations import addieren, subtrahieren

def test_addieren_success():
    ergebnis = addieren(3, 3)
    assert ergebnis == 6


def test_subtrahieren():
    ergebnis = subtrahieren(3, 1)
    assert ergebnis == 2
