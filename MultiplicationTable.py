#Program to find multiplication table of a number from 1 to 10

num = int(input("Enter the number:"))

for i in range(1,11):
    Multi = num * i
    print(num ,"*",i,"=",Multi  )
