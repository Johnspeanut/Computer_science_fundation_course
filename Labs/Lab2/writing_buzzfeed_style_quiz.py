'''Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr. Abi Evans and Andrew Jelani
Lab 2 Problem： Writing a Buzzfeed-style quiz
What role would you play?
'''

def main():
    place = input("Where do you want to live? A -- Manhattan, NYC. B -- Miami. C -- countryside. ").upper()
    food = input("What's your favourite food? A -- Fried Chiken. B -- Vegetable.").upper()
    activity = input("What activity do you like? A -- Gym. B -- Cooking. C -- Movies").upper()
    valid_place = place in ["A", "B", "C"]
    valid_food = food in ["A", "B"]
    valid_activity = activity in ["A", "B", "C"]
    if valid_place and valid_food and valid_activity:
        if place in ["A", "B"]:
            if food == "A":
                if activity == "A":
                    role = "general"
                elif activity == "B":
                    role = "teacher"
                else:
                    role = "King"
            else:
                if activity == "B":
                    role = "retailer"
                elif activity == "A":
                    role = "fisherman"
                else:
                    role = "priest"
        else:
            role = "farmer"
    else:
        role = "farmer"
    print("You role would be {}.".format(role.capitalize()))


if __name__=="__main__":
    main()
