def is_isogram(string):
    char_list = []
    for letter in string:
        letter = letter.lower()

        if letter in char_list and letter.isalpha():
            return False
        else:
            char_list.append(letter)

    return True
    
