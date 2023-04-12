print(12+34)

print(11 % 2)  # 1

print(3**2)  # 9

print(2**4)  # 16 used for power

nyc_bal = 188  # distance between NYC and BAL
bal_pitt = 247  # distance between BAL and PIT
total_distance = nyc_bal+bal_pitt
print(total_distance)  # 435 used for calculating total distance

mph = 65
time = total_distance/mph
print(time)  # 6.6923076923076925

# used for rounding off the value upto 2 decimal places -6.69
print(round(time, 2))

# used for rounding off the value upto 3 decimal places -6.692
print(round(time, 3))

print(10+2*3)  # 16 why 16? because 2*3 is done first and then 10 is added to it

# 36 why 36? because 10+2 is done first and then 3 is multiplied to it
print((10+2)*3)

print(6-5.7)  # 0.2999999999999998 by default it would be float

print(round(6-5.7, 2))  # 0.3 by rounding off to 2 decimal places
