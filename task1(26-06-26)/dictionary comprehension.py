''' dictionary comprehension '''
names=["Alice", "Bob", "Charlie", "David", "Eve"]
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
