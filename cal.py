import calendar;
month= int(input("Enter month in number :"))
if(month<=12 or month>1):
    year= int(input("Enter year : "))
    cal = calendar.month(year,month)
    print(cal)
    print("Month : ", month, "Year : ",year)
else:
    print("Invalid Month")
