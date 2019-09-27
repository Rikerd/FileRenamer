from pathlib import Path
import os

# Find directory
def findDirectory()->Path:
    '''Returns directory'''
    pathInput = input("Enter folder directory: ")
    path = Path(pathInput)

    if path.exists() == False or not path.is_dir():
        print("Directory not found!")
        findDirectory()
        
    print("Directory Found!\n")
    
    return path

# Rename files to have base name, hyphen, index
def baseHyphenIndex(p: Path):
    '''Name - 01'''
    currentVideoIndex = 1;
    
    for file in p.iterdir():
        if currentVideoIndex <= 9:
            hyphenString = " - 0"
        else:
            hyphenString = " - "
    
        newFileName = videoNameBase + hyphenString + str(currentVideoIndex) + file.suffix
    
        file.rename(p.joinpath(newFileName))

        currentVideoIndex += 1
        
# Rename files to have base name, index
def baseIndex(p: Path):
    '''Name 01'''
    currentVideoIndex = 1;

    for file in p.iterdir():
        if currentVideoIndex <= 9:
            spaceString = " 0"
        else:
            spaceString = " "
    
        newFileName = videoNameBase + spaceString + str(currentVideoIndex) + file.suffix
    
        file.rename(p.joinpath(newFileName))

        currentVideoIndex += 1

# Rename files to have index, hyphen, base name
def indexHyphenBase(p: Path):
    '''01 - Name'''
    currentVideoIndex = 1;

    for file in p.iterdir():    
        if currentVideoIndex <= 9:
            startString = "0"
        else:
            startString = ""
    
        newFileName = startString + str(currentVideoIndex) + " - " + videoNameBase + file.suffix
    
        file.rename(p.joinpath(newFileName))

        currentVideoIndex += 1

# Rename files to have index, base name
def indexBase(p: Path):
    '''01 Name'''
    currentVideoIndex = 1;

    for file in p.iterdir():    
        if currentVideoIndex <= 9:
            startString = "0"
        else:
            startString = ""
    
        newFileName = startString + str(currentVideoIndex) + " " + videoNameBase + file.suffix
    
        file.rename(p.joinpath(newFileName))

        currentVideoIndex += 1


if __name__ == '__main__':
    path = findDirectory()
    
    print("CHOOSE NAMING CONVENTION")
    print("(1) Name Base - 01")
    print("(2) Name Base 01")
    print("(3) 01 - Name Base")
    print("(4) 01 Name Base")

    conventionChoice = input("\nEnter convention choice: ")

    videoNameBase = input("Enter file name base: ")

    if conventionChoice == "1":
        baseHyphenIndex(path)
    elif conventionChoice == "2":
        baseIndex(path)
    elif conventionChoice == "3":
        indexHyphenBase(path)
    elif conventionChoice == "4":
        indexBase(path)
