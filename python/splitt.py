k=[123,456]
for i in k:
    sum=0
    while(i>0):
        r=i%10
        sum=sum+r
        i=i//10
    print(sum)
    
