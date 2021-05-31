'''Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr. Abi Evans and Andrew Jelani
Lab 1 Problem 2: Buying a house
'''

def main():
    house_price = float(input("Enter the cost of the house: "))
    annual_salary = float(input("Enter the annual salary: "))
    percentage_monthly_save = float(input("Enter the proportion that user can save from their monthly salary(a float between 0 and 1): "))
    downpayment = 0.25 * house_price
    save_montly = (annual_salary/12) * percentage_monthly_save
    months_for_downpayment = downpayment / save_montly
    years_save = months_for_downpayment // 12
    month_save = round(months_for_downpayment % 12)
    msg = "If you save $" + str(round(save_montly,2)) + " per month. It will take you " + str(years_save) + " years and " + str(month_save) + " months to save enought for the down payment. "
    print(msg)

if __name__=="__main__":
    main()

