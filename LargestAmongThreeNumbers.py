#To find the largest number among three numbers

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
num3 = float(input("Enter the third number:"))
if (num1 >= num2) and (num1 >= num3) :
    print("{0} is the largest number".format(num1))
elif (num2 >= num1) and(num2 >= num3):
    print("{0} is the largest number".format(num2))
else:
    print("{0} is the largest number".format(num3))