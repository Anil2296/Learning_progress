#LCM of two numbers
a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
if(a>b):
    max=a
else:
    max=b
while(a>0 and b>0):
    if(max%a==0 and max%b==0):
        print(max)
        break

    max+=1
    

