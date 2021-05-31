'''Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr. Abi Evans and Andrew Jelani
Lab 1 Problem 1:Easting out with a group problem
'''

def main():
    amount = float(input("How much was the bill? "))
    tip_share = float(input("How percentage tip do you want to pay(a float between 0 and 1): "))
    number_people = int(input("How many people: "))
    percentage_tip = tip_share * 100
    value = amount * (1+tip_share) / number_people
    msg = "The total amount of the bill is " + str(round(amount,2)) + ", excluding " + str(round(percentage_tip,2)) + "% of the bill for tips. Each person should pay " + str(round(value,2))
    print(msg)

if __name__=="__main__":
    main()


