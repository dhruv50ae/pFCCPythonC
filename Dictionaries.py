myDict = {"name": "Max", "age": 28, "city": "Boston"}

print(myDict)

myDict2 = dict(name="Mary", age=27, city="New York")

print(myDict2)

value = myDict['name']

print(value)

myDict['email'] = "max@xyz.com"

print(myDict)

myDict['email'] = "coolmax@xyz.com"

print(myDict)

del myDict["name"]

print(myDict)

myDict.pop("age")

print(myDict)

if "name" in myDict:
    print(myDict["name"])

try:
    print(myDict["name"])
except:
    print("Error")

for key in myDict.keys():
    print(key)

for value in myDict.values():
    print(value)

for key, value in myDict.items():
    print(key, value)

myDictCopy = myDict.copy()

myDict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
myDict2 = dict(name="Mary", age=27, city="New York")

myDict.update(myDict2)

print(myDict)

myDict = {3: 9, 6: 36, 9: 81}

print(myDict)

value = myDict[3]

print(value)

myTuple = (8, 7)

myDict = {myTuple: 15}

print(myDict)
