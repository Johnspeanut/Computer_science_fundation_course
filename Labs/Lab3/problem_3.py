""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Lab 3
Problem 3: Days until Friday
"""

def weekday_num(str_day):
    '''
    Function -- weekday_num
        Calculates weekday number
    Parameters:
        stry_day -- any one in ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su'], String 
                    data type.Must be upper case.
    Returns:
        The number of a weekday, integer data type. If input is
        invalid, return "Not valid input"
    '''

    valid_day = str_day in ['M', 'TU', 'W', 'TH', 'F', 'SA', 'SU']
    if not valid_day:
        print("Not valid input")
    else:
        if str_day == "M":
            return 1
        elif str_day == "TU":
            return 2
        elif str_day == "W":
            return 3
        elif str_day == "TH":
            return 4
        elif str_day == "F":
            return 5
        elif str_day == "SA":
            return 6
        else:
            return 7


def num_day_until(current_day, until_day):
    '''
    Function -- num_day_until
        Calculates the number of days between current day and until day
    Parameters:
        current_day -- current day number, integer data type.
        until_day -- The until day number, integer data type.
    Returns:
        How many days there are between current day and until day, integer
        data type. If input is invalid(negative), return 0
    '''

    if current_day <= 0 or until_day <= 0:
        return 0
    else:
        if current_day <= until_day:
            return until_day - current_day
        else:
            return until_day + 7 - current_day


def main():
    name = input("Enter your name: ")
    print("Hello, " + name)
    current_day = input("Enter the current day ('M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su')").upper()
    UNTIL_DAY = "F"
    current_day_num = weekday_num(current_day)
    until_day_num = weekday_num(UNTIL_DAY)
    number_of_days_until = num_day_until(current_day_num, until_day_num)
    print("The current day is {}. The number of {} days until {}.".format(current_day, number_of_days_until, UNTIL_DAY))


if __name__ == "__main__":
    main()
