# -*- coding: cp949 -*-
import random
import timeit

"""
���� ��ȣ�� �ε��� ���̳ʽ� 1��  true �� �ϰ� , ������ ������ �� ������ false�� �ٲ۴�
���� ���� ������ �� 0�̶�� �̹� �����Ŵϱ� �ٽ� �̴´�.

�̰��� �ݴ�� ���� ����Ʈ���� �����ϰ� ���� ������ 1 ���̸鼭 ���¹��
�̶��� ����Ʈ�� �ε��� ���ڴ� �������� �ް� �� �ȿ� ���� ���� ��ȣ�� �δ°��̴�
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
