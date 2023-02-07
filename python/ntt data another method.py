a=[1,0,0,0,0,0,1,0,2,1]
n=int(input())
c=0
while(n):
    rem=n%10
    c+=a[rem]
    n=n//10
print(c)
