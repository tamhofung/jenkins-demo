import pytest
from main import CheckLeap
from main import getUserInput
import sys

@pytest.mark.parametrize("arg", [2001, 2003, 1998])
def test_noraml(arg):
    assert CheckLeap(arg) == False

@pytest.mark.parametrize("arg", [2000, 2020, 0])
def test_leap(arg):
    assert CheckLeap(arg) == True

def test_import(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2002")
    result = getUserInput()
    assert result == 2002

