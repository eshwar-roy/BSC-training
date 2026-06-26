def square_numbers(n):
    for i in range(n):
        yield i*i
a=square_numbers(5)
print(next(a))
print(next(a))

numbers = (x for x in range(5))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(numbers)

def numm():
    yield 10
    yield 20
    yield 44
a=numm()
print(next(a))
print(next(a))
print(next(a))