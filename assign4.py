#1.Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.Suppose the following input is supplied to the program:hello world and practice makes perfect and hello world again
#Then, the output should be:again and hello makes perfect practice world

sequence = input("Input sequence: ")
x = [word for word in sequence.split(' ')]

Duplicate_words = []
for i in x:
    if i not in Duplicate_words:
        Duplicate_words.append(i)
    else:
        continue
Duplicate_words.sort()
print((' ').join(Duplicate_words))