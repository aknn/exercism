import re
from collections import Counter

def count_words(sentence):
    """
    Counts the occurrences of each word in a given sentence from subtitles.

    This function is case-insensitive and handles contractions, numbers, and
    various forms of punctuation. It correctly ignores apostrophes used as
    quotation marks.
    """
    # Normalize unicode apostrophes to standard
    sentence = sentence.lower().replace("’", "'")

    # Use regex to find all sequences of letters, numbers, and apostrophes.
    # This correctly separates words based on punctuation and whitespace,
    # while keeping contractions like "that's" together.
    potential_words = re.findall(r"[a-z0-9']+", sentence)

    # Remove any leading or trailing apostrophes from each item.
    cleaned_words = [word.strip("'") for word in potential_words]

    # Count the frequency of each unique, cleaned word.
    return Counter(cleaned_words)
