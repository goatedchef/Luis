def getspeeds():
    speedList = []
    fname = input("Enter file name: ")
    infile = open(fname, 'r')
    line = infile.readline()
    line = line.strip()
    while line != "":
        speed = float(line)
        speedList.append(speed)
        line = infile.readline()
        line = line.strip()
        
    return speedList 

def speeds():
    speedList = []
    fname = input("Enter file name: ")
    infile = open(fname, 'r')
    for line in infile:
        line = line.strip()
        speed = float(line)
        speedList.append(speed)
    return

def getdata():
    speedList = []
    dateList = []
    fname = input("Enter file name: ")
    infile = open(fname, 'r')
    for line in infile:
        line = line.strip()
        speed, date = line.split(',')
        speed = float(line)
        speedList.append(speed)
        dateList.append(date)
    return speedList, dateList
