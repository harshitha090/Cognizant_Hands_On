import pytest
from calculator import *

def test_add(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 30

def test_add_negative():
    assert add(-5, -3) == -8

def test_subtract(sample_numbers):
    a, b = sample_numbers
    assert subtract(a, b) == 10

def test_subtract_negative():
    assert subtract(5, 10) == -5

def test_multiply(sample_numbers):
    a, b = sample_numbers
    assert multiply(a, b) == 200

def test_multiply_zero():
    assert multiply(10, 0) == 0

def test_divide(sample_numbers):
    a, b = sample_numbers
    assert divide(a, b) == 2

def test_divide_float():
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_large_numbers():
    assert add(1000000, 1000000) == 2000000

def test_string_concat():
    assert add("Hello ", "World") == "Hello World"