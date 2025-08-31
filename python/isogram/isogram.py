def is_isogram(string):
    """
    This function checks if a string is an isogram

    Args:
        string(str): The string to check

    Returns:
        bool: True if the string is an isogram, False otherwise
    """
    seen_letters = []

    for char in string.lower():
        if char.isalpha() and char in seen_letters:
            return False
        seen_letters.append(char)

    return True
