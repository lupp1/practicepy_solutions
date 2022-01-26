# Check Primality Functions www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
# Ask the user for a number and determine whether the number is prime or not.

def get_number():
    return int(input('Give me a number: '))

def check_primalty(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return 'Prime number.' if len(divisors) <= 2 and len(divisors) != 1 else 'Not a prime number.'

if __name__ == '__main__':
    x = get_number()
    print(check_primalty(x))