myList = ["banana", "cherry", "apple"]

print(myList)

myList2 = [5, True, "apple", "apple"]

print(myList2)

item = myList[0]

print(item)

for i in myList:
    print(i)

if "banana" in myList:
    print("yes")
else:
    print("no")

print(len(myList))

myList.append("lemon")

print(myList)

myList.insert(1, "blueberry")

print(myList)

item = myList.pop()

print(item)
print(myList)

item = myList.remove("cherry")

print(myList)

item = myList.reverse()

print(myList)

# item = myList.clear()

print(myList)

item = myList.sort()

print(myList)

newList = sorted(myList)

print(newList)
print(myList)

myList = [0]*5

print(myList)

myList2 = [1, 2, 3, 4, 5]

newList = myList + myList2

print(newList)

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = myList[1:5]

print(a)

listOrg = ["banana", "cherry", "apple"]

listCpy = listOrg.copy()

listCpy.append("lemon")

print(listCpy)
print(listOrg)

a = [1, 2, 3, 4, 5, 6]
b = [i*i for i in a]
print(a)
print(b)
