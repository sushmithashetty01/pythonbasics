#Write a program that accepts a sentence and calculate the number of letters and digits.Suppose the following input is supplied to the program:hello world! 123
#Then, the output should be:LETTERS 10 DIGITS 3


sentence = input("Input a string: ")
d=l=0
for c in sentence:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters =", l)
print("Digits =", d)