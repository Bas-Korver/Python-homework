# This method reads a file, puts each line into a list whilst splitting each
# line at each Seperator, also removes newline Name of the file you wish to
# convert to a list, the seperator returns list which has the file info in it
def fileToList(fileName, seperator):

    # creates a list in which the file is put into
    tempList = []

    # opens the file and defines it as a temp var called file
    with open(fileName) as file:

        # iterates over each line in file until it hits a pointer exeption
        # (a.k.a blank line)
        for line in file:

            # adds line to file, removes newline and seperates by given
            # seperator
            tempList.append(line.strip().split(seperator))

    # returns list which has the file info in it
    return (tempList)