from pathlib import Path

# Find directory
def findDirectory()->Path:
    '''Returns directory'''
    pathInput = input("Enter folder directory: ")
    path = Path(pathInput)

    if path.exists() == False or not path.is_dir():
        print("Directory not found!")
        return findDirectory()
    else:
        print("Directory Found!\n")
    
    return path

# Rename files to have base name, hyphen, index
def baseHyphenIndex(p: Path):
    '''Name - 01'''
    videoNameBase = input("Enter file name base: ")

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
    videoNameBase = input("Enter file name base: ")

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
    videoNameBase = input("Enter file name base: ")

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
    videoNameBase = input("Enter file name base: ")
    
    currentVideoIndex = 1;

    for file in p.iterdir():    
        if currentVideoIndex <= 9:
            startString = "0"
        else:
            startString = ""
    
        newFileName = startString + str(currentVideoIndex) + " " + videoNameBase + file.suffix
    
        file.rename(p.joinpath(newFileName))

        currentVideoIndex += 1


# Picks the naming convention used
def chooseNamingConvention(p: Path):
    print("CHOOSE NAMING CONVENTION")
    print("(1) Name Base - 01")
    print("(2) Name Base 01")
    print("(3) 01 - Name Base")
    print("(4) 01 Name Base")

    conventionChoice = input("\nEnter convention choice: ")

    if conventionChoice == "1":
        baseHyphenIndex(p)
    elif conventionChoice == "2":
        baseIndex(p)
    elif conventionChoice == "3":
        indexHyphenBase(p)
    elif conventionChoice == "4":
        indexBase(p)
    else:
        print("INVALID INPUT\n")
        chooseNamingConvention(p)

if __name__ == '__main__':
    path = findDirectory()

    chooseNamingConvention(path)

    print("\nRenaming Complete")
    
    
