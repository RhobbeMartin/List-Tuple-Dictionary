'''
03/01/2021

List

A data structure that is mutable (changeable) ordaered a sequence of elements. Define by having values between square brackets, [].

student1 = "John"

student2 = ["John", "Chloe", "Ian", "Ashley"]
print (student2)
>>["John", "Chloe", "Ian", "Ashley"]

box = ["Anything", 123, True, 4.28, -13]
print(box)
>>["Anything", 123, True, 4.28, -13]


Indexing ListEach item in a list corresponds to an indexing number, which uses an integer; starting with 0.


print (box[1])


List Functions 

adding element/items
1. LIST.append(ELEMENT)
2. LIST.insert(INDEX, ELEMENT)


'''
box = ["Anything", 123, True, 4.28, -13]
box.append("toy")
box.insert(1, False)

print (box)

import random
pizzaToppings = ["pineapple", "pepperoni", "olives", "mushroom", "bellpeppers", "bacon"]
#"pineapple = 0", "pepperoni = 1", "olives = 2", "mushroom = 3", "bellpeppers = 4", "bacon = 5"
print (len(pizzaToppings))

print(pizzaToppings[2])

pizzaToppings.append("extra cheese") # add
pizzaToppings.remove("mushroom") # take away
pizzaToppings.insert(5, "spinach") # in between extracheese and bacon
pizzaToppings.pop(2) # remove certain number area

print(len(pizzaToppings))
print(pizzaToppings)

# While version
index = 0
while(index <= len(pizzaToppings)-1):
  print(pizzaToppings[index])
  index = index + 1

# For version
for index in pizzaToppings:
  print(index)

for letters in pizzaToppings[4]:
  print(letters)

print(pizzaToppings[random.randint(0, len(pizzaToppings)-1)])


teacher = {}
teacher["name"] = "Celine"
teacher["favorite color"] = "Yellow"
teacher["favorite fruit"] = "Banana"
teacher["height"] = "5'2"

print(teacher)
print(teacher["favorite fruit"])