import pytest
from main import capitalize_words, add_numbers, is_palindrome

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
