#!/usr/bin/env python

import random
import re

def get_words(filename, min_length = 3, max_length=9, disallowed=[' ', '-']):
    words = []
    with open(filename, 'r') as data_in:
        for line in data_in:
            word = line.strip().lower()
            if not word:
                continue
            if len(word) >= min_length and len(word) <= max_length:
                if not any([c in word for c in disallowed]):
                    words.append(word)
    return words

__dictionaries = ['adverbs','verbs','nouns']
words = [get_words(dictionary) for dictionary in __dictionaries]

def create_name(add_number=99):
    """
    Create a random, semi-realistic, name. If add_number is != 0 (default 99) a
    number in range 1-add_number is added to the end of the name.
    """
    name = [random.choice(wlist) for wlist in words]
    if add_number:
        name.append(str(random.randint(1,add_number)))
    return '-'.join(name)

def name_possibilities():
    '''Get the number of possible names'''
    return reduce(lambda pos, lst: pos*len(lst),words, 1)

def word_len():
    '''Number of words being used'''
    return reduce(lambda l, wlist: l + len(wlist), words, 0)


if __name__ == '__main__':
    print create_name(add_number=0)

    print name_possibilities()
    print word_len()
