""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Lab 5
Problem 3:draw a rectangle
"""

isFlag = True
while isFlag:
    notice = input("Draw a rectangle(Y/N): ")
    if notice == "N" or notice == "n":
        isFlag = False
    else:
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        draw_element = input("Enter a character that you wanna use to draw: ")
        print(draw_element * width)
        for i in range(height - 2):
            print(draw_element, " " * (width - 2), draw_element)
        print(draw_element * width)
