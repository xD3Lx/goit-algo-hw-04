import re
from collections import deque


def is_palindrome(input_string):
    # Normalize the string by removing whitespace characters and converting to lowercase
    normalized_string = re.sub(r"\s+", "", input_string.lower())

    characters_deque = deque(normalized_string)

    while len(characters_deque) > 1:
        # Check the characters at both ends
        if characters_deque.popleft() != characters_deque.pop():
            return False

    return True


if __name__ == '__main__':
    test_strings = [
        "Tenet",
        "abba",
        "T e n e t",
        "T\tenet",
        "Del"
    ]

    for test in test_strings:
        print(f"'{test}' is a palindrome: {is_palindrome(test)}")


