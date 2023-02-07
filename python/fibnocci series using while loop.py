f=int(input("enter the limit :...."))
a=0
b=1
count=0
if(f<=0):
    print("please enter positive integer ")
elif(f==1):
    print("the fibonacci sequence upto:")
    print(a)
else:
    print("fibonacci sequence :")
    while(count<f):
     print(a)
     k=a+b
     a=b
     b=k
     count+=1
