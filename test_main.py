import pytest
from main import CheckLeap
       

def test_normal():
    assert CheckLeap(2001) == False
def test_normal2():
    assert CheckLeap(2002) == False
def test_leap():
    assert CheckLeap(2000) == True
def test_leap2():
    assert CheckLeap(2020) == True