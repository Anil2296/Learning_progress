def factorial():
    n=int(input("Enter n value"))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
factorial()

