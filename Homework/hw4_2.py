#Luis Mejia 2/27/24
#make the function and the prameters
def subString(input_string, length):
    substrings = []
    # here i'll put a for loop 
    # when making this for loop I had to try out this way since it worked like vs code 
    #did't have a problem and I looked up if this did work and yes the len with
    # - length I looked because I kind knew it was possible so I wanted to use it
    for i in range(len(input_string) - length + 1):
        #here I did use a new way that was not taught in class with postion i
        #in range with i + length I knew this before though and I juust wanted to finsih this hw
        substrings.append(input_string[i:i+length])
    return substrings

def allsubstring(string):
    allsubs = []
    for i in range (1, len(string) + 1):
        allsubs.extend(allsubstring(string)[:i])
    return allsubs

