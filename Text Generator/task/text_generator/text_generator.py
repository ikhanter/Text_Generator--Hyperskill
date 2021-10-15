from nltk.tokenize import regexp_tokenize
from nltk.probability import FreqDist
import nltk
import sys
from collections import Counter
import random
import string
import re

class KeyError(Exception):

    def __str__(self):
        return 'Key Error: The requested word is not in the model'


class TypeError(Exception):

    def __str__(self):
        return 'Type Error: entered command must be an integer'


class IndexError(Exception):

    def __str__(self):
        return 'Index Error: entered index does not exist'


def detect_first_word():
    check_words = random.choice(list(trigrams_sorting.keys()))
    while not (check_words[0] in string.ascii_uppercase) or (('.' in check_words) or ('?' in check_words) or ('!' in check_words)):
        check_words = random.choice(list(trigrams_sorting.keys()))
    return check_words

def detect_words(test_words, i):
    words, weights = zip(*trigrams_sorting[test_words].most_common())
    check_word = random.choices(words, weights)[0]
    check2 = test_words.split()[-1] + ' ' + check_word
    while (i <= 5 and (word[-1] not in string.punctuation for word in trigrams_sorting[check2].keys()) and (i > 5)):
        words, weights = zip(*trigrams_sorting[test_words].most_common())
        check_word = random.choices(words, weights)[0]
        check2 = test_words.split()[-1] + ' ' + check_word
    return check_word

filename = input()
f = open(f'{filename}', 'r', encoding='utf-8')
word_list = []
for line in f:
    x = regexp_tokenize(line, "[^\s]+")
    word_list += x
# freqdist = FreqDist(word_list)
f.close()

# bigrams_list = list(nltk.bigrams(word_list))
trigrams_list = list(nltk.trigrams(word_list))

trigrams_sorting = {}
# bigrams_sorting = {}

# for head, tail in bigrams_list:
#     bigrams_sorting.setdefault(head, []).append(tail)
# for key in bigrams_sorting:
#     bigrams_sorting[key] = Counter(bigrams_sorting[key])

for head1, head2, tail in trigrams_list:
    trigrams_sorting.setdefault((head1 + ' ' + head2), []).append(tail)
for key in trigrams_sorting:
    trigrams_sorting[key] = Counter(trigrams_sorting[key])


for j in range(10):
    i = 0
    sentence = ''
    while i <= 5:
        i = 0
        sentence = ''
        go_words = detect_first_word()
        sentence += go_words + ' '
        i += 1
        while sentence[-2] not in ('.', '!', '?'):
            i += 1
            second_word = detect_words(go_words, i)
            sentence += second_word + ' '
            go_words = sentence.split()[-2] + ' ' + sentence.split()[-1]
    print(sentence)

