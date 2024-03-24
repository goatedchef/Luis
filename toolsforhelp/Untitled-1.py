def isprime(num):
    primenum = 0
    if num % 2 == 0:
        primenum = 0
    else:
        primenum = 1
    return primenum

def allprime(numList):
    allprimeList = []
    prime = 0
    for i in range (len(numList)):
        prime = isprime(numList[i])
        if prime == 1:
            allprimeList.append(numList[i])
        
