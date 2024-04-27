#Name: Luis Mejia
#Assignment: hoework 6 for CSC110
#Date: 3/21/24
 
#Gets good file for our file we want to search for today
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

#GEt data here is gonna be used to gt all data and sort them into correct order
def getdata():
    file = Infile()
    yearList = []
    Names = []
    for line in file:
        line = line.strip()
        year,name = line.split(",")
        year = float(year)
        yearList.append(year)
        Names.append(name)
        return yearList, Names



def getYearLinear(yearList, year):
    positionL = 0
    compL = 0
    for i in range (len(yearList)):
        compL += 1
        if yearList[i] == year:
            compL += 1
            positionL = i
    
        return -1

    return positionL

def getYearbinary(YearList, year):
    positionB = 0
    compB = 0
    left = 0
    found = -1
    right = len(YearList) -1
    while left <= right and found == -1:
        compB += 1
        mid = (left + right) // 2
        
        if YearList[mid] == year:
            positionB = len(YearList[mid])
        elif year < YearList[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    if found == -1:
        return ""
    else: 
        return positionB
            


def printResults(positionL, positionB, year):
    print(positionB, positionL, year)

def main():
    yearList = getdata()
    year = input("Enter a year: ")
    positionL = getYearLinear(yearList, year)
    positionB = getYearbinary(yearList, year)
    printResults(positionL, positionB, year)
    
main()