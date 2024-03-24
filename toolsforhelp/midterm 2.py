def countEven(myList, start, end):
    i = 0
    even = 0
    for j in range (start, end):
        while i < len(myList):
            if myList[i] % 2 == 0:
                even = even + 1
            i = i + 1
    return even 

def main():
    myList = [23,44,56,64,25,78]
    print(countEven(myList, 1, 4))
    
main()