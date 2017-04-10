# -*- coding: utf-8 -*-

import random



randomNumber = 11
#randomNumber = random.randint(1,20)

#print 'Well, '+ myName + ',I am thinking of a number between 1 and 20'


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
        break
    
    elif inputnumber > randomNumber:
        print 'High, '
        
    elif inputnumber < randomNumber:
        print 'Low, '

if randomNumber == inputnumber :
    print 'Good! You guessed my number in '+ str(wrongTimes)

else :
    print 'Nope'
