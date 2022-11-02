#importing datetime
from datetime import datetime

date_format = "%d/%m/%Y"
#calculate and return difference between dates or zero if end date before first
def numOfDays(date1, date2):
    if(date2>date1):
        return (date2-date1).days
    else:
        print('end date must be after first date')
        day='0'
        return day
# check if format is correct 1st date    
def checkDay(date):
    flag=False
    while True:
        try:
           
            date1=datetime.strptime(date, date_format)
            flag=True
            return date1
            break
        except ValueError:
            print('the format should be dd/m/yyyy')
            date=input("give first date:")
# check if format is correct end date            
def checkDay2(date):
    flag=False
    while True:
        try:
            
            date2=datetime.strptime(date, date_format)
            flag=True
            return date2
        except ValueError:
            print('the format should be dd/m/yyyy')
            date=input("give end date:")    
f_date=""
while True:
    f_date=input("give first date:")
    date1=checkDay(f_date)
    e_date=input("give end date:")
    date2=checkDay2(e_date)
    print(numOfDays(date1,date2 ), "days")
    end=input('press any key to continue or e for exit:')
    if end=='e':
            break
    else:
        continue
    
