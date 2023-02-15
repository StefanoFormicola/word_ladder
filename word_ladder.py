#!/bin/python
'''
from collections import deque


import string


from queue import Queue
'''


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    word_file = _get_text(dictionary_file)
    dictionary = word_file.split()
    if start_word == end_word:
        return [start_word]
    if end_word not in dictionary:
        return None
    queue = [[start_word]]
    while queue:
        cstack = queue.pop(0)
        cword = cstack[-1]
        for word in dictionary.copy():
            if _adjacent(cword, word):
                if word == end_word:
                    cstack.append(word)
                    return cstack
                new_stack = cstack.copy()
                new_stack.append(word)
                queue.append(new_stack)
                dictionary.remove(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if len(ladder) == 0:
        return False
    for i in range(len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    lc = sum(1 for i in range(len(word1)) if word1[i] != word2[i])
    return lc == 1


def _get_text(filename):
    '''
    Takes filename and splits the test returning a list of words
    '''
    with open(filename, 'r', encoding='latin1') as f:
        text = f.read()
    return text
