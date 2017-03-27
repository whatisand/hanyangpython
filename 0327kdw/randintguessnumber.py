# -*- coding: utf-8 -*-
#2017.03.20. KDW hanyang python
#And 2017.03.27. 
import random

print 'Hello! what is your name?'

myName = raw_input()

#number = 11
randomNumber = random.randint(1,20)

print 'Well, '+ myName + ',I am thinking of a number between 1 and 20'
#print 'Take a guess'

wrongTimes = 0


while True:
    print 'Take a guess'
    """
    inputnumber = int(raw_input())
    """
    # Check input error
    try:    
        inputnumber = int(raw_input())
    except:
        print 'Please input number'
        continue
    
    
    #TODO Input range check
    if randomNumber == inputnumber:
        print 'Good'
        print 'you can guess my number in '+ str(wrongTimes) +' times!' 
        break
    
    elif inputnumber > randomNumber:
        print 'High'
        wrongTimes+=1
        
    elif inputnumber < randomNumber:
        print 'Low'
        wrongTimes+=1
