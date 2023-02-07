a=int(input('Enter a value'))
b=int(input('Enter b value'))
c=int(input('Enter c value'))
if(a>b):
       if(a>c):
           big = a
       else:
           big = c
else:
    if(b>c):
        big = b
    else:
        big = c
print('The biggest number =',big)
