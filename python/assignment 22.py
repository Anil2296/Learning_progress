import math
l=2
m=3
b=3
for a in range(1,5):
    while(b<7):
     c=l**a*m**b

    b+=1  
     g=0
    while(c%2==0):
      g+=1
      print(c)
      c=c*m/l
k=math.log(c,3)
print(k)
print(g)
 
  
