# challenge 1
import calculator as c
print("8 + 1 = ",c.sum(8,1))
print("2 - 4 = ",c.subtract(2,4))
print("6 * 6 = ",c.multiply(6,6))
print("2 / 8 = ",c.division(2,8))

# challenge 2
import datetime as dt
today=dt.datetime.now()
print("year: ",today.year)
print("Today is: ",today)
print("month: ",today.strftime("%B"))
print("year: ",today.strftime("%A"))

# challenge 3
print("The date yesterday was: ",today - dt.timedelta(days = 1))
print("The date tomorrow will be: ",today + dt.timedelta(days = 1))



