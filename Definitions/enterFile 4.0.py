# Asks for a file name and tries to find it and adds a file extention to the
# input name. If it is not found, tell and try again untill it is found
def enterFile():

    # initialisation
    notFound = True

    # while the file isn't found, keep asking for a filename
    while notFound:

        # input filename needs to be without the file extention
        fileName = input('Enter the filename here, without the suffux("<enter file suffix here>"): ')

        # adds custom file extention
        fileName += str('<enter file suffix here>')

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