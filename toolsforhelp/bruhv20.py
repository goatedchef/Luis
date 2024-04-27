def bruh(a):
    goofy = 1
    for i in range (1,26):
        if a*i % 26 == 1:
            goofy = i
            
    return i
def main():
    a = int(input("enter for a"))
    i = bruh(a)
    print(i)
main()
    