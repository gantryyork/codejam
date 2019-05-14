#!/usr/bin/python3

def main():

    n = input( 'Choose an upper limit ')
    print( 'Checking 1..{0}\n'.format(n) )

    for i in range( 1, int(n)+1 ):
        if is_prime(i):
            print( '{0} is prime'.format(i) )


def is_prime( n ):

    #print( 'checking {0}'.format(n) )

    if n == 4:
        return False

    for divisor in range(2, int(n/2 + .5) ):
        #print( 'divisor {0}'.format(divisor) )
        if n/divisor == int(n/divisor):
           return False
    return True

if __name__ == "__main__":
    main()
