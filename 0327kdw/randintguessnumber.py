# -*- coding: utf-8 -*-
#2017.03.20. KDW hanyang python
#And 2017.03.27. And 2017.04.03.
import random

print 'Hello! what is your name?'

myName = raw_input()

#number = 11
randomNumber = random.randint(1,20)

print 'Well, '+ myName + ',I am thinking of a number between 1 and 20'
#print 'Take a guess'

wrongTimes = 0


while wrongTimes < 6:
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

    wrongTimes+=1
    
    #TODO Input range check
    if randomNumber == inputnumber:
        print 'Good'
        print 'you guess my number in '+ str(wrongTimes) +' times!' 
        break
    
    elif inputnumber > randomNumber:
        print 'High, '
        print 'Your try and wrong : '+ str(wrongTimes) +' times!'
        
    elif inputnumber < randomNumber:
        print 'Low, '
        print 'Your try and wrong : '+ str(wrongTimes) +' times!'
        
