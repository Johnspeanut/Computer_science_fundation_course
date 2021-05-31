""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Lab 6
Problem 2:Greatest common divisor
"""

# Part 1

def greatest_common_divisor(num1, num2):
    if num2 != 0:
        return greatest_common_divisor(num2, num1 % num2)
    else:
        return num1

print("************************************************")
print(greatest_common_divisor(50, 24))
print(greatest_common_divisor(6, 8))
print(greatest_common_divisor(20, 12))
print(greatest_common_divisor(51050, 2355))
print(greatest_common_divisor(60, 24))


# Part 2
    # n = int(input("How many positive integers: "))
    # new_list = []
    # for i in range(n):
    #     i += 1
    #     num = int(input("Enter integer number: "))
    #     new_list.append(num)
def lst_GCD(lst):
    if len(lst) == 2:
        return greatest_common_divisor(lst[0], lst[1])
    else:
        return greatest_common_divisor(lst[0], lst_GCD(lst[1:]))

print("********************************************************")
print(lst_GCD([50, 60, 70, 80, 96]))
print(lst_GCD([50, 60, 70, 80, 95]))
print(lst_GCD([50, 60, 70, 80, 120]))
print(lst_GCD([50, 60, 70, 80, 3]))





