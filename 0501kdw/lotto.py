# -*- coding: cp949 -*-
import random
import timeit

"""
뽑힌 번호의 인덱스 마이너스 1을  true 로 하고 , 렌덤을 돌렸을 때 나오면 false로 바꾼다
이후 렌덤 돌렸을 때 0이라면 이미 뽑힌거니까 다시 뽑는다.

이것의 반대는 뽑을 리스트에서 삭제하고 렌덤 범위를 1 줄이면서 가는방법
이때는 리스트의 인덱스 숫자는 렌덤으로 받고 그 안에 값을 뽑은 번호로 두는것이다
"""

startT = timeit.default_timer()

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

for i in range(7) :
    if i == 6 :
        print 'and ' + str(ball[i])
    else :
        print str(ball[i]) +', ',

endT = timeit.default_timer()

print("Time : " + str(endT-startT))
