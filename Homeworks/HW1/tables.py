""" 
Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Home work 1 
Programming Component
Program 2:tables.py
"""
def main():
    numberTops = int(input("Number of tops: "))
    numberLegs = int(input("Number of legs: "))
    numberScrews = int(input("Number of screws: "))
    numberTables = min(numberTops, numberLegs // 4, numberScrews // 8)
    leftoverTops = numberTops - numberTables
    leftoverLegs = numberLegs - numberTables*4
    leftoverScrews = numberScrews - numberTables*8
    msg = str(numberTables) + " tables assembled. Leftover parts: " + str(leftoverTops) + " tops, " + str(leftoverLegs) + " legs, " + str(leftoverScrews) + " screws."
    print(msg)

if __name__=="__main__":
    main()

""" Test cases
4 tops, 20 legs, 32 screws => 4 tables assembled. Leftover parts: 0 table tops, 4 legs, 0 screws.
100 tops, 89 legs, 200 screws => 22 tables assembled. Leftover parts: 78 table tops, 1 legs, 24 screws.
800 tops, 1500 legs, 3200 screws => 375 tables assembled. Leftover parts: 425 table tops, 0 legs, 200 screws.
"""
