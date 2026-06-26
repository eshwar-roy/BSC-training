#26-10-26

''' list comprehension '''
names=["Alice", "Bob", "Charlie", "David", "Eve"]
namee=[name.lower() for name in names]
print(namee)
lenth=[len(name) for name in names]
print(lenth)
numbers=[1,2,3,4,5,6,7,8,9,10]
numm=[n for n in numbers if n%2==0]
print(numm)
ex=[x*10 if x%2==0 else x*100 for x in numbers]
print(ex)
a=[(i,j) for i in range(3) for j in range(3)]
print(a)


''' dictionary comprehension '''
x={x:x*x for x in range(5)}
print(x)
x={x:(x*x,x**3) for x in range(6)}
print(x)
x={word:len(word) for word in names}
print(x)
x={x:x**2 for x in range(10) if x%2==0} #conditional statment
print(x)
x={x:x**3 for x in range(14) if x%2!=0 if x>=6}
print(x)
x={x:x+10 if x%2==0 else x+100 for x in range(10)}
print(x)
students=["Alice", "Bob", "Charlie", "David", "Eve"]
subjects=["Math", "Science", "History"]
marks={student:{subject:0 for subject in subjects} for student in students}
print(marks)
a=[44,65,21]
results={student:{subject:marks for subject , marks in zip(subjects,a) } for student in students}
print(results)



# generators

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


