import pytest
from main import CheckLeap
from main import getUserInput
import sys

def test_noraml():
    assert CheckLeap(2001) == False

def test_import(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2002")
    result = getUserInput()
    assert result == 2002

def test_noraml2():
    assert CheckLeap(2000) == True