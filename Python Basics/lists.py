# Lists in Python

item1 = "bread"
item2 = "milk"
item3 = "eggs"

items = ["bread", "milk", "eggs"]  # list

print(items)  # ['bread', 'milk', 'eggs']

# accessing elements in a list
print(items[0])  # bread
print(items[1])  # milk

# Lists are mutable, meaning the value of elements of a list can be altered
items[0] = "chips"
print(items)  # ['chips', 'milk', 'eggs']

print(items[0:2])  # ['chips', 'milk']

print(items[-1])  # eggs

# Adding elements to a list
items.append("butter")  # ['chips', 'milk', 'eggs', 'butter']
print(items)
items.insert(1, "cheese")  # ['chips', 'cheese', 'milk', 'eggs', 'butter']
print(items)

# List Concatenation
food = ["bread", "pasta", "fruits"]
bathroom = ["soap", "shampoo", "toothpaste"]
concatenateList = food+bathroom
# ['bread', 'pasta', 'fruits', 'soap', 'shampoo', 'toothpaste']
print(concatenateList)

len(items)  # 5 returns the length of the list

# Look up an element in a list (checks if an element is present in the list)
"bread" in items  # True
"soda" in items  # False
