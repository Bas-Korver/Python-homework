#Initialisation
def enterFile(): 
    notFound = True

    while notFound:
        fileName = input('Enter the filename here, without the suffux("<enter file suffix here>"): ')
        fileName += str('<enter file suffix here>')
        try:
            File = open(fileName, 'r')
        except FileNotFoundError:
            print('')
            print('File not found, please try again')
            print('')
        else:
            print('')
            print('File found, Congratulations!')
            print('')
            notFound = False

    fileSep = input('Which seperator does the file use? (for instance: ,  or ;) ')
    fileList = readFile(File, fileSep)