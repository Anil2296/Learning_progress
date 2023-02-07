class sum:
    display=0
    def process(self,a,b):
        c=a+b
        print("The sum is",c)
s1=sum()
a=int(input("Enter a value"))
b=int(input("Enter b value"))
s1.process(a,b)
s1.display
del s1
s1.display()
