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





# generators




