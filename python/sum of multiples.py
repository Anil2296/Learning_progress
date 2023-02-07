a=int(input("enter a first number"))
b=int(input("enter second number"))
n=int(input("enter limit number"))
sum=0
list1=[]
list2=[]
for i in range(1,n+1):
    if(i%a==0):
     #sum=sum+i
     list1.append(i)
     
for i in range(1,n+1):
    if(i%b==0):
     #add=add+i
      list2.append(i)
list3=list1+list2
set1=set(list3)
print(set1)
#r=len(set)
list4=list(set1)
for k in list4:
    sum=sum+k
print(sum)    

    
    
