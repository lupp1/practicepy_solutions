# Divisors www.practicepython.org/exercise/2014/02/26/04-divisors.html
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 

num = int(input())
x = [i for i in range(1, num + 1) if num % i == 0]
print(x)