"""
20170605 KDW
lotto  by me
"""

import random, time

for m in range(1,10) :

    start = time.time()

    ball = [0]*7

    ballList = range(45)

    random.shuffle(ballList)

    for i in range(7) :
        ball[i]=ballList[i]+1

    for i in range(7) :
        if i == 6 :
            print 'and ' + str(ball[i])
        else :
            print str(ball[i]) +',',
    end = time.time()

    print end - start

