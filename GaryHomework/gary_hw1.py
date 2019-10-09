#!/usr/bin/python3
import random

def main():
    start = 1
    end = 100
    turn = 1
    last = 8
    number = random.randint(1,100)


    while turn <= last:
        result = get_valid_num(start, end)
        if result > number:
            print("Your guess is too high, you have ",last-turn, "tries left!")
        elif result < number:
            print("Your guess is too low, you have ",last-turn, "tries left!")
        else:
            print("You guessed it!")
            break
        turn = turn + 1
    
    print("You are out of guesses, sorry")


def get_valid_num(start, end):

    while True:
        try:
            result = int(input("Please type a number from 1-100 : "))
        except (ValueError, TypeError):
            print("Number is not an Integer! Try again")
        else:
            if result >= start and result <= end:
                return result
                    #print("{0} is a number between 1 and 100, congrats!".format(result))
            else:
                print("Value is out of range")


    return num


if __name__ == '__main__':
    main()
