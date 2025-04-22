#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Huria Tahiry: elon  <--- Put your name here
"""

""" 
This project has two parts: 

1. "Winning" functions that evaluate the bet type, the number
   rolled, and whether the bettor won

2. The "main" function that facilitates one bet by the user,
   one spin of the wheel, and a report of the win or loss.

Note that for all code, the number 37 represents a roll of 00.
"""

"""
Part 1: Winning functions

Complete each function, which should return True if the player wins
the bet, and False if they lose.  The bet_value is the number that the 
player bets on and the roll is the number where the marble landed.
A roll value of 37 represents a roulette roll of 00.

Running the tester.py code will test these functions and check the answers,
reporting the first incorrect answer it finds for each function.

Note: If your code is very complex or long for any of these functions,
try using your problem solving techniques to find a more elegant (mathy)
solution.  
"""

import random


# For a straight bet, bet_value is an integer between 0 and 37 inclusive.  
# To win, the player must bet on the exact number that gets rolled.
def win_straight(bet_value, roll):
    if bet_value == roll:
        print('you win')
        return True
    else:
        print('you lose')
        return False


# For an even/odd bet, a bet_value of 0 represents betting "even" and 
# a bet_value of 1 represents betting "odd".
# A roll of 0 or 00 (37) always loses with this type of bet.
def win_even_odd(bet_value, roll):
    if roll == 0 or roll == 37:
        print('you lost')
        return False
    elif (roll%2) != 0 and (bet_value%2) !=0:
        return True
        print('you win')
    if (roll % 2) == 0 and (bet_value) == 0:
        return True
        print('you win')
    else:
        return False
    

# For a dozen bet, bet_value is either 1, 2, or 3, representing
# a bet on the first, second, or third dozen.
# A roll of 0 or 00 (37) always loses with this type of bet.
def win_dozen(bet_value, roll):
    bet_value = input('Select a squares: (1, 2, 0r 3):')
    square_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
    square_2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    square_3 = [23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
    true_number = random.randint(0, 37)
    if roll == 1 and true_number in square_1:
        return True
    elif roll == 2 and true_number in square_2:
        return True
    elif roll == 3 and true_number in square_3:
        return True
    else:
        return False




# For a column bet, bet_value is either 1, 2, or 3, representing
# a bet on the first, second, or third column of numbers.
# A roll of 0 or 00 (37) always loses with this type of bet.
def win_column(bet_value, roll):
    column_1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    column_2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    column_3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
    true_number = random.randint(0, 37)
    if roll == 0 or 37:
        return False
    elif roll == 1 and true_number in column_1:
        return True
    elif roll == 2 and true_number in column_2:
        return True
    elif roll == 3 and true_number in column_3:
        return True
    else:
        return False
        #
        # if bet_value == 0 or 37:
        #     return False
        # elif bet_value <= 12:
        #     return 1
        # elif bet_value <= 24:
        #     return 2
        # else:
        #     return 3

""" 
Project Part 2: Play the game.

Leave the code provided, then complete the game using the 
directions in the comments.

There is no autograder for this part.
You should run this file to test your code.
"""


def main_play_game():
    money = int(input('Enter the amount of money you want to bet: '))

    bet_type = int(input('Choose your type of bet:\n'+
                       '1: Straight bet\n'+
                       '2: Even/odd bet\n'+
                       '3: Dozen bet\n'+
                       '4: Column bet\n'))

    follow_prompts = ['',
        'Enter number to bet on, and use 37 for double-zero: ',
        'Enter 0 for even or 1 for odd: ',
        'Enter 1 for first dozen, 2 for second, or 3 for third: ',
        'Enter column number: 1, 2, or 3: '
    ]

    bet_choice = int(input(follow_prompts[bet_type]))
    import random
    roll = (0 , 37)

    # 1. Generate a random number between 0 and 37 inclusive.  This represents the
    # roll of the roulette wheel.  A value of 37 represents a roll of "00".
    # Save the value in a variable.
    # Print the value of the roll.


    if roll == 37:
        print('The roll value is 00')
    else:
        print('The roll value is', roll)


        # 2. Write a series of if-statements that calls the "win" function
        # that corresponds to the bet type, determines if the player won or
        # lost, and determines the payout.  Use as many variables as you
        # need to store/track this information.


        if bet_type == 1:
            if win_straight(bet_choice, roll) == True:
                payout = money * 2
                print('You won, amount of money', payout)
        else:
            False
            payout = 0
            print('You lost.', payout)

        if bet_type == 2 and roll != 37 and roll % 2 == 0:
            if win_even_odd(bet_choice, roll) == True:
                payout = money * 2
                print('You won, amount of money', payout)
        else:
            False
            payout = 0
            print('You lost.', payout)
        if bet_type == 3 and roll != 37 and 0 and roll == (13, 14, 15, 16, 17, 18, 19, 20, 21, 22):
            if win_dozen(bet_choice, roll) == True:
                payout = money * 3
                print('You won, amount of money', payout)
        else:
            False
            payout = 0
            print('You lost.', payout)
        if bet_type == 4 and roll != 37 and 0 and roll == (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36):
            if win_column(bet_choice, roll):
                payout = money*3
            print('You won, amount of money', payout)
        else:
            False
            payout = 0
            print('You lost.', payout)




    # 3. Print whether the player won or lost, and how much
    #    (Payout amounts are in the project description)


if __name__ == "__main__":
    main_play_game()
