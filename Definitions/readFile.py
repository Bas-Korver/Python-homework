def readFile(file, fileSep):

    #Initialisation
    fileList = []
    emptyStr = ''

    #Skip header in file
    file.readline()

    #Read the file and enter it in a list
    eof = False
    while not eof:
        fileLine = file.readline()
        if fileLine == emptyStr:
            eof = True
        else:
            fileList.append(fileLine.strip().split(fileSep))

    return (fileList)