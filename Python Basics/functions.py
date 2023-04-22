#Functions- Block of code that performs a specific task

#Makes your code more readable and easier to debug

tom_exp_list=[2100, 3100, 2980, 3700, 4000];
joe_exp_list=[2400, 3500, 2000, 3420, 3100];

def calculate_total(exp) : 
    total = 0
    for item in exp:
        total = total+item
    return total

toms_total = calculate_total(tom_exp_list)
joes_total = calculate_total(joe_exp_list)
print("Tom's total expense is ", toms_total)
print("Joe's total expense is ", joes_total)


def sum(a,b):
    print("a : ",a)
    print("b : ",b)
    return a+b

#n=sum(2,3)
#by default the function has positional arguments
n=sum(b=5,a=6)#here we are passing the arguments by name
print("Total is  ",n)