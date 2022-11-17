def brick_lang(word):
    """
    Function-translator from Russian to "brick language"
    :param word:
    :return: brick_word
    """
    import re

    # creating  variables
    new_vowels = []
    letters = []
    brick_word = ""

    pattern = r"[уеэоаыяию]"
    vowels = re.findall(pattern, word)

    # making new vowels for replacement old ones.
    for i in range(0, len(vowels)):
        new_vowels += [vowels[i] + "к" + vowels[i]]

    # crutch
    new_vowels += ' '

    # joining two litst by element
    parts = re.split(pattern, word)
    for i in range(0, len(parts)):
        letters += parts[i] + new_vowels[i]

    # to for sting
    for letter in letters:
        brick_word += letter

    print(brick_word)


brick_lang("кирпич")
