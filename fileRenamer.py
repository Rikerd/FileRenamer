import os

def baseHyphenIndex():
    currentVideoIndex = 1;
    
    for file in os.listdir():
        fileName, fileExtension = os.path.splitext(file)
    
        if currentVideoIndex <= 9:
            hyphenString = " - 0"
        else:
            hyphenString = " - "
    
        newFileName = videoNameBase + hyphenString + str(currentVideoIndex) + fileExtension
    
        os.rename(file, newFileName)

        currentVideoIndex += 1

def baseIndex():
    currentVideoIndex = 1;

    for file in os.listdir():
        fileName, fileExtension = os.path.splitext(file)
    
        if currentVideoIndex <= 9:
            spaceString = " 0"
        else:
            spaceString = " "
    
        newFileName = videoNameBase + spaceString + str(currentVideoIndex) + fileExtension
    
        os.rename(file, newFileName)

        currentVideoIndex += 1

def indexHyphenBase():
    currentVideoIndex = 1;

    for file in os.listdir():
        fileName, fileExtension = os.path.splitext(file)
    
        if currentVideoIndex <= 9:
            startString = "0"
        else:
            startString = ""
    
        newFileName = startString + str(currentVideoIndex) + " - " + videoNameBase + fileExtension
    
        os.rename(file, newFileName)

        currentVideoIndex += 1

def indexBase():
    currentVideoIndex = 1;

    for file in os.listdir():
        fileName, fileExtension = os.path.splitext(file)
    
        if currentVideoIndex <= 9:
            startString = "0"
        else:
            startString = ""
    
        newFileName = startString + str(currentVideoIndex) + " " + videoNameBase + fileExtension
    
        os.rename(file, newFileName)

        currentVideoIndex += 1


dirPath = input("Enter folder directory: ")

os.chdir(dirPath)

print("Directory Found!\n")

print("CHOOSE NAMING CONVENTION")
print("(1) Name Base - 01")
print("(2) Name Base 01")
print("(3) 01 - Name Base")
print("(4) 01 Name Base")

conventionChoice = input("\nEnter convention choice: ")

videoNameBase = input("Enter video name base: ")

if conventionChoice == "1":
    baseHyphenIndex()
elif conventionChoice == "2":
    baseIndex()
elif conventionChoice == "3":
    indexHyphenBase()
elif conventionChoice == "4":
    indexBase()
