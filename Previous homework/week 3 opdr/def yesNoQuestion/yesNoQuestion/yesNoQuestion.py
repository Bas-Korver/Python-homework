# Asks a yes/no question. If no awnser given it asks again.
def yesNoQuestion(message: str):
    
    # With whil True the loop wil never end.
    while True:

        # Asks a variable yes/no question.
        answer = input(message + ' [Y/N]: ')

        # Checks if something has been enterd and if it is a y or n.
        if len(answer) > 0 and answer[0].lower() in ('y', 'n'):            
            return answer[0].lower() == 'y'

        # Prints error message if something else was enterd.
        print('Sorry, input is not recognised. Please try again.')
