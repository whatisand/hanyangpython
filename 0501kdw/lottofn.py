import random


def lotto():
    
    ball = [0]*7

    ballList = [0]*45


    for i in range(45) :
        ballList[i] = (i+1)


    for i in range(7) :
        while True :
            m = random.randint(0,44)
            # print 'test ' + str(m)
            if ballList[m] !=0 :
                ball[i] = ballList[m]
                ballList[m] = 0
                break
            else :
                continue
    returnStr = ""
    for i in range(7) :
        if i == 6 :
            returnStr = returnStr + ( 'and ' + str(ball[i]))
        else :
            returnStr = returnStr + (str(ball[i]) +', ')
    return returnStr

print lotto()



    
