#!/bin/python3

from collections import deque


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

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

    HINT:
    See <https://github.com/mikeizbicki/cmc-csci046/issues/472> for a discussion about a common memory management bug that causes the generated word ladders to be too long in some cases.
    '''
    words = load_dict(dictionary_file)
    if start_word not in words or end_word not in words:
        return None
    if start_word == end_word:
        return [start_word]
    words.remove(start_word)

    stack = [start_word]
    queue = deque()
    queue.append(stack)

    while queue:
        stack = queue.popleft()
        for word in list(words):
            if _adjacent(word, stack[-1]):
                if word == end_word:
                    return stack + [word]
                copy = stack[:]
                copy.append(word)
                queue.append(copy)
                words.remove(word)

    return None

def load_dict(path='words5.dict'):
    with open(path) as f:
        return {line.strip() for line in f}

WORDS = load_dict()


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if not ladder:
        return False
    if not all(word in WORDS for word in ladder):
        return False
    return all(_adjacent(word1, word2) for word1, word2 in zip(ladder, ladder[1:]))

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    return len(word1) == len(word2) and sum(x != y for x, y in zip(word1, word2)) == 1
