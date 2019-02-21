#Program to check if the year is a leap year

Year = int(input("Enter the year:"))
if (Year % 4) == 0:
    if(Year % 100) == 0:
        if(Year % 400) == 0:
            print("{0} is a leap year".format(Year))
        else:
            print ("{0} is not a leap year".format(Year))
    else:
        print("{0} is a leap year".format(Year))
else:
    print("{0} is not a leap year".format(Year))

