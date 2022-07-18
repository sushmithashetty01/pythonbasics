#Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10]

list1=[1,2,3,4,5,6,7,8,9,10]
EvenNumbers=list(filter(lambda x: x%2==0,list1))
print(EvenNumbers)