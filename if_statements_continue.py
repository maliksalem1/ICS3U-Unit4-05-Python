#!/usr/bin/env python3
# Created by: maliksalem1
# Created on: Oct 2022
# This program adds only positive integers


def main():
    # This is the continue loop function
    loop_counter = 0
    add_int = 0

    # input,process,output
    loops_string = input("How many positive integers do you want to add?: ")
    print("")

    try:
        loops_integer = int(loops_string)
        if loops_integer > 0:
            while loop_counter < loops_integer:
                loop_counter = loop_counter + 1
                user_string = input("Enter a number to add: ")
                user_number = int(user_string)
                if user_number < 0:
                    continue
                add_int = add_int + user_number
                sum = add_int
            print("Sum of just the positive numbers is = {0}".format(sum))
        else:
            print("That is not a positive integer.")
    except ValueError:
        print("That is not a valid input, try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
