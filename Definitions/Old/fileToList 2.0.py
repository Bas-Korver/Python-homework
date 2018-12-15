# This method reads a file, puts each line into a list whilst splitting each line at each Seperator, also removes newline
# Name of the file you wish to convert to a list, the seperator
#returns list which has the file info in it
def fileToList(originalFileName, seperator):

    # creates a list in which the file is put into
    tempList = []

    #saves the pointer position (in this case it should be the first line)
    originalFileName.tell()
    # Uncomment if you want to skip the header
    # originalFileName.readline()

    # Reads the file and puts into list
    tableLine = originalFileName.readline()

    # while the selected line in the file is not empty, write that line into a list (and split it)
    while tableLine:
        tempList.append(tableLine.split(seperator))
        tableLine = originalFileName.readline()

    # Returns the pointer position to the saved position
    originalFileName.seek()

    return (tempList)
