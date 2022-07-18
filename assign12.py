#Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included

squares = list(map(lambda x:x*x, range(1,21)))
print(squares)