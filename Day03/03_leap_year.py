year = int(input("Enter year:"))

if year%4==0:
    if year%100==0:
        print(year,"is not leap year")
    else:
        print(year,"is leap year")
else:
    print(year,"is not leap year")
