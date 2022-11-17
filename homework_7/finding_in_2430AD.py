import re
from matplotlib import pyplot as plt

# exstraction all number from 2430AD
pattern_num = r"\d+\.\d+|\d+"
with open("results/numbers_2430AD.txt", "w+") as res_num:
    with open("data/2430AD", "r") as story:
        for line in story:
            num = re.findall(pattern_num, line)
            for sub_str in num:
                # print(num)
                res_num.write(sub_str + ", ")


# exstraction words contaned letter "a"
pattern_a = r"\w*a\w*"
with open("results/a_words.txt", "w+") as res_a:
    with open("data/2430AD", "r") as story:
        for line in story:
            a_word = re.findall(pattern_a, line)
            for sub_str in a_word:
                # print(sub_str)
                res_a.write(sub_str+", ")


# extraction all exclamatory sentences from the story
pattern_exc = r"[A-Z][\w\s\-]*!"
with open("results/sentences!.txt", "w+") as res_exc:
    with open("data/2430AD", "r") as story:
        for line in story:
            exc_sen = re.findall(pattern_exc, line)
            for sub_exc_sen in exc_sen:
                # print(sub_exc_sen)
                res_exc.write(sub_exc_sen + '\n')


# extraction words from the story. Example "i'll" is one word.
pattern_words = r"[a-z][a-z']+|a|i"
unique_words = []
length_words = []
with open("results/words.txt", "w+") as res_words:
    with open("data/2430AD", "r") as story:
        for line in story:
            line = line.lower()
            words = re.findall(pattern_words, line)
            for sub_words in words:
                if sub_words not in unique_words:
                    unique_words.append(sub_words)
                    length_words.append(len(sub_words))

# making histogram
y = length_words
plt.hist(y)
plt.show()
