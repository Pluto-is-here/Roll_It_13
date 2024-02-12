# checks that the users enter and integer that is more than 13

while True:

    error = "Please enter an integer"

    try:
        my_num = int(input("Enter an integer "))

        # Checks that the number is more than / equal to 13

        if my_num < 13:
            print(error)

        print("Your number is ", my_num)

    except ValueError:
        print(error)
