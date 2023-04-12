num = input("Enter a number : ")

# num is a string,we need to convert it to int

num = int(num)

# intendation is important
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# operators
print(4 == 4)  # True

print(4 != 4)  # False

print(2 > 1)  # True

print(2 >= 2)  # True


# check 2 conditions
# logical operators
print(3 > 2 and 4 > 3)  # True

print(3 > 2 and 4 < 3)  # False

print(3 > 2 or 4 < 3)  # True

# Write a program that asks user to enter dish name and it should print which cuisine is that dish.
indian = ["samosa", "dal", "roti", "chicken tikka"]
chinese = ["noodles", "fried rice", "chow mein", "spring roll"]
italian = ["pizza", "pasta", "risotto", "bruschetta"]

dish = input("Enter a dish name : ")

if dish in indian:
    print("Indian Cuisine")
elif dish in chinese:
    print("Chinese Cuisine")
elif dish in italian:
    print("Italian Cuisine")
else:
    print("Based on little knowledge,I don't know which cuisne is ", dish)
