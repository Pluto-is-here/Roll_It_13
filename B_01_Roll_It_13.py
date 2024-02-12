# checks users enter yes(y) or no(n)

def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes/no

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


# Displays instructions to user
def instructions():
    print(''' 
    
    *** Instructions ***
    
    To begin, decide on a score goal (eg: The first one to get to a score of 50 wins).
    
    For each round, you will win points by rolling dice.
    The winner of the round is the one who gets 13 (or slightly less)
    
    If you win the round, then your score will increase by the number of points that you earned.
    If your first roll of two dices is a double (eg: both dice show a three), the your score will be DOUBLE 
    the number of points
    
    If you lose the round, then you don't get any points
    
    If you and the computer tie (eg: you both get a score of 11,
    then you will have 11 points added to your score.
    
    ''')

# checks that the users enter and integer that is more than 13


def int_checker():
    while True:

        error = "Please enter an integer that is 13 or more"

        try:
            response = int(input("Enter an integer "))

            # Checks that the number is more than / equal to 13

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine

print()
print('🎲🎲Roll it 13🎲🎲')
print()

want_instructions = yes_no("Do you want to view instructions? ")

if want_instructions == "yes":
    instructions()

print()

target_score = int_checker()
