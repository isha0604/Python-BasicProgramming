#Program to find the sum of n natural numbers where n is provided by the user

#Take input from the user
n = int(input("Enter a number:"))

#Check if the number entered by the user is valid
if n < 0 :
    print("Enter a positive number ")
else :
    sum = 0
    while n > 0 :
        sum += n
        n -= 1
    print("The Sum is",sum)
