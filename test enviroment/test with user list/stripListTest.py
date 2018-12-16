
def enterFile(): 
    notFound = True

    while notFound:
        fileName = input('Enter the filename here, without the suffux("txt"): ')
        fileName += str('.txt')
        try:
            open(fileName)
        except FileNotFoundError:
            print('')
            print('File not found, please try again')
            print('')
        else:
            print('')
            print('File found, Congratulations!')
            print('')
            notFound = False

    return(fileName)

def fileToList(fileName, seperator):

    # creates a list in which the file is put into
    tempList = []

    with open(fileName) as file:
        for line in file:
            tempList.append(line.strip().split(seperator))
    return (tempList)

convertedList = fileToList(enterFile(), ',')
print(convertedList)