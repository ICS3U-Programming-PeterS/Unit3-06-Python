#!/usr/bin/env python3

# Created By: Peter Sobowale
# Date: October 19, 2022
# This program asks the user for a random number from
# 0 to 9 and checks if it is the same as the correct
# number that is generated
import random


def main():
    # Get the users input for a number 0 to 9
    user_num_as_a_string = input("Enter a number from 0 to 9: ")

    # Generates a random number from 0 to 9
    random_number = random.randint(0, 1)

    # try catch
    try:
        # changes the user_num into a string then prints
        user_num = int(user_num_as_a_string)
        if user_num == random_number:
            print("\nYou guessed correctly!")
        else:
            # changes the random number into a string then prints
            random_number = str(random_number)
            print("\nYou guessed wrong :(\nThe right answer was " + random_number)
    except:
        print("\n" + user_num_as_a_string + " is not an integer.")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
