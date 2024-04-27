#Name: Luis Mejia
#Date: 3/29/2024
#Programming Project design 

#Tv design

# def inFile():
#the user would have to input a file.txt
#this will check if file is correct
#return file

def inFile():
    goodFile = False
    while goodFile == False:
        fname = input("Enter the name of the data file ")
        try:
            file = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invlid file name, try again ... ")
    return file
#______________________________________________________________________________________________________________________

#def getData():
#this function will get all of the Data into Lists
#then it will return all lists needed for other functions
#return Title , Rating , Year , score lists

def getData():
    File = inFile()
    titleList = []
    ratingList = []
    yearList = []
    scoreList = []
    next(File)
    for line in File:
        line = line.strip()
        title, rating, year, score = line.split(",")
        titleList.append(title)
        ratingList.append(rating)
        year = int(year)
        yearList.append(year)
        score = int(score)
        scoreList.append(score)
    return titleList, ratingList, yearList, scoreList
        

#def getchoice():
#Have print statements for the user to see in order to make a choice
#return int of said choice made

def getchoice():
    choice = 0
    print("please choose the following options: ")
    print("1 -- Find all shows with a certain rating")
    print("2 -- Find the show with the highest score released in a specified range of years")
    print("3 -- Search for a show by title")
    print("4 -- Find the average score for films with a specified rating")
    print("5 -- Find all shows with a score higher than the score for a given show")
    print("6 -- Sort all lists by year and write results to a new file")
    print("7 -- Quit")
    choice = int(input("Choice ==> "))
    
    if choice == 7:
        print("Good-bye")

    return choice

#def getspecrating(Titlelist, ratinglist)
#have a linear search where a for loops i will be index for both titel and rating and checking 
##rating as it goes down the list
#return index of all rating titles with specific rating

def getspecrating(titleList, ratingList, yearList, scoreList):
    certainrating = input("Enter rating: ")
    highest_bruh = []
    if certainrating in ratingList:
        for i in range (len(ratingList)):
            if ratingList[i] == certainrating:
                highest_bruh.append(i)
    else:
        print("Invalid entry - try again")
        getspecrating(titleList, ratingList, yearList, scoreList)
    
    if (len(highest_bruh)) > 0:
        for i in range (len(highest_bruh)):
            print(titleList[highest_bruh[i]].ljust(40), ratingList[highest_bruh[i]].ljust(8), str(yearList[highest_bruh[i]]).ljust(5),str(scoreList[highest_bruh[i]]).ljust(4))
    return highest_bruh

        

#def highestscoreyears(scorelist, startyear, endyear)
# by the way the start and end will be asked in the main While loop
#I will use a loop for this because if end year is over the len of the socre list 
#it will give out a -1 for erorr
#return index for said hieghest score 
def getyear1(yearList):
    goodyear1 = False
    while goodyear1 == False:
        try:
            startyear = int(input("Year1 "))
            if startyear not in yearList:
                print("Invalid year ")
            goodyear1 = True
        except ValueError:
            print("Invlid entry ")
    return startyear
    # if startyear != int:
    #     print("Invalid Entry")
    # elif startyear not in yearList:
    #     print("Invalid year")
    # return startyear

def getyear2(yearList):
    goodyear2 = False
    while goodyear2 == False:
        try:
            endyear = int(input("Year2 "))
            if endyear not in yearList:
                print("Invalid year ")
            goodyear2 = True
        except ValueError:
            print("Invlid entry ")
    return endyear
        
def highestscoreyears(titleList, ratingList, yearList, scoreList):
    highestscore = 0
    highest_bruh = []
    
    
    print("Enter year range to search (oldest year first) ")
    startyear = getyear1(yearList)
    endyear = getyear2(yearList)
        
    for i in range (len(scoreList)):
        if startyear <= scoreList[i] or endyear >= scoreList[i]:
            highest_bruh.append(scoreList[i])
        
        
            
    for j in range (len(highest_bruh)):
        if highestscore < highest_bruh[j]:
            highestscore = highest_bruh[j]
        else:
            print(titleList[highestscore].ljust(40), ratingList[highestscore].ljust(8), str(yearList[highestscore]).ljust(5),str(scoreList[highestscore]).ljust(4))
    
    return 
        

#def searchyear(Titlelist, titleinput)
#I will get the title name before calling this function in from main
#I will use a binaray search in order to find the title in a quicker fashsion
#this function will return the index which will be used for finding the title

#def findaverage(Ratinglist, ratinginput)
#the input will be assigned in the main function
# I will use lists to my advantage inorder to deivide the average rating with all the shows in the list 
#return veragescore

#def findhieghtest(title, score, treshold)
#im gonna get the threshold before this function is calle din the main function
#I will use the treshold and the score to simultainiusly get index for the higest score and the titles
#and put them in a list
#this will print said title and score at the same time

#def sortyears(title, rating, score, year):
#mabe making the years into an integer so i can make it into
#heighest i honestly don't know or maybe i honestly don't know maybe like sort it by compare each year with title
#opens new file and input write into our new sorted lists



#def main():
#main will be where the choice number goes into then makes the specific choice algorithim 
#in order to do this make a while loop of != and if eroor in choice else would be erorr then get choice again
def main():
    titleList, ratingList, yearList, scoreList = getData()
    choice = getchoice()
    if choice == 1:
        getspecrating(titleList, ratingList, yearList, scoreList)
    elif choice == 2:
        highestscoreyears(titleList, ratingList, yearList, scoreList)
        
main()
        
