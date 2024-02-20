import random


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

target_score = int_checker("Enter a target score: ")
print(target_score)

while user_score < target_score and comp_score < target_score:
    # Add one to the number of rounds (for our heading)
    num_rounds += 1

    print(f"⌚ Rounds {num_rounds} ⌚")

    add_points = int(input("How many points have been won?"))
    user_score += add_points

print()
print(f"Your final score is {user_score}")
