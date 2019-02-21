#Program to check a number is positive ,negative or zero using if...elif...else

print("Enter a number:")
num=float(input())
if num > 0 :
    print("The number is positive")
elif num == 0:
    print("The number is zero")
else:
    print ("The number is negative")

#Uncomment the below code for using Nested if
"""if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")"""
