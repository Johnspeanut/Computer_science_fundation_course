""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Lab 4
Problem 3:Calculator
"""

def calculator():
    subtotal = float(input("Enter a number: "))
    operator = input("Enter the next step in the calculation: ").split()
    while operator[0].lower() != "q":
        if operator[0] == "+":
            subtotal += float(operator[1])
        elif operator[0] == "-":
            subtotal -= float(operator[1])
        elif operator[0] == "*":
            subtotal *= float(operator[1])
        elif operator[0] == "/":
            subtotal /= float(operator[1])
        print("Total = ", subtotal)
        operator = input("Enter the next step in the calculation: ").split()


def main():
    calculator()


if __name__ == "__main__":
    main()



