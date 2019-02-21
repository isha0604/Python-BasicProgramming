a=5
b=6
c=7
a=float(input("Enter first side:"))
s=(a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area is %0.2f"%area)