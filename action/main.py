def capitalize_words(sentence):
    """Capitalize the first letter of every word in a sentence."""
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    return " ".join(word.capitalize() for word in sentence.split())

def add_numbers(a, b):
    """Add two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be int or float")
    return a + b

def is_palindrome(word):
    """Check if a word is a palindrome."""
    if not isinstance(word, str):
        raise TypeError("Input must be a string")
    cleaned = word.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
