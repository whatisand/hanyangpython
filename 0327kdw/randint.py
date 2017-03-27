# -*- coding: utf-8 -*-
#2017.03.27. KDW hanyang python

import random

randlist = []
listTimeRand = map(lambda x : 0, range(20))

for i in range(500):
    randlist.append(random.randint(1,20))

for j in randlist:
    listTimeRand[j-1]+=1

print randlist
print listTimeRand






