"""
2017.05.01. KDW

"""

def mult(dan, to = 9) :
    for i in range(1, to+1):
        print( "%d X %d = %d"%(dan, i , dan* i))
       

def main() :
    print("Please enter a number for mult table")
    number = int(raw_input())

    mult(number, to = 19)

if __name__ == "__main__" :
    main()
