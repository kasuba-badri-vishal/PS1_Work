
import calendar
import datetime

# def findDay(date):
#     born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
#     # print(born)
#     return (calendar.day_name[born])
    
# date = input()
# print(findDay(date))

t = input()
t = int(t)
a,b = [],[]
for i in range(0,t):
    a.append(input())
    b.append(input())
for i in range(0,t):
    diff = datetime.datetime.strptime(a[i],"%a %d %b %Y %H:%M:%S %z") - datetime.datetime.strptime(b[i],"%a %d %b %Y %H:%M:%S %z")
    diff = diff.days*86400 + diff.seconds
    if(diff<0):
        diff = diff*(-1)    
    print(diff)