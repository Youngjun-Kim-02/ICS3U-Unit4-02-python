#!/usr/bin/env python3

# Created by: Youngjun Kim
# Created on: May 2021
# This program multiply integers using a while loop


def main():
    # this function multiply integers using a while loop

    # this is to keep track of hw many times you go through the loop
    loop_counter = 1
    factorial = 1

    # input
    integer_as_string = input("Enter a positive integer: ")

    # process & output
    try:
        integer_as_number = int(integer_as_string)
        if integer_as_number > 0:

            while loop_counter <= integer_as_number:
                factorial = factorial * loop_counter
                loop_counter = loop_counter + 1
            print("{0}! = {1}".format(integer_as_string, factorial))
    except Exception:
        print("That was not valid input.")


if __name__ == "__main__":
    main()
