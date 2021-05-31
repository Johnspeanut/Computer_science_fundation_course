""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Home work 3
Programming Component
Problem 2:expenses.py
"""


def calculate_mileage(start, end):
    '''
    Function -- calculate_mileage
        Calculates miles driven using the start and end odometer values.
    Parameters:
        start -- The odometer reading at the start of the trip. Expecting a
                 number greater than 0.
        end -- The odometer reading at the end of the trip. Expecting a number
               greater than 0 and greater than the start value
    Returns:
        The miles driven, a number. If either parameter is invalid (e.g. either
        parameter is negative or end is less than start), returns 0.
    '''

    if start > 0 and end > 0 and end >= start:
        return end - start
    else:
        return 0


def get_reimbursement_amount(miles):
    '''
    Function -- get_reimbursement_amount
        Calculates the amount in dollars that the employee should be reimbursed
        based on their mileage and the standard rate per mile.
        The standard rate is 57.5
    Parameters:
        mileage -- The number of miles driven.
    Returns:
        The amount the employee should be reimbursed in dollars, a float
        rounded to 2 decimal places.
    '''

    REIMBURSEMENT_RATE = 57.5
    return round(REIMBURSEMENT_RATE * miles / 100, 2)


def get_actual_mileage_rate(mpg, fuel_price):
    '''
    Function -- get_actual_mileage_rate
        Calculates the actual trip cost per mile in dollars based on the car's
        MPG and the fuel price.
    Parameters:
        mpg -- The car's miles per gallon (MPG), an integer greater than 0.
        fuel_price -- The feul cost in dollars per gallon, a non-negative float
    returns:
        The actual cost per mile in dollars, a float rounded to 4 decimal.
        If supplied arguments are invalid, returns 0.0
    '''

    if mpg > 0 and fuel_price > 0:
        return round(1 / mpg * fuel_price, 4)
    else:
        return 0


def get_actual_trip_cost(start, end, mpg, fuel_price):
    '''
    Function -- get_actual_trip_cost
        Calculates the cost of a trip in dollars based on the miles driven, the
        MPG of the car, and the fuel price per gallon.
    Parameters:
        start -- The odometer reading at the start of the trip. Expecting a
        number greater than 0.
        end -- The odometer reading at the end of the trip. Expecting a number
        greater than 0 and greater than the start value.
        mpg -- The car's miles per gallon, an integer greater than 0.
        fuel_price -- The fuel price per gallon, a non-negative float.
    Returns:
        The cost of the drive in dollars, a float rounded to 2 decimal places.
        If any of the supplied arguments are invalid, return 0.0
    '''

    if start > 0 and end > 0 and end >= start and mpg > 0 and fuel_price >= 0:
        cost = 1 / mpg * fuel_price * calculate_mileage(start, end)
        return round(cost, 2)
    else:
        return 0


def main():
    msg = ("MILEAGE REIMBURSEMENT CALCULATOR\nOptions:\n1 - Calculate "
           "reimbursement amount from odometer readings\n2 - Calculate "
           "reimbursement amount from miles traveled\n3 - Calculate the "
           "actual cost of your trip")
    print(msg)
    choice = int(input("Enter your choice (1, 2, or 3): "))
    valid_choice = choice in [1, 2, 3]
    if not valid_choice:
        print("Not a valid choice")
    elif choice == 1:
        start_odo = float(input("Enter your starting odometer reading: "))
        end_odo = float(input("Enter your ending odometer reading: "))
        miles = calculate_mileage(start_odo, end_odo)
        cost_odo = get_reimbursement_amount(miles)
        print("You will be reimbursed ${}".format(cost_odo))
    elif choice == 2:
        miles = float(input("Enter the number of miles traveled: "))
        cost_travel = get_reimbursement_amount(miles)
        print("You will be reimbursed ${}".format(cost_travel))
    else:
        start = float(input("Enter your starting odometer reading: "))
        end = float(input("Enter your ending odometer reading: "))
        mpg = float(input("Enter your car's MPG: "))
        fuel_price = float(input("Enter the fuel price per gallon: "))
        cost_actual = get_actual_trip_cost(start, end, mpg, fuel_price)
        print("Your trip cost ${}".format(cost_actual))


if __name__ == "__main__":
    main()
