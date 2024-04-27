# Given: A list of processes with execution times
# Find: A schedule of the processes using time slices

import queue
import random


# Function to get open data file
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Enter the name of the file containing the processes: ")
        try:
            inFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid file name - try again ... ")
    return inFile

        
        

# Function to get the time slice value and the processes from the file into the queue
# Queue will contain a string with process ID and exec time separated by a comma

def getProcs():
    infile = openFile()
    procList = []
    execList = []
    # Get the first line in the file containing the time slice value
    # Strip the \n from the line and convert to an integer
    # Loop through the file inserting processes into the queue
    for line in infile:                             
        line = line.strip()
        proc, eTime = line.split(',')
        procList = procList + [proc]
        execList = execList + [int(eTime)]
    infile.close()
    return procList, execList

# Function to print the contents of the queue

def printQueue(tslice, cpuQ):
    tslice = 0
    print("The time slice is ",tslice, "- The contents of the queue are: ")
    for i in range(cpuQ.qsize()):
        proc = cpuQ.get()
        cpuQ.put(proc)
        print(proc)


# Function to execute the processes in the queue

def scheduleProcs(tslice, cpuQ):
    while (cpuQ.empty() == 0):                  
	# Get next process from queue
        proc = cpuQ.get()                           
	# Separate the process ID and the execution time from the process info
        PID, exectime = proc.split(",")             
	# Convert exectime to an integer
        exectime = int(exectime)                    
        print("Next Process", PID,"with", exectime,"instructions to execute")
	# Initialize the timer
        timer = 0                                   
	# While proc still has time in slice and still has code to execute
        while (timer < tslice) and (exectime > 0):  
	    # Execute an instruction of process
            exectime = exectime - 1                         
	    # Count one tick of the timer
            timer = timer + 1                       
            print("Instruction:", exectime," Process:", PID," Timer:", timer)

	# If proc still has instructions to execute put it back in the queue
        if (exectime > 0):                          
	    # Create string with new exec time and process ID
            proc = PID + "," + str(exectime)        
	    # Put the process back in the queue
            cpuQ.put(proc)                          
            print("Process:", PID," back in queue ", exectime,"instructions remaining")
        else:
            print("*** Process", PID, "Complete ***")
    return


# Main function

def main():
    # Create the scheduling queue
    cpuQ = queue.Queue()

    # Get the processes from the data file
    procList, execList= getProcs()

    print(procList,execList)

    # Schedule the processes
    #scheduleProcs(tslice, cpuQ)
