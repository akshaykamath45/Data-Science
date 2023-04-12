text = "ice cream"
print(text)

# using index, we can access the characters in a string

print(text[0])  # i
print(text[1])  # c

# text[0]='g'#TypeError: 'str' object does not support item assignment,they are immutable

# using slicing, we can access the characters in a string

print(text[0:3])  # ice  from 0 to 3-1

print(text[4:9])  # cream from 4 to 9-1

print(text[4:])  # cream from 4 to end

print(text[:3])  # ice from start to 3-1

# use  " " instead of ' ' to print the string with ' in it
# print('I'm a student') #SyntaxError: invalid syntax

# address="1 purple street
# newyork
# usa"
# This will give error,we should use ''' ''' or """ """ to print the string in multiple lines

address='''1 purple street
newyork
usa'''
print(address)


#String Concatenation

s1="Hello"
s2="World"
print(s1+s2) #HelloWorld

s="Total states in USA is "
num=25
#print(num+25) -->not possible,we can't add string and int

print(s+str(num)) #Total states in USA is 25