# Fibonacci www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of 
# numbers in the sequence to generate.

def fibonacci(n):
    f = [0, 1]
    for i in range(n - 2):
        f.append(f[-1] + f[-2])
    return f

def user_input():
    return int(input('How many fibonacci numbers to generate? '))

print(fibonacci(user_input()))
