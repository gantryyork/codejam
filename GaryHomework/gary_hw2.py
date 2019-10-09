#!/usr/bin/python3

import random

llimit = 1
ulimit = 60
quantity = 6


def main():

    winning_nums = draw_numbers()
    my_nums = select_numbers()

    print( winning_nums )
    print( my_nums )

    correct_nums = check_numbers(my_nums, winning_nums)

    print( "You got {0} numbers correct: {1}".format( len(correct_nums), correct_nums ) )


def draw_numbers():

    nums = []

    for i in range(0, quantity):
        num = random.randint(llimit, ulimit)
        nums.append(str(num))

    nums.sort()

    return nums


def select_numbers():

    nums = []

    while len(nums) < quantity:

        num = int(input("Enter number: "))

        if not valid_num(num, nums):
            print("Invalid number.  Choose again.")
            continue
        else:
            nums.append(str(num))

    nums.sort()    

    return nums


def valid_num( number, numbers):

    if str(number) in numbers:
        return False

    if llimit <= number and number >= ulimit:
        return False 
    else:
        return True 


def check_numbers(elements, correct_elements):

    match_elements = []

    for element in elements:
        if element in correct_elements:
            match_elements.append(element)

    return match_elements

if __name__ == "__main__":
    main()
