# -*- coding: utf-8 -*-
"""
2017.03.27. KDW hanyang python
Guess my birth month

"""

attempts = 0
birthMonth = 1

while True:
    attempts+=1
    inputNumber = raw_input('Input your guess : ')

    if birthMonth == int(inputNumber):
        print 'You are right! you can guess right number in ' + str(attempts) + 'times'
    else:
        print 'No...'
        
