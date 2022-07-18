#Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included)

def Tup():
    x = []
    for i in range(1, 21):
        x.append(i*i)
    print(tuple(x))

Tup()

