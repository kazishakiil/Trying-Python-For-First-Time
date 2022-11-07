import datetime
x=int(input("Input your Birthyear="))
today = datetime.date.today()
y=today.year
age=y-x
print(age)