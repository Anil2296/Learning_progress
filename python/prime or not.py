i=int(input("Enter a lower limit:"))
j=int(input("Enter a upper limit:"))
count=0
for i in range(2,j):
   for j in range(1,i):
     if (j%i)==0:
      count+=1
if count==1:   
  print(i)

