"""
File: anagram.py
Name: Jack Chen
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

d_lst = []  # List that contains
anagram_lst = []  # The list that includes the separated alphabets of the input.
summary_lst = []  # The full list of the anagrams that the input word has.


def main():
    """
    According to the input, this algorithm is able to search all the combinations of the anagrams.
    """
    global anagram_lst, summary_lst
    while True:
        print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
        insert = str(input('Find anagrams for: '))
        if insert == EXIT:
            print('Search Complete')
            break
        else:
            start = time.time()
            ####################
            print('Searching...')
            find_anagrams(insert)
            print(f'{len(summary_lst)} anagrams: {summary_lst}')
            ####################
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')
        anagram_lst = []  # Clear the results from the last search.
        summary_lst = []  # Clear the results from the last search.


def read_dictionary():
    '''
    To import 'ONLY' THE the dictionaries' content WITH THE SAME LENGTH AS INPUT into d_lst [list].
    '''
    with open(FILE, 'r') as f:
        for line in f:
            words = line.split()
            words_str = ''.join(words)
            # d_lst will only include vocabs that has the same length as input.
            if len(str(words_str)) == len(anagram_lst):
                d_lst.append(str(words_str))
        return d_lst


def find_anagrams(s):
    """
    :param s: the input letter.
    :return: the anagrams of the input letter.
    """
    for i in range(len(s)):
        anagram_lst.append(s[i])
    d_lst = read_dictionary()
    find_anagrams_helper(anagram_lst, [], len(anagram_lst), d_lst, [])


def find_anagrams_helper(anagram_lst, current_lst, length, d_lst, support_lst):
    '''
    :param anagram_lst: The list that includes the separated alphabets of the input.
    :param current_lst: The list that includes the current alphabets.
    :param length: The length of the input letter.
    :param d_lst: The list that includes letters that have the same length as the letter.
    :param support_lst: The list that includes all the current anagrams of the letter. (Prevent anagram duplication)
    '''
    if len(current_lst) == length:  # if current list's length has the same length as anagram list
        current_str = ''.join(current_lst)  # turn current list into a str letter
        if current_str in d_lst and current_str not in summary_lst:
            summary_lst.append(current_str)
            print('Found: ' + current_str)
            print('Searching...')
    else:
        for i in range(length):
            if i not in support_lst:  # In case letter duplication, anagram list matches with support list
                current_lst.append(anagram_lst[i])
                support_lst.append(i)
                if has_prefix(''.join(current_lst), d_lst):
                    find_anagrams_helper(anagram_lst, current_lst, length, d_lst, support_lst)
                    current_lst.pop()
                    support_lst.pop()
                else:
                    current_lst.pop()
                    support_lst.pop()


def has_prefix(sub_s, d_lst):
    """
    :param sub_s: input sub str.
    :return: Boolen, return True when sub_s matches d_lst, return False when the sub_s has no where found in d_lst.
    """
    for alpha in d_lst:
        if alpha.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
