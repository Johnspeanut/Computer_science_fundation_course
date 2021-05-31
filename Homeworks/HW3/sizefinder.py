""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Home work 3
Programming Component
Problem 1:sizefinder.py
Program description: the program helps users to find their size based on
chese measurement in inches by kid, woman, and man.
"""


def size_checker(chest, gender):
    '''
    Function -- size_checker
        Calculates kid, man, or woman size.
    Parameters:
        chest -- Chest in inches. Integer data type.
        gender -- String. "M" for man; "W" for woman; "K" for kid.
    Returns:
        The size that it falls in, a String data type. If there is no matching
        size, return "not available".
    '''

    if gender == "K":
        if chest >= 26 and chest < 28:
            return "S"
        elif chest >= 28 and chest < 30:
            return "M"
        elif chest >= 30 and chest < 32:
            return "L"
        elif chest >= 32 and chest < 34:
            return "XL"
        elif chest >= 34 and chest < 36:
            return "XXL"
        return "not available"
    elif gender == "W":
        if chest >= 30 and chest < 32:
            return "S"
        elif chest >= 32 and chest < 34:
            return "M"
        elif chest >= 34 and chest < 36:
            return "L"
        elif chest >= 36 and chest < 38:
            return "XL"
        elif chest >= 38 and chest < 40:
            return "XXL"
        elif chest >= 40 and chest < 42:
            return "XXXL"
        return "not available"
    else:
        if chest >= 34 and chest < 37:
            return "S"
        elif chest >= 37 and chest < 40:
            return "M"
        elif chest >= 40 and chest < 43:
            return "L"
        elif chest >= 43 and chest < 47:
            return "XL"
        elif chest >= 47 and chest < 50:
            return "XXL"
        elif chest >= 50 and chest < 53:
            return "XXXL"
        return "not available"


def main():
    chest = float(input("Chest measurement in inches: "))
    kids_size = size_checker(chest, "K")
    womens_size = size_checker(chest, "W")
    mens_size = size_checker(chest, "M")
    if (kids_size == "not available" and womens_size == "not available" and
            mens_size == "not available"):
        print("Sorry, we don't carry your size")
    else:
        print("Your size choices:")
        print("Kids size:", kids_size)
        print("Womens size:", womens_size)
        print("Mens size:", mens_size)


if __name__ == "__main__":
    main()
