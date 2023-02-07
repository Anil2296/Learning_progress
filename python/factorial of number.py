i=int(input("enter a number::"))
if(i<0):
    print("please enter correct number")
elif(i==1):
    print(1)
elif(i==0):
    print(i)
fact=1
for k in range(1,i+1):
    fact=fact*k
print(fact)
