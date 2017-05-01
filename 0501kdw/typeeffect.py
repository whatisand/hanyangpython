import random
import time

def fn(x, y):
    return x + 3*y


def typingEff(printStr):
    for a in printStr:
        write(a)
        time.sleep(0.03)

#typingEff("t  est")



print(fn(5, 7))
