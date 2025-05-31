import pytest
from main import capitalize_words, add_numbers, is_palindrome, subtract

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python is fun") == "Python Is Fun"
    with pytest.raises(TypeError):
        capitalize_words(123)

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(2.5, 3.5) == 6.0
    with pytest.raises(TypeError):
        add_numbers("2", 3)

def test_is_palindrome():
    assert is_palindrome("madam") is True
    assert is_palindrome("race car") is True
    assert is_palindrome("hello") is False
    with pytest.raises(TypeError):
        is_palindrome(12345)


def test_subtract_positive_numbers():
    assert subtract(10, 5) == 5

def test_subtract_negative_numbers():
    assert subtract(-5, -10) == 5

def test_subtract_positive_and_negative():
    assert subtract(5, -3) == 8

def test_subtract_zero():
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5

def test_subtract_same_numbers():
    assert subtract(7, 7) == 0

def test_subtract_floats():
    assert subtract(5.5, 2.2) == pytest.approx(3.3)