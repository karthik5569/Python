#Task 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial(num))

#Task 2
import math

num = float(input("Enter a number: "))
print("Square root:", math.sqrt(num))
print("Natural log:", math.log(num))
print("Sine:", math.sin(num))
