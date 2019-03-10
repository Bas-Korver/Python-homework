# part of requirement 1
# Asks for a file name and tries to find it and adds a file extention to the
# input name. If it is not found, tell and try again untill it is found
def enterFile():

    # initialisation
    notFound = True

    # while the file isn't found, keep asking for a filename
    while notFound:

        # input filename needs to be without the file extention
        fileName = input('Enter the filename here, without the suffux(".txt"): ')

        # adds custom file extention
        fileName += str('.txt')

        # assigns the opening of a file to a variable, and tries to open it
        try:
            open(fileName)

        # If file isn't found, tell the user
        except FileNotFoundError:
            print('')
            print('File not found, please try again')
            print('')

        # if file is found, tell the user and stop asking for a new filename
        else:
            print('')
            print('File found, congratulations!')
            print('')
            notFound = False
    
    return(fileName)

# requirement 1, 2, 3
# This method reads a file, puts each line into a list whilst splitting each
# line at each Seperator, also removes newline Name of the file you wish to
# convert to a list, the seperator returns list which has the file info in it
def fileToList(fileName, seperator):

    # creates a list in which the file is put into
    tempList = []

    # opens the file and defines it as a temp var called file.  The mode (r, w,
    # etc) is not added because it wil now automaticaly choose 'r'
    with open(fileName) as file:

        # iterates over each line in file until it hits a pointer exeption
        # (a.k.a blank line)
        for line in file:

            # adds line to file, removes newline and seperates by given
            # seperator
            tempList.append(line.strip().split(seperator))

    # returns list which has the file info in it
    return (tempList)

# calculates deviation
def calcDeviation(continualValues, mean):
    lenValues = len(continualValues)
    sumSquared = 0
    for i in continualValues:
        sumSquared += ((float(i.replace(",", ".")) - mean)**2)
    mathVariable = (sumSquared / (lenValues - 1))
    deviation = (mathVariable**0.5)
    return deviation

# calculates IQR
def calcIQR(discreteValues):
    lenValues = len(discreteValues)
    sortedValues = sorted(discreteValues)
    medianIndex = lenValues // 2
    if (lenValues % 2 == 0):
        quartile1 = calcMedian(discreteValues[0:medianIndex])
        quartile3 = calcMedian(discreteValues[medianIndex:])
    else:
        quartile1 = calcMedian(discreteValues[0:medianIndex])
        quartile3 = calcMedian(discreteValues[(medianIndex + 1):])
    IQR = int(quartile1) - int(quartile3)
    return (IQR)

# calculates mean
def calcMean(listOfMean):
    lenList = len(listOfMean)
    total = 0
    for i in listOfMean:
        total += float(i.replace(",", "."))
    mean = total / lenList
    return mean

# calculates median
def calcMedian(discreteValues):
    lenValues = len(discreteValues)
    sortedValues = sorted(discreteValues)
    medianIndex = lenValues // 2
    if (lenValues % 2 == 0):
        median = int(((int(sortedValues[medianIndex]) + int(sortedValues[(medianIndex + 1)])) / 2))
    else:
        median = sortedValues[medianIndex]
    return median

# calculates modus
def calcMode(listOfData):
    return max(listOfData, key=listOfData.count)

# prints results
def printResults(fileList, modes, means, deviations, medians, IQRs):
    modeCounter = 0
    meanCounter = 0
    deviationCounter = 0
    medianCounter = 0
    IQRCounter = 0
    categoricalList = [["Name", "Mode"]]
    continualList = [["Name", "Mean", "Deviation"]]
    discreteList = [["Name", "median", "IQR"]]
    for i in range(len(fileList[1])):
        tempList = []
        if fileList[1][i] == "categorical":
            tempList.append(fileList[0][i])
            tempList.append(modes[modeCounter])
            modeCounter += 1
            categoricalList.append(tempList)
        elif fileList[1][i] == "continual":
            tempList.append(fileList[0][i])
            tempList.append(means[meanCounter])
            tempList.append(deviations[deviationCounter])
            deviationCounter += 1
            meanCounter += 1
            continualList.append(tempList)
        elif fileList[1][i] == "discrete":
            tempList.append(fileList[0][i])
            tempList.append(medians[medianCounter])
            tempList.append(IQRs[IQRCounter])
            medianCounter += 1
            IQRCounter += 1
            discreteList.append(tempList)
    print("\n Categorical \n")
    for i in range(0, len(categoricalList)):
        for j in range(0, len(categoricalList[i])):
            print('{:<20}'.format(categoricalList[i][j]), end="" )
        print()
    print("\n Continual \n")
    for i in range(0, len(continualList)):
        for j in range(0, len(continualList[i])):
            print('{:<20}'.format(continualList[i][j]), end="" )
        print()
    print("\n Discrete \n")
    for i in range(0, len(discreteList)):
        for j in range(0, len(discreteList[i])):
            print('{:<20}'.format(discreteList[i][j]), end="" )
        print()


fileName = enterFile()
fileList = fileToList(fileName, ";")
defineList = []
for i in fileList[0]:
    charRightInput = False
    while (charRightInput == False):
        print("The characteristic you're defining is %s" % (i))
        print("Is this characteristic categorical or numerical?")
        charInput = input().lower()
        if charInput == "categorical":
            defineList.append("categorical")
            print("You have answered that the characteristic is categorical.")
            charRightInput = True
        elif charInput == "numerical":
            dataRightInput = False
            print("You have answered that the characteristic is numerical.")
            while (dataRightInput == False):
                print("Does this characteristic contain continual or discrete data?")
                dataInput = input().lower()
                if dataInput == "continual":
                    defineList.append("continual")
                    dataRightInput = True
                elif dataInput == "discrete":
                    defineList.append("discrete")
                    dataRightInput = True
                else:
                    print("Answer not recognised, please try again.")
            charRightInput = True
        else:
            print("Wrong answer, please try again.")

fileList.insert(1, defineList)
categoricalValues = []
continualValues = []
discreteValues = []
for j in range(len(fileList[1])):
    tempList = []
    for k in range(2, len(fileList)):
        tempList.append(fileList[k][j])
    if fileList[1][j] == "categorical":
        categoricalValues.append(tempList)
    elif fileList[1][j] == "continual":
        continualValues.append(tempList)
    elif fileList[1][j] == "discrete":
        discreteValues.append(tempList)

#if any categorical values exists, returns true
if categoricalValues:
    Modes = []
    for i in range(len(categoricalValues)):
        Modes.append(calcMode(categoricalValues[i]))

#if any continual values exists, returns true
if continualValues:
    Means = []
    for i in continualValues:
        Means.append(calcMean(i))
    Deviations = []
    for i in range(len(continualValues)):
        Deviations.append(calcDeviation(continualValues[i], Means[i]))

#if any discrete values exists, returns true
if discreteValues:
    Medians = []
    for i in discreteValues:
        Medians.append(calcMedian(i))
    IQRs = []
    for i in discreteValues:
        IQRs.append(calcIQR(i))

#prints results
printResults(fileList, Modes, Means, Deviations, Medians, IQRs)