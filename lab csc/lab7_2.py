chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def relativelyPrime(a,m):
    primerelative = True
    for i in range(2, m+1):
        testa = a%i
        testm = m%i
        if testa == 0 and testm == 0:
            primerelative= False
    
    return primerelative

def affine(a, b, m, p):
    cipher = ""
    if relativelyPrime(a, m):
        for i in range(len(p)):
            pind = chars.index(p[i])
            c = ((a*pind) + b) % m
            cipher += chars[c]
        return cipher
    else:
        return ""
    
def modInverse(a, m):
    i = 1
    foundmod = False
    x = 0
    while not foundmod:
        foundmod = ((a*i)%m == 1)
        if not foundmod:
            i+=1
        if i > 500:
            return -1
    x = i
    return x


    
        