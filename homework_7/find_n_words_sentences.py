def find_n_words_sentences(text, num):
    """
    The function for extracting sentences with a given number of words from text
    :param text:
    :param num:
    :return: res: a list of tuples, each containing individual words from the found sentences
    """
    import re

    res = []
    # pattern for find sentences from text
    pattern_1 = r"[А-Я][\w\s\,\-]+\.*"
    # pattern for find words from sentence
    pattern_2 = r"\w+"

    # find sentences from text
    sentences = re.findall(pattern_1, text)
    # find words from sentence
    for sentence in sentences:
        words = re.findall(pattern_2, sentence)
        if len(words) == num:
            words = tuple(words)
            res.append(words)
    print(res)


find_n_words_sentences("Здесь три слова. Здесь тоже три. И тут, три. И тут - три. А тут уже четыре", 3)
