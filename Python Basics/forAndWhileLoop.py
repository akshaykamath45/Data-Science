# Store  monthly expenses in a list and find out total expenses for all months.

expense = [2340, 2500, 2100, 3100, 2980]
total = expense[0]+expense[1]+expense[2]+expense[3]+expense[4]
print(total)  # 13020

# instead we can use for loop to find the total

totalExpense = 0
for item in expense:
    totalExpense = totalExpense+item
print(totalExpense)  # 13020


# Print 1 to 10 using range() function
for i in range(1, 11):
    print(i)

# Print square of natural numbers from 1 to 10
for i in range(1, 11):
    print(i**2)  # or print(i*i)

 # using range() in monthly expenses example
totalExpense2 = 0
for i in range(len(expense)):
    print("Month ", i+1, " expense ", expense[i])
    totalExpense2 = totalExpense2+expense[i]

print("Total Expense is ", totalExpense2)  # 13020

# using break statement
key_location = "chair"
locations = ["table", "sofa", "bed", "chair"]
for item in locations:
    if item == key_location:
        print("Key is found in", item)
        break

# print square of numbers between 1 to 5 EXCEPT even numbers
for i in range(1, 6):
    if (i % 2 == 0):
        continue  # skips the even numbers
    print(i*i)

# while loop
i = 1
while i <= 10:
    print(i)
    i = i+1
