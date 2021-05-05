#!/usr/bin/env python3

# Created by: Nika Zamani
# Created on: April 2021
# This program adds two numbers together
#    with numbers inputted from the user


def main():
    # this function adds two number

    # input
    first_number = int(input("Enter the first number to add (integer): "))
    second_number = int(input("Enter the second number to add (integer): "))


# process
    result = first_number + second_number


# output
    print('')
    print(first_number, " + ", second_number, " = ", result)
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
