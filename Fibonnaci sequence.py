
#Program to display the fibonacci sequence upto n terms

#Number of terms to be displayed
n = int(input("Enter the number of terms:"))

#First two terms
a = 0
b = 1


i = 0

#To check if the number of terms entered by the user is valid or not
if n <= 0 :
    print("Please enter a  positive number")
elif n == 1 :
    print("Fibonacci sequence upto", n,":", a)
else :
    while i < n :
        print(a, end=",")
        c = a + b

       #Update the values
        a = b
        b = c
        i+=1





