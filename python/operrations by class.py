class operation:
    a=20
    b=30
    def addition(self):
        operation.c=operation.a+operation.b
        
    def sub(self):
        operation.d=operation.a-operation.b
    def mul(self):
        operation.e=operation.a*operation.b
    def div(self):
        operation.f=operation.a/operation.b
    def output(self):
        print("Sum is",operation.c)
        print("Diff is",operation.d)
        print("Mul is",operation.e)
        print("Div is",operation.f)
s=operation()
#a=int(input("Enter a value"))
#b=int(input("Enter b value"))
s.addition()
s.sub()
s.mul()
s.div()
s.output()
    
