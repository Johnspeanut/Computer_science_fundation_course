""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Lab 3
Problem 1: One function, one job
"""


def downpayment(house_price, rate):
    '''
    Function -- downpayment
        Calculates downpayment amount
    Parameters:
        house_price -- The house price, float data type.
        rate -- downpayment rate, float data type.
    Returns:
        The downpayment buyer should pay, float data type. If either parameter 
        is invalid (e.g. either parameter is negative), returns 0.
    '''

    if house_price < 0 or rate < 0:
        return 0
    else:
        return house_price * rate

def save_monthly(annual_salary, save_rate):
    '''
    Function -- save_monthly
        Calculate how much you can save monthly
    Parameters:
        annual_salary -- The annual salary, float data type.
        save_rate -- save rate monthly, float data type.
    Returns:
        How much money you can save monthly, float data type. If either
        parameter is invalid (e.g. either parameter is negative), returns 0.
    '''

    if annual_salary < 0 or save_rate < 0:
        return 0
    else:
        return (annual_salary/12) * save_rate

def months_need_for_downpayment(downpayment_amount, save_monthly_amount):
    '''
    Function -- months_need_for_downpayment
        Calculate how many monthes you need to save for the downpayment
    Parameters:
        downpayment -- The downment amount you need to pay, float data type.
        save_monthly -- The amount you save monthly, float data type.
    Returns:
        How many monthes do you need for the downpayment, float data type. If
        either parameter is invalid (e.g. either parameter is negative), 
        returns 0.
    '''

    if downpayment_amount < 0 or save_monthly_amount <= 0:
        return 0
    else:
        return downpayment_amount / save_monthly_amount

def years_need_for_save(total_months_for_downpayment):
    '''
    Function -- years_need_for_save
        Calculate how many years you need to save for the downpayment
    Parameters:
        total_months_for_downpayment -- The total months needed for
                                        downpayment, float data type.
    Returns:
        How many years do you need for the downpayment, int data type. If
        either parameter is invalid (e.g. either parameter is negative), 
        returns 0.
    '''

    if total_months_for_downpayment < 0:
        return 0
    else:
        return total_months_for_downpayment // 12

def months_need_for_save(total_months_for_downpayment):
    '''
    Function -- months_need_for_save
        Calculate how many months you need to save for the downpayment
    Parameters:
        total_months_for_downpayment -- The total months needed for
                                        downpayment, float data type.
    Returns:
        How many months do you need for the downpayment, int data type ,round 2
        decimal. If either parameter is invalid (e.g. either parameter is
        negative), returns 0.
    '''

    if total_months_for_downpayment < 0:
        return 0
    else:
        return round(total_months_for_downpayment % 12)


def main():
    house_price = float(input("Enter the cost of the house: "))
    annual_salary = float(input("Enter the annual salary: "))
    percentage_monthly_save = float(input("""Enter the proportion that user can \
save from their monthly salary(a float between 0 and 1): """))
    DOWNPAYMENT_RATE = 0.25
    down_amount = downpayment(house_price, DOWNPAYMENT_RATE)
    save_mon = save_monthly(annual_salary, percentage_monthly_save)
    total_months = months_need_for_downpayment(down_amount, save_mon)
    msg = ("If you save $" + str(round(total_months, 2))
           + " per month. It will take you "
           + str(years_need_for_save(total_months)) + " years and "
           + str(months_need_for_save(total_months))
           + " months to save enought for the down payment. ")
    print(msg)

if __name__=="__main__":
    main()
