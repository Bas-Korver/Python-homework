# Test case
s1 = [{1,2,3,4}, {3,4,5}]
s2 = [{1,2,3,4}, {3,4,5}, {2,6}]

#Gets elements that are in sets of a list, but not if they're in multiple sets in said list
def unique(list):
    # Variable that stores the calculation of the sets.
    total = ""
    #Adds first set to the string
    total += str(list[0])
    #adds other sets to the total string, but with a symmetric difference calculation
    # before it
    for x in range(1, len(list)):
        total+= " ^ " + str(list[x])
        print(total)

    # runs the calculation as described in the string total
    symDifference = eval(total)
 
    return(symDifference)
print("The symmetric difference between the sets from list S1 is")
print(unique(s1))
print("The symmetric difference between the sets from list S2 is")
print(unique(s2))

#keeps asking for custom input after S1 and S2 have been calculated
## DOES NOT CHECK FOR INPUT ERRORS.
while True:
    continueInput = True
    inputList = []
    print("If you want to calculate the symmetric difference for")
    print("any other sets, please input a set below and press enter to input the next set.")
    print("When you've entered all the sets, type 'end' and press enter to end input.")
    print("Please input the sets by placing a space in between elements, like so: 1 2 3. This inserts the set {1,2,3}")
   
    while continueInput == True:
        inputSet = set(input().split())
        if inputSet == set({'end'}):
            continueInput = False
        else:
            inputList.append(inputSet)
    #the resulting symmetric difference elements are strings, but this doesn't matter in practice; the aim of
    #the program is to display it to the end user, not to use the result in different code.
    print(unique(inputList))
