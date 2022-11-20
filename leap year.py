def leap_year(year):
    if year%400==0 and year%100==0:
        print(f"{year} is a leap year")
        return True
    elif year%4==0 and year%100!=0:
        print(f"{year} is a LEAP YEAR")
        return True
    else:
        print(f"{year} is not a LEAP YEAR")
        return False
def month_in_year(year,month):
     month_days=[30,28,31,30,31,30,31,31,30,31,30,31]

     if leap_year(year) and month==2:
      month_days = 29
      print(f"The Year {year} Has {month_days} Days In Month {month} ")
     else:
      print(f"The Year {year} Has {month_days[month-1]} Days In Month {month} ")

year=int(input("Enter the year : "))
month=int(input("Enter the month in number : "))
month_in_year(year,month)




