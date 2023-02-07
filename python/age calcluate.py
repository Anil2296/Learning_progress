import datetime
object= datetime.datetime.now()
print(object)
yearofbirth=int(input("enter your year of birth"))
currentyear=object.today().year
age=currentyear-yearofbirth
today=datetime.date.today()
print("your age is :",age)
print(today)                  
