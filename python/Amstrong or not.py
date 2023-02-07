import math
n=int(input("enter a number :"))
count=0
sum=0
t=n
n1=n
while(n1!=0):
    n1=n1/10
    count+=1
while(n>0):
    rem=n%10
    sum=sum+pow(rem,count)
    n=n//10
if sum==t:
    print("Amstrong number")
else:
    print("not a Amstrong number")
    
                                                                                                                                      
    
    
