import random


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


# Main routine starts here

# Initialise 'pass' variable

user_pass = 'no'
computer_pass = 'no'
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
while computer_points < 13 and user_points < 13:

    # ask user if they want to roll again, update

    print()
    if user_pass == 'no':
        roll_again = input("Do you want to roll again? (type 'no' to pass) ")
    else:
        roll_again = 'no'

    print()
    if roll_again == "yes":
        user_move = roll_die()
        user_points += user_move

        if user_points > 13:
            print(f"Whoops! you rolled a {user_move}. Your total score is now {user_points}, which is over 13 points.")
            # reset user points to zero so that when we update their score at the end
            # of the round it is correct
            user_points = 0

            break

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

        if computer_points > 13:
            print(f'❗❗❗ The computer rolled a {computer_move}, taking their points to {computer_points} '
                  f'This is over 13 so the computer loses! ❗❗❗')
            computer_points = 0
            break

        else:
            print(f"The computer rolled a {computer_move}. The computer now has {computer_points}.")

    print()
    if user_points > computer_points:
        result = "🙂 You are ahead! 🙂"
    elif user_points < computer_points:
        result = "😢 The computer is ahead!😢"
    else:
        result = "👀 It's currently a tie. 👀"

    print(f"***Round update***: {result} ")
    print(f"User Score: {user_points} \t | \t Computer Score: {computer_points}")

    if computer_pass == "yes" and user_pass == "yes":
        break

    # Show rounds results
if user_points < computer_points:
    print("Sorry - you lost this round and no points have been added to your total score. "
          f"The computer's score has increased by {computer_points} points")

elif user_points > computer_points:
    # - double user points if they won and are eligible
    if double_points == "yes":
        user_points *= 2

    print(f" 🎉 Yay! You won the round and {user_points} point have been added to your score. 🎉")

else:
    print(f"The result for this round is a tie. You and the computer both have {user_points}")
