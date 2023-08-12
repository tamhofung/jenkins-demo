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
'''
def test_normal2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2002")
    result = CheckLeap()
    assert result == False
def test_leap(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2000")
    result = CheckLeap()
    assert result == True
def test_leap2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2020")
    result = CheckLeap()
    assert result == True
'''