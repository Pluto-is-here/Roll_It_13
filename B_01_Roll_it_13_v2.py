import random


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


def int_checker(question):
    while True:

        error = "Please enter an integer that is 13 or more"

        try:
            response = int(input(question))

            # Checks that the number is more than / equal to 13

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# find the lowest. highest and average score from a list
def get_stats(stats_list):
    # sort the lists
    stats_list.sort()

    # calculate the lowest, highest and average score and display them
    lowest_score = stats_list[0]
    highest_score = stats_list[-1]
    average_score = sum(stats_list) / len(stats_list)

    return [lowest_score, highest_score, average_score]


# generates an integer between 0 and 6 to simulate roll of a die

def roll_die():
    roll_result = random.randint(1, 6)
    return roll_result


# rolls two dice and returns total and whether we had a double roll

def two_rolls(who):
    double_score = 'no'

    # Roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # Check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points (So far)
    first_points = roll_1 + roll_2

    # Shows user the results
    print(f"{who}: {roll_1} & {roll_2} - Total: {first_points}")

    return first_points, double_score


# main routine goes here

# initialise user score and computer score

user_score = 0
comp_score = 0

num_rounds = 0

# create lists to hold user and computer scores

user_scores = []
comp_scores = []
game_history = []

# Program starts here

print()
print('🎲🎲Roll it 13🎲🎲')
print()

want_instructions = yes_no("Do you want to view instructions? ")

if want_instructions == "yes":
    instructions()

# Get a target score (must be an integer more than 13)

target_score = int_checker("Enter a target score: ")
print(target_score)

# Loop until we have a winner

while user_score < target_score and comp_score < target_score:
    # Add one to the number of rounds (for our heading)
    num_rounds += 1

    # Start of a single round

    user_pass = 'no'
    computer_pass = 'no'
    print(f"Round {num_rounds}")
    print("Press <Enter> to begin this round: ")
    input()

    # Get initial dice rolls for user
    user_first = two_rolls("User")
    user_points = user_first[0]
    double_points = user_first[1]

    # Tell the user if they are eligible for double points
    if double_points == "yes":
        print("If you win this round, you gain double points!")

    # Get initial dice rolls for computer
    computer_first = two_rolls("Computer")
    computer_points = computer_first[0]

    print(f"The computer rolled a total of {computer_points}.")

    # Loop (While both user / computer have <= 13 points) ...
    while computer_points <= 13 and user_points <= 13:

        # ask user if they want to roll again, update

        if user_points == 13:
            user_pass = "yes"

        print()
        if user_pass == 'no':
            roll_again = yes_no("Do you want to roll again? (type 'no' to pass) ")
        else:
            roll_again = 'no'

        print()
        if roll_again == "yes":
            user_move = roll_die()
            user_points += user_move

            if user_points > 13:
                print(
                    f"Whoops! you rolled a {user_move}. Your total score is now {user_points}, which is over 13 points.")
                # reset user points to zero so that when we update their score at the end
                # of the round it is correct
                user_points = 0

                break
            else:
                print(f"You rolled a {user_move}. You now have {user_points} points in total")

        else:
            user_pass = "yes"

        # if computer has 10 points or more (and is winning) it should pass
        if computer_points >= 10 and computer_points >= user_points:
            computer_pass = 'yes'

        # Don't let computer roll again if the pass condition is done
        elif computer_pass == "yes":
            pass

        else:

            # Roll die for computer and update computer points
            computer_move = roll_die()
            computer_points += computer_move

            # Check computer has not gone over...

            if computer_points > 13:
                print(f'❗❗❗ The computer rolled a {computer_move}, taking their points to {computer_points} '
                      f'This is over 13 so the computer loses! ❗❗❗')
                computer_points = 0
                break

            else:
                print(f"The computer rolled a {computer_move}. The computer now has {computer_points}.")

        print()
        # Tell the user if loss, win or tie
        if user_points > computer_points:
            result = "🙂 You are ahead! 🙂"
        elif user_points < computer_points:
            result = "😢 The computer is ahead!😢"
        else:
            result = "👀 It's currently a tie. 👀"

        print(f"User Score: {user_points} \t | \t Computer Score: {computer_points}")

        if computer_pass == "yes" and user_pass == "yes":
            break

    # Show rounds results

    print()

    if user_points < computer_points:
        print("Sorry - you lost this round and no points have been added to your total score. "
              f"The computer's score has increased by {computer_points} points")

        add_points = computer_points

    elif user_points > computer_points:
        # - double user points if they won and are eligible
        if double_points == "yes":
            user_points *= 2

        print(f" 🎉 Yay! You won the round and {user_points} point have been added to your score. 🎉")

        add_points = user_points

    else:
        print(f"👔 The result for this round is a tie. You and the computer both have {user_points} 👔")

        add_points = user_points

    round_result = f"Round {num_rounds} - User {user_points} \t Computer: {computer_points}"
    game_history.append(round_result)

    # end of a single round

    print(f"⌚ Rounds {num_rounds} ⌚")

    # If the computer wins, add its points to its score
    if user_points < computer_points:
        comp_score += add_points

    # If the user wins, add their points to their score
    elif user_points > computer_points:
        user_score += add_points

    else:
        comp_score += add_points
        user_score += add_points

    user_scores.append(user_score)
    comp_scores.append(comp_score)

    print()
    print(f"User Score: {user_points} \t | \t Computer Score: {computer_points}")
    print()

print()
if user_score > comp_score:
    print("Game over - You won! ")
elif user_score < comp_score:
    print("Game over - You lost! ")
else:
    print("Game over- It's a tie!")

print(f"Final scores: User ({user_score}) vs Computer ({comp_score}")
print()

# Display history if user wants to see it
show_history = yes_no("Do you want to see the game history?")
if show_history == "yes":
    print("\n ⌛ Game History ⌛")

    for item in game_history:
        print(item)

    print()

# calculate the lowest, highest and average score and display them
user_stats = get_stats(user_scores)
comp_stats = get_stats(comp_scores)

print(" *** Game statistics *** ")
print(f"User     - Lowest Score: {user_stats[0]}\t "
      f"Highest Score: {user_stats[1]}\t "
      f"Average Score: {user_stats[2]:.2f}")

print(f"Computer - Lowest Score: {comp_stats[0]}\t "
      f"Highest Score: {comp_stats[1]}\t "
      f"Average Score: {comp_stats[2]:.2f}")
