#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:26:03 2021
@author: Shannon Duvall


Modified on Thu Feb 28 16:04:30 2023
@author: Duke Hutchings
"""









"""
You should run this file, but
don't change any of the code in this file
"""

















"""
Here be dragons
"""







"""
Do not change this code
"""

import roulette


def general_tester(tests, function, row_change, function_str):
    for b in range(len(tests)):
        for d in range(len(tests[0])):
            bet = b + row_change
            your_answer = function(bet, d)
            correct = tests[b][d]
            if your_answer is None:
                reply = function_str + "(" + str(bet) + ", " + str(d) + ")" + \
                    " incorrectly returned None"
                return reply
            elif your_answer != correct:
                reply = function_str + "(" + str(bet) + ", " + str(d) + ")" + \
                    " incorrectly returned " + str(your_answer)
                return reply
    return function_str + ": ALL TESTS PASSED"


def test_straight():
    tests = [[b == d for b in range(38)] for d in range(38)]
    return general_tester(tests, roulette.win_straight, 0, "win_straight")


def test_eo():
    row0 = [False] + [False, True] * 18 + [False]
    row1 = [False] + [True, False] * 18 + [False]
    tests = [row0, row1]
    return general_tester(tests, roulette.win_even_odd, 0, "win_even_odd")


def test_dozen():
    tests = [[False] + [True] * 12 + [False] * 24 + [False],
             [False] + [False] * 12 + [True] * 12 + [False] * 12 + [False],
             [False] + [False] * 24 + [True] * 12 + [False]]
    return general_tester(tests, roulette.win_dozen, 1, "win_dozen")


def test_col():
    tests = [[False] + [True, False, False] * 12 + [False],
             [False] + [False, True, False] * 12 + [False],
             [False] + [False, False, True] * 12 + [False]]
    return general_tester(tests, roulette.win_column, 1, "win_column")


if __name__ == "__main__":
    print(test_straight())
    print(test_eo())
    print(test_dozen())
    print(test_col())    
