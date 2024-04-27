def computesubtotl(mylist, start, n):
    end = start + n
    if end > len(mylist):
        return -1
    else:
        return sum(mylist[start:n])

def printresults(start,n,Total):
    print(start, "+ ",  n, Total)

def main():
    start = int(input("where do you want to start"))
    n = int(input("where would you like it to end"))
    mylist = [20,30,40,50,60,70]
    Total = computesubtotl(mylist, start, n)
    printresults(start, n, Total)
    
main()