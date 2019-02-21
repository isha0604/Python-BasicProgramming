#Program to check if a number is prime or not within a given interval

#Enter the range
lower = int(input("Enter the lower range number:"))
upper = int(input("Enter the upper range number:"))

#Prime numbers are greater than 1
print("Prime numbers between",lower,"and", upper,"are :")

for num in range(lower,upper+1) :

    if num > 1 :
#Checking for factors
        for i in range(2,num):
             if (num % i) == 0 :
                   break
        else :
             print(num)

