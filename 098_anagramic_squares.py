#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Anagramic squares" – Project Euler Problem No. 98
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=98
import itertools


def load_words(filename):
    with open(filename) as f:
        words = f.read().replace("\"", "").split(",")
    return words


def word2digits(word, letters, mapping):
    ret = ''
    for char in word:
        index = letters.index(char)
        ret = ret + str(mapping[index])
    return int(ret)


def are_anagrams_of_each_other(w1, w2):
    if len(w1) != len(w2):
        return false
    for char in w1:
        if w1.count(char) != w2.count(char):
            return False
    return True


def get_distinct_letters(word):
    ret = list(set(list(word)))
    ret = sorted(ret)
    return ret


def find_anagrams(words):
    # expecting words of same length
    ret = []
    visited = [False] * len(words)
    for i in range(0, len(words)-1):
        tmp = [words[i]]
        if visited[i]:
            continue
        for j in range(i+1, len(words)):
            if visited[j]:
                continue
            if are_anagrams_of_each_other(words[i], words[j]):
                visited[j] == True
                tmp.append(words[j])
        visited[i] == True
        if len(tmp) > 1:
            ret.append(tmp)
    return ret


def group_words_by_length(words, maxlength):
    buckets = {}
    for word in words:
        length = len(word)
        if length > maxlength:
            continue
        if length in buckets:
            buckets[length].append(word)
        else:
            buckets[length] = [word]
    return buckets


def find_anagramic_squares_max_in_group(anagram_words):
    ret = 0
    word = anagram_words[0]
    letters = get_distinct_letters(word)
    if len(letters) > 10:
        return 0
    for digits_to_map_to in itertools.combinations(list(range(10)), len(word)):  # select k digits from '0123456789'
        for mapping in itertools.permutations(digits_to_map_to):  # try out all permutations of the digits to map to
            count_squares = 0
            for word in anagram_words:
                word_num = word2digits(word, letters, mapping)
                if len(str(word_num)) != len(word):
                    continue  # leading zeros

                if int(word_num**0.5)**2 == word_num:
                    count_squares = count_squares + 1
                    if count_squares > 1:
                        ret = max(ret, word_num)
    return ret


def find_anagram_groups(words):
    """
    Finds all anagrams and groups them into sublists
    """
    ret = []
    word_groups = group_words_by_length(words, maxlength=10)
    for word_group in word_groups.values():
        for anagram_group in find_anagrams(word_group):
            ret.append(anagram_group)
    return ret


def find_max_square_in_anagrams(words):
    ret = 0
    for anagram_group in find_anagram_groups(words):
        ret = max(ret, find_anagramic_squares_max_in_group(anagram_group))
    return ret

# Testcase
words = ['CARE', 'RACE']
testcase_solution = find_max_square_in_anagrams(words)
assert testcase_solution == 9216, "Testcase failed"

# Solve
words = load_words("098_words.txt")
solution = find_max_square_in_anagrams(words)
print "Solution:", solution
