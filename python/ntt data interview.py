while(1):
    n=int(input())
    count=0
    while(n>0):
       rem=n%10;
       if(rem==6 or rem==9 or rem==0):
          count+=1
       if(rem==8):
          count+=2;
       n=n//10;

    print(count)
        
