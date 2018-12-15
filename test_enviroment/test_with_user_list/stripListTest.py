
def enterFile(): 
    notFound = True

    while notFound:
        fileName = input('Enter the filename here, without the suffux("txt"): ')
        fileName += str('.txt')
        try:
            file = open(fileName, 'r')
        except FileNotFoundError:
            print('')
            print('File not found, please try again')
            print('')
        else:
            print('')
            print('File found, Congratulations!')
            print('')
            notFound = False

    return(file)

def fileToList(originalFileName, seperator):

    # creates a list in which the file is put into
    tempList = []

    with originalFileName as file:
        for line in file:
            tempList.append(line.strip("\n").split(seperator))
    return (tempList)

sep = ","
convertedList = fileToList(enterFile(), sep)
print(convertedList)