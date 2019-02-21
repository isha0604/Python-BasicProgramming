#Program to check whether the number entered by the user is an armstrong number or not

num= int(input("Enter a numbeer:"))
sum = 0

#Find the sum of cube of each digit
temp = num
while temp > 0 :
    digit = temp % 10
    sum += digit**3
    temp //= 10

#Display the result
if sum == num :
    print(num," is an armstrong number")
else :
    print(num," is not an armstrong number")
