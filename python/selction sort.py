#n=int(input("enter the size:"))
list=[]
n=int(input("enter the n value"))
for i in range(1,n+1):
    a=int(input("enter element:"))
    list.append(a)
k=len(list)
print(k)
#print("enter the array elements::")
for i in range(0,k+1):
    for j in range(0,k-i-1):
        if(list[j]>list[j+1]):
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print("After sorting")
print(list)


