import math
import sys

def findPrime(number):
    print('Finding if', number, 'is prime.')

    sieve = sieveOfEratosthenes(number)

    for x in sieve:
        if (number % x == 0):
            print(number, 'is divisible by', x)
            sys.exit()

    print('Could not find a divisor,', number, 'must be prime.')

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
