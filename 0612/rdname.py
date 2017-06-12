import random

def random_output(many ,min_  = 0, max_ = 0 ) :
    if max_ is 0 :
        max_ = many - 0

    randomlist = list(range(max_-min_))
    outputlist = [0]*many
    rmax = many-1
    
    for i in range(many) :
        rcurser = random.randint(0, rmax)
        outputlist[i] = randomlist[rcurser]
        
        randomlist[rcurser], randomlist[many-1] = randomlist[many-1], randomlist[rcurser]

        rmax-=1

    print(outputlist)

if __name__ == "main" :

    
