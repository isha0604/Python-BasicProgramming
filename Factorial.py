#Program to find the factorial of a number

num = int(input("Enter the number:"))
fact = 1

#Check whether number is positive,negative or zero
if num < 0 :
    print("Factorial of negative numbers do not exist")
elif num == 0 :
    print("Factorial of 0 is 1")
else :
  for i in range(1,num+1):
    fact = fact*i
print("factorial of", num ,"is" ,fact)
