import tool_working as tool_working
from Student import Student
from SmartStudent import SmartStudent

# STRING AND NUMBER ---------------------------------

temp = "World Hello \ World"
print(temp)
print(temp.upper())
print(temp.islower())
print(len(temp))
print(temp.index("o"))  # first "o" can find
print(temp.index("World"))
print(temp.replace("World", "Fcking World"))  # replace all

num = 5

pow3Num = num**3  # same pow(num,3)

print(str(num))

print(pow3Num)

# name = float(input("enter your code:"))  # input with type = float
# print("endcode : " + name)  # output

# LIST ( ARRAY ) ----------------------------------------------

friends = [4, 2, 3, 1]
pow2friends = [i*i for i in friends]
print(pow2friends)
friends0 = [0] * 5
friends2 = ["A", "B", "C", "D"]

print(friends[1:])
print(friends[1::2])  # get elements from 1 with step = 2
print(friends[2::-2])  # get elements from 2 with step = 2 but left dim
friends3 = sorted(friends)
friends.sort()
print(friends)
print(friends3)

friends[2] = 9
print(friends[1:3])
friends.insert(1, "GG")
print(friends)
friends.append("GG")
print(friends)
friends.extend(friends2)   # same friends + friends2

print(type(friends[0]))
print(type(friends[-1]))

print(friends.index("GG"))  # first GG can find
print(friends.count("GG"))  # how many value "GG"

friends.remove("GG")  # first GG can find
print(friends)

friends.pop()  # last element
print(friends)

# friends.sort()  # can't sort both string and int
# print(friends)

friends3 = friends
# or friends.copy() or friends[1:]
print(friends3)

friends.reverse()
print(friends)

friends.clear()  # first GG can find
print(friends)

if "D" in friends2:
    print("DDDDDD")

# TUPLE ------------------------------------------------------------------

tupleTemp = (4, 5)
print(tupleTemp[0])  # TUPLE = CONST list , use for set up data

tupleFriends2 = tuple(friends2)  # change list to tuple

mytuple = 'Max', 22, 'IT'
name, age, major = mytuple

print(name + ' - ' + str(age) + ' - ' + major)

mytuple2 = (0, 1, 2, 3, 4)

x1, *x2, x3 = mytuple2

print(x2)  # all element [1,2,3] with type = list

# FUNCTION ------------------------------------------------------------------


def printString():
    print("GGEZ")


def returnNum(num):
    return num


printString()
print(returnNum(3))

# if else -------------------------------

if (temp.isupper() or False) and True:
    print(temp)
elif temp.isupper() and not (False):
    print(temp.lower())
else:
    print(temp.upper())

# DICTIONARY ( object ) ------------------------------------------------------------------

myDictionary = {
    "book": "sach",
    "paper": "top-conference",
    10: "ten"
}

print(myDictionary["paper"])
print(myDictionary[10])

print(myDictionary.keys())
print(myDictionary.values())

for key, value in myDictionary.items():
    print(key, value)

del myDictionary["book"]  # delete item
# same myDictionary.pop("book")
# myDictionary.popitem() is delete last item

# u also can update a dictionary like my_dict.update(my_dict_2)

# output = ( (8,7) : 15 ) ( a dictionary with key = a tuple )
my_dict_2 = {mytuple: 15}

print(myDictionary.get("papers", "paper"))

# LOOP ------------------------------------------------------------------

while num <= 10:
    print(num)
    num += 1

for friend in friends3:
    print(friend, end=' ')

for letter in temp:
    print(letter, end=' ')

for index in range(11):
    print(index, end=' ')

for index in range(-2, 10):
    print(index, end=' ')

for index in range(len(friends2)):
    print(friends2[index], end=' ')

# 2D LIST ------------------------------------------------------------------

list2dim = [
    [0, 1, 2],
    [0, 1, 2, 3],
    [0, 1, 2],
    [0]
]

# try:
#   ....
# except:
#   .....
# except ZeroDivisionError:
# .......
# except ValueError as err:
# print(err)

# = try catch in JAVA

# FILES ------------------------------------------------------------------

# READING FILES ( read txt and specially that CSV files for datas)

test_read_file = open("beginner/test.txt", "r")
# "a" for add new information "r+" for both read and write files

print(test_read_file.readable())

# give a list content in string type so u can use for loop
print(test_read_file.readlines())

print(test_read_file.readline())  # done reading and take point to next line
print(test_read_file.read())
# read also have this absolute so point gave to end of file so 2nd readline get " "
print(test_read_file.readline())


test_read_file.close()

# WRITING FILES

test_read_file = open("beginner/test.txt", "w")

test_read_file.write("Toby - Dev")  # clear old file and write new

test_read_file.close()

test_read_file = open("beginner/test.txt", "a")

test_read_file.write("\nToby - Dev")  # write new in end of file
# becareful if u forget down line in file , you will have content in the same line so u should add "\n" in begin of text like :

test_read_file.write("\nEZ - Dev")

test_read_file.write("\n<p> GG Ez <\p>")
# u also can write HTML file using this feature

test_read_file.close()

# Modul and pip

print(tool_working.cong(3, 5))

# Class and Object

student1 = Student("Wray", "21020123")

print(student1.name)

student1.toString()

# inheritance

student2 = SmartStudent("HH", "21020124")

student2.toString()

print(student2.isSmart())
