import random
list=list(range(1,11))
count=0
n=int(input("enter lucky number:"))
for i in range (1,11):
    luckynumber=random.choice(list)
    if(luckynumber==n):
          count=count+1
if(count>=2):
   print("you are lucky")
else:
  print("you are not lucky" )
        
          
