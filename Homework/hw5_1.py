def Infile():
    
    goodFile = False
    while goodFile == False:
        fname = input("Enter the name of the data file ")
        try:
            file = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invlid file name, try again ... ")
    return file

def getData():
    file = Infile()
    yearList = []
    shadowList = []
    diffList = []
    fibList = []
    marchList = []
    for line in file:
        line = line.strip()
        year, phil, fib, march, difference = line.split(',')
        year = int(year)
        fibList.append(fib)
        marchList.append(march)
        yearList.append(year)
        shadowList =(phil)
        diffList = (difference)
    return yearList, shadowList, diffList

def shadowTrend(year, yearList, shadowList):
    percentshadow = 0
    countshadow = 0
    for i in range (len(yearList)):
        if yearList[i] >= year and yearList[i] <= year + 4:
            print(yearList[i])
            print(shadowList[i])
            if shadowList[i] == "Full Shadow":
                countshadow += 1
    
    percentshadow = (countshadow // 5) * 100
    return percentshadow

def inputtext():
    goodValue = False
    while goodValue == False:
        try:
            year = int(input("Enter a year between 1895 and 2016: "))
            goodValue = True
        except:
            print("5 year trend could not be computed from given year ", year)
    return year

def printResults(percentshadow, year):
    print("Phil saw his shadow for ", percentshadow, "% ", "of the 5 years starting in ", year)
    
    return

def main():
    yearList, shadowList, diffList = getData()
    year = inputtext()
    percentshadow = shadowTrend(year, yearList, shadowList)
    printResults(percentshadow, year)
    
main()