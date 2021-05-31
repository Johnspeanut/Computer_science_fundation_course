""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Home work 2
Programming Component
Problem 1:registration.py
"""


def main():
    course_number = input("Enter a course number: ").upper().replace(" ", "")
    valid_course = course_number in ["X101", "X102", "B500", "B525", "B701"]
    if valid_course:
        if course_number in ["X101", "X102"]:
            print("You have successfully registered for {}".format(
                course_number))
        else:
            grade_x101 = input("What grade did you get for X101? ").upper()
            grade_x102 = input("What grade did you get for X102? ").upper()
            if grade_x101 in ["A", "B"] and grade_x102 in ["A", "B", "C"]:
                print("You meet all the prerequisites and have successfully "
                      "registered for {}".format(course_number))
            else:
                print("You do not meet the prerequisites for"
                      " {}".format(course_number))
    else:
        print("Invalid course number")


if __name__ == "__main__":
    main()
