
"""
20170605 KDW
lotto in lecture
"""



import random, time

timeline = [0]*50

for m in range(1,50) :

    start = time.time()

    ball = [0]*7
    number = 0

    while 0 in ball :
        pick = random.randint(1,45)

        if pick in ball :
            continue
        else :
            ball[number] = pick
            number+=1
        
    for i in range(7) :
        if i == 6 :
            print 'and ' + str(ball[i])
        else :
            print str(ball[i]) +',',

    end = time.time()
    timeline[m-1] = end - start
print timeline

