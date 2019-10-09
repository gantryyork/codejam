#!/usr/bin/python3

import pprint
pp = pprint.PrettyPrinter(indent=4)



lower_limit = 1
upper_limit = 60

def main():

    nums = []

    while len(nums) < 6:

        num = int(input("Enter number: "))

        if not valid_num( num, nums):
            print("Invalid number.  Choose again.")
            continue
        else:
            nums.append(str(num))

    nums.sort()
    print( "Lotto numbers: ", '-'.join(nums) )



def valid_num( number, numbers):

    if number in numbers:
        return False

    if lower_limit <= number and number >= upper_limit:
        return False 
    else:
        return True 


if __name__ == "__main__":
    main()
