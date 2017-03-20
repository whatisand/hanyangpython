# -*- coding: cp949 -*-

#2017.03.20 KDW hanyang python
import random

print 'Hello! what is your name?'

myName = raw_input()

number = 11
randomNumber = random.randrange(1,20)

print 'Well, '+ myName + ',I am thinking of a number between 1 and 20'
#print 'Take a guess'

wrongTimes = 0


while True:
    print 'Take a guess'
    try:    
        inputnumber = int(raw_input())
    except:
        print 'Please input number'
        pass
    #TODO Type check
    #TODO Input range check
    if randomNumber == inputnumber:
        # 맞았을 때
        print 'Good'
        break
    elif inputnumber > randomNumber:
        print 'High'
        wrongTimes+=1

    elif inputnumber < randomNumber:
        print 'Low'
        wrongTimes+=1

