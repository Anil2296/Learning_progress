import cmath
a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))
d=(b**2)-(4*a*c)
e=cmath.sqrt(d)
r1=(-b+e)/(2.0*a)
r2=(-b-e)/(2.0*a)
print(r1)
print(r2)



