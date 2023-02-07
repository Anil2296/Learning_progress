numbers={2,3,4,5}
def square(number):
    return number*number
iterator=map(square,numbers)
square_numbers=set(iterator)
print(square_numbers)
