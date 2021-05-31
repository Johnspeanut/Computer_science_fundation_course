""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Home work 2
Programming Component
Problem 2:shapes.py
"""


def main():
    shape = input("Select a shape (triangle, square, or rectangle): ").upper()
    valid_shape = shape in ["TRIANGLE", "SQUARE", "RECTANGLE"]
    if valid_shape:
        width = float(input("Enter the width: "))
        if width > 0:
            if shape in ["TRIANGLE", "RECTANGLE"]:
                height = float(input("Enter the height: "))
                if height > 0:
                    if shape == "TRIANGLE":
                        area = width * height / 2
                    else:
                        area = width * height
                else:
                    print("Invalid height")
            else:
                area = width ** 2
            print("The area of the {} is {:.2f}".format(shape.lower(), area))
        else:
            print("Invalid width")
    else:
        print("Unknown shape")


if __name__ == "__main__":
    main()
