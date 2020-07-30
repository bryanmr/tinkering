import math
import sys

def findPrime(number):
    print('Finding if', number, 'is prime.')

    if number < 10000000:
        sieve = sieveOfEratosthenes(number)

        for x in sieve:
            if (number % x == 0):
                print(number, 'is divisible by', x)
                sys.exit()

        print('Could not find a divisor,', number, 'must be prime.')
    else:
        shortPrimes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        for n in shortPrimes:
            if (number % n == 0):
                print(number, 'is divisible by', n)
                sys.exit()
        print('Number could be prime,', number, 'is too large to sieve')
        print('Checked if divisible by:', shortPrimes)

def sieveOfEratosthenes(number):
    prime = set(range(2, number))

    current = 2
    while (current * current <= number):
        if current in prime:
            for i in range(current*2, number, current):
                prime.discard(i)

        current += 1

    return prime

if __name__ == '__main__':
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = int(input('Enter a number to check if it is prime: '))

    findPrime(number)
