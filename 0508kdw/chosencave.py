import random
import time

def checkCave() :
    print('you approach the cave...')
    time.sleep(1)
    print('asdf...sadfsadf...')
    time.sleep(1)
    print('asdf...sadfsadf...')
    time.sleep(1)

    
    user_chosen = int(raw_input("please your choice where you to go(1, 2)"))

    if user_chosen == random.randint(1,2) :
        print('k')
    else :
        print('l')


if __name__ == '__main__' :
    
