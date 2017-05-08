# -*- coding: utf-8 -*-
"""
2017.03.27. KDW hanyang python
Pick a day of the year
And change 2017.05.08.
"""

import random

def pickday(year) : 

    month = random.randint(1,12)
    
    if month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        day = random.randint(1,31)
        
    elif month == (4 or 6 or 9 or 11):
        day = random.randint(1,30)

    elif month == 2:
        day = random.randint(1,28)

    ret =  str(year)+'-'+str(month)+'-'+str(day)
    return ret

if __name__ == "__main__" :
    
    y = int(raw_input("input year =>> "))
    print(pickday(y))
