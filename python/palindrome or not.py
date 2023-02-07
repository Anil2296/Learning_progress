
i=int(input("enter a  number"))
sum=0
t=i
while(i>0):
    r=i%10
    sum=(sum*10)+r
    i=i//10
if sum==t:
    print("palindrome number")
else:
   print("not a palindrome number") 
    
