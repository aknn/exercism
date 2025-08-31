def is_valid(isbn):
    """
    Check if a string is a valid ISBN-10.
    """
    # Remove hyphens and check length
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False

    # Validate characters and calculate sum
    total = 0
    for i, char in enumerate(isbn):
        if i < 9:
            if not char.isdigit():
                return False
            total += int(char) * (10 - i)
        else:  # Check digit
            if char == "X":
                total += 10
            elif not char.isdigit():
                return False
            else:
                total += int(char)

    # Check if the sum is divisible by 11
    return total % 11 == 0