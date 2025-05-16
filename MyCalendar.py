import calendar

Year = int(input("Enter the Year : "))
# Month = int(input("Enter the Month : "))

calendar.setfirstweekday(calendar.SUNDAY)
# MyCalendar = calendar.month(Year, Month)

My_Calendar = calendar.calendar(Year)

print(My_Calendar)