""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Home work 2
Programming Component
Problem 3:exercise.py
"""


def main():
    weekday = input("What day is it? ").upper()
    valid_weekday = weekday in ["M", "TU", "W", "TH", "F", "SA", "SU"]
    holiday = input("Is it a holiday? ").upper()
    valid_holiday = holiday in ["Y", "N"]
    rain_day = input("Is it raining? ").upper()
    valid_rain_day = rain_day in ["Y", "N"]
    temperature = float(input("What is the temperature? "))

    if valid_weekday and valid_holiday and valid_rain_day:
        workout_day = weekday in ["M", "W", "F", "SA"] or holiday == "Y"
        if workout_day:
            if rain_day == "Y":
                activity = "swim"
            elif weekday == "SA" or holiday == "Y":
                activity = "hike"
            else:
                activity = "run"
            if activity == "run" and (temperature > 75 or temperature < 35):
                duration = 30
            else:
                duration = 45
            print("{} for {} minutes".format(activity, duration).capitalize())
        else:
            print("Take a rest day")
    else:
        print("Swim for 35 minutes")


if __name__ == "__main__":
    main()
