year=int(input("Eneter a Year \n"))
if(year%100==0 & year%400==0):
    print(year, "is a leap year")
elif(year%4==0):
    print(year,"is a leap year")
else:
    print("not a leap year")