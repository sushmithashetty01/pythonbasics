#Define a function which can compute the sum of two numbers.
# Hints: Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

def add_numbers(a,b):
    sum=a+b
    return sum

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
print("The sum two numbers:", add_numbers(num1,num2))