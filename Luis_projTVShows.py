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

def getspecrating(ratingList, certainrating):
    listofcertainrating = []
    for i in range (len(ratingList)):
        if ratingList[i] == certainrating:
            listofcertainrating.append(i)
        elif len(listofcertainrating) == 0:
            return -1
    return listofcertainrating

        

#def highestscoreyears(scorelist, startyear, endyear)
# by the way the start and end will be asked in the main While loop
#I will use a loop for this because if end year is over the len of the socre list 
#it will give out a -1 for erorr
#return index for said hieghest score 
def getyear1(yearList, startyear):
    if startyear != int:
        print("Invalid Entry")
    else:
        
    
def highestscoreyears(scorelist, highestscore):
    #highestscore = startyear
    #if startyear and endyear in yearlist:
     #   for i in range (len(yearlist, startyear, endyear)):
      #      if scorelist[highestscore] < scorelist[i]:
       #         highestscore = i
        #        print(i)
    return highestscore
        

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

#def printResults():
#print oen of all strings used for each question answered 

def printResults(titleList, ratingList, yearList, scoreList, choice, certainrating, startyear, endyear):
    if choice == 1:
        listofcertainrating = getspecrating(ratingList, certainrating)
        for i in range (len(listofcertainrating)):
            print(titleList[listofcertainrating[i]].ljust(40), ratingList[listofcertainrating[i]].ljust(8), str(yearList[listofcertainrating[i]]).ljust(5),str(scoreList[listofcertainrating[i]]).ljust(4))
    elif choice == 2:
        highestscore = highestscoreyears(scoreList, yearList, startyear, endyear)
        print(titleList[highestscore].ljust(40), ratingList[highestscore].ljust(8), str(yearList[highestscore]).ljust(5),str(scoreList[highestscore]).ljust(4))

            
    
    
    return

#def main():
#main will be where the choice number goes into then makes the specific choice algorithim 
#in order to do this make a while loop of != and if eroor in choice else would be erorr then get choice again
def main():
    titleList, ratingList, yearList, scoreList = getData()
    choice = getchoice()
    if choice == 1:
        certainrating = input("Enter rating ")
        printResults(titleList, ratingList, yearList, scoreList, choice, certainrating)
    elif choice == 2:
        startyear = int(input("Enter year1: "))
        endyear = int(input("Enter year2: "))
        printResults(titleList, ratingList, yearList, scoreList, choice, startyear, endyear)
        
main()
        
