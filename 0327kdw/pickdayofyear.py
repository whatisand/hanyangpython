# -*- coding: utf-8 -*-
"""
2017.03.27. KDW hanyang python
Pick a day of the year

"""

import random

#print '2017-'

month = random.randint(1,12)

#print str(month) + '-'

if month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
    day = random.randint(1,31)
    
elif month == (4 or 6 or 9 or 11):
    day = random.randint(1,30)

elif month == 2:
    day = random.randint(1,28)

print '2017-'+str(month)+'-'+str(day)
