
trial = 0

print 'Hello! What is your favorite player?'

name = raw_input()

backNumber = 26

while trial < 7
    print 'Take a guess'

    # Checking input type error
    try:
        inputnumber = int(raw_input())
    except:
        print 'Please input number'
        continue

    trial+=1
    
    if backNumber == inputnumber:
        print 'Good'
        print 'you guess my number in '+ str(trial) +' times!' 
        break
    
    elif inputnumber > backNumber:
        print 'High, '
        print 'Your try and wrong : '+ str(trial) +' times!'
        
    elif inputnumber < backNumber:
        print 'Low, '
        print 'Your try and wrong : '+ str(trial) +' times!'
        
