def mysteryFunction(A,B):
    i = 0
    d = A
    r = 0
    while (d > 0):
        d = d - B
        if d < 0:
            r = B + d
            print(r)
        else:
            i = i + 1
    return i,r

def main():
    print(mysteryFunction(10,5))
    
main()