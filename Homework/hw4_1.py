#Luis Mejia 2/27/24 total time took 1hr 48min 
#thank you for grading my stuff thank you 
#for get data we want the data to be stored in a list but just the data
def getData():
    names = []
    scores = []
    x = int(input("How many golfers are in the tournament? "))
    for i in range (x):
        n = input("Enter golfer name: ")
        s = int(input("Enter golfer score: "))
        names.append(n)
        scores.append(s)
    return names, scores

# this funtion will do the computing 
def whoMadeCut(scores, n):
    listIndex = []
    for i in range(len(scores)):
        if scores[i] <= n:
            listIndex.append(i)
    return listIndex

#print results using my listIndex 
#using loop to repeat who was below cut score
# hi there hope you're having a great day for real keep your head up
def printResults(listIndex, scores, names):

    if len(listIndex) < 1:
        print("No players made the cut. ")
    else:
        print("The players who made the cut are:")
        for i in range (len(listIndex)):
            index = listIndex[i]
            print(names[index], "with score: ", scores[index])
        return

# main does main :>
#  used main to get my cut off score and also help me guide my code
# main is the easist part :3
def main():
    names, scores = getData()
    n = int(input("Enter cut score: "))
    listIndex = whoMadeCut(scores, n)
    printResults(listIndex, scores, names)
# that damn print results took years but I got it thank you :>
    