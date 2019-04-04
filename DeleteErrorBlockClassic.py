# coding=utf-8
import glob
import os


logFile = open("File summary information.log", 'w')
for nameFile in glob.glob("*.dat"):
    print("Work in progress: " + nameFile)
    fl = nameFile[nameFile.find("fl") + 3: nameFile.find("fn") - 1]
    fn = nameFile[nameFile.find("fn") + 3: nameFile.find("dist") - 1]
    iterationAmount = int(fl) * int(fn) * 2 - 1
    originalFile = open(nameFile, 'r+')
    arrayOfStrings = []
    i = 0
    erroneousBlock = 0
    rightBlock = 0
    pointer = "-1 0 0 0 0 0 0"
    print("Checking the block length - in the process")
    for currentLine in originalFile:
        currentLine = currentLine.rstrip()
        if currentLine == "":
            continue
        arrayOfStrings.append(currentLine)
        if currentLine == pointer:
            if i < iterationAmount:
                i = i + 1
                erroneousBlock = erroneousBlock + 1
                while i > 0:
                    arrayOfStrings.pop()
                    i = i - 1
            else:
                rightBlock = rightBlock + 1
            i = 0
            continue
        i = i + 1
    print("Checking the block length - completed")
    originalFile.close()
    os.remove(nameFile)
    print("Number of lines: "+str(len(arrayOfStrings)))
    summaryFile = open(nameFile, 'w')
    print("Writing to file - in the process")
    for line in arrayOfStrings:
        summaryFile.write(line + "\n")
    print("Writing to file - completed")
    summaryFile.close()
    logFile.write("Right block: " + str(rightBlock) + "\n")
    logFile.write("Erroneous blocks: " + str(erroneousBlock) + "\n")
    logFile.write("File Completed: " + nameFile + "\n")
    logFile.write("________________________________________________" + "\n")
