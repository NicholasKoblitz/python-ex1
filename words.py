def print_upper_words(words, starts_with):
    """Prints out all words in a list that starts with the given set."""

    for elemnet in starts_with:
        for word in words:
            if word[0].lower() == elemnet.lower():
                print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  starts_with={"h", "y"})
