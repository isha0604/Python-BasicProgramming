#Program to check whether the number entered by the user is an armstrong number of n digits or not

num= int(input("Enter a number:"))


#Change the num variable to string to find the length
order = len(str(num))

sum = 0

#Find the sum of cube of each digit
temp = num
while temp > 0 :
    digit = temp % 10
    sum += digit**order
    temp //= 10

#Display the result
if num == sum:
    print(num," is an armstrong number")
else :
    print(num," is not an armstrong number")
