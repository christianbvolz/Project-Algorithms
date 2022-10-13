def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    for letter in first_string.lower():
        if letter in second_string.lower():
            second_string = second_string.lower().replace(letter, "", 1)
        else:
            return False
    return True
