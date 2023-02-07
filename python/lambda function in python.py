def fun(n):
    return lambda a : a*n
mydoubler = fun(3)
mytripler = fun(2)

print(mydoubler(11))
print(mytripler(11))
    
