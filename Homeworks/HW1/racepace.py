""" 
Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Home work 1 
Programming Component
Program 1:racepace.py
"""
def main():
    runDistance = float(input("How many kilometers did you run? "))
    hours = int(input("What was your finish time? Enter hours: "))
    minutes = int(input("Enter minutes: "))
    pacePerMile = (hours*60*60 + minutes*60) / (runDistance/1.61)
    paceMinutes = pacePerMile // 60
    paceSeconds = pacePerMile % 60
    speedMile = runDistance/1.61 / (hours + minutes/60)
    msg = str(round((runDistance/1.61),2)) + " miles, " + str(int(paceMinutes)) + ":" + str(round(paceSeconds)) + " pace, " + str(round(speedMile,2)) + " MPH"
    print(msg)

if __name__=="__main__":
    main()

""" Test cases
5km, 0 hours, 30 minutes => 3.11 miles, 9:40 pace, 6.21 MPH
10km, 1 hours, 15 minutes => 6.21 miles, 12:5 pace, 4.97 MPH
23km, 3 hours, 44 minutes => 14.29 miles, 15:41 pace, 3.83 MPH
"""





