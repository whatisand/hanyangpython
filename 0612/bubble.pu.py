from timeit import timeit

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

print(bubblesort([1,4,5,2,4,5,2,2,3,4,6,7,8,9,4,445,234,0,3,45,64,3,16,34,6435,54,3,23,5,3]))

