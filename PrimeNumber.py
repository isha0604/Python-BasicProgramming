#Program to check if a number is prime or not

num = int(input("Enter the number:"))

#Prime numbers are greater than 1

if num > 1 :
#Checking for factors
    for i in range(2,num):
        if (num % i) == 0 :
            print("{0} is not a prime number".format(num))
            break
    else :
            print("{0} is a prime number". format(num))



else:
    print("{0} is not a prime number".format(num))
