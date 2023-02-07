a=int(input("Enter the lower limit"))
b=int(input("Enter the upper limit"))
for i in range(a,b+1):
    for j in range(2,b+1):
        if(i%j)==0:
            break

    else:
        print(i)
    
        
