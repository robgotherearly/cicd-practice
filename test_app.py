# test_app.py
from app import add, subtract

def test_add():
    assert add(2, 3) == 5  # fixed!

def test_subtract():
    assert subtract(5, 3) == 2