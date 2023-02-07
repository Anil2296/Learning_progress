a=int(input("Enter a number"))
b=int(input("Enter b number"))
try:
    r=a/b
    print(r)
except ZeroDivisonError:
    print("Error occured")
c=a+b
print(c)
d=a-b
print(d)
e=a*b
print(e)
    
