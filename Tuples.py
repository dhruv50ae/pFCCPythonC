import sys
myTuple = ("Max", 28, "Boston")
item = myTuple[0]

print(item)

for i in myTuple:
    print(i)

if "Max" in myTuple:
    print("Yes")
else:
    print("No")

myTuple = ('a', 'p', 'p', 'l', 'e')

print(len(myTuple))

print(myTuple.count("p"))

print(myTuple.index("p"))

myList = list(myTuple)

print(myList)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = a[2:5]

print(b)

myTuple = ("Max", 28, "Boston")

name, age, city = myTuple

print(name)
print(age)
print(city)

myTuple = (0, 1, 2, 3, 4)

i1, *i2, i3 = myTuple

myList = [0, 1, 2, "hello", True]
myTuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(myList), "bytes")
print(sys.getsizeof(myTuple), "bytes")
