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

def Menu():
    loop = True
    while loop:
        print('__________________________________________________________')
        print('│  Maak een keuze uit de volgende opties:                │')
        print('│  1.                                                    │')
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')