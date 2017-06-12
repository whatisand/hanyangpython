import random
import time



def random_output(many ,min_  = 0, max_ = 0 ) :
    if max_ is 0 :
        max_ = many - 0

    randomlist = list(range(min_, max_))
    outputlist = [0]*many
    rmax = many-2
    
    for i in range(many-1) :
        rcurser = random.randint(0, rmax)
        outputlist[i] = randomlist[rcurser]
        
        randomlist[rcurser], randomlist[rmax] = randomlist[rmax], randomlist[rcurser]
        
        rmax -= 1
    outputlist[many-1] = randomlist[rmax]
    return outputlist

def bubblesort(lists) :
    length = len(lists) - 1
    results = []*length
    howmany = 0
    while length > 0 :
        n = 0
        while n < length :
            if lists[n] > lists[n+1]:
                lists[n], lists[n+1] = lists[n+1] , lists[n]
            n+=1
            howmany+=1
        length-=1
    return lists, howmany


start = time.time()
print(bubblesort(random_output(6700,0,17520)))
stop = time.time()


print(stop-start)
