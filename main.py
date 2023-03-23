# AvgTwoHighest.py

"""
Author: Austin Miller
Class: CS 170/01
Purpose: Create a function that returns the average of the two highest numbers
"""


def AvgTwoHighest(s1, s2, s3):
    average = 0
    if s1 < s2 and s1 < s3:
        average = (s2 + s3) / 2
    elif s2 < s1 and s2 < s3:
        average = (s1 + s3) / 2
    else:
        average = (s1 + s2) / 2
    return average


def main():
    score1 = eval(input("Enter the first score between 0 and 100 inclusive: "))
    score2 = eval(input("Enter the second score between 0 and 100 inclusive: "))
    score3 = eval(input("Enter the third score between 0 and 100 inclusive: "))
    ans = AvgTwoHighest(score1, score2, score3)

    print("\nThe average of the two highest scores is", format(ans, "0.2f"))


main()
