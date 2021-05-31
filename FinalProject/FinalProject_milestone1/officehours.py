class Officehours():
    def __init__(self, start_hour, end_hour, week, location, host):
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.week = week
        self.location = location
        self.host = host
    
    def is_happening_at(self, time, day):
        return day == self.week and time >= self.start_hour and time <= self.end_hour


def main():
    """
      office_hours = {
        "day": "Tu",
        "start": 16,
        "end": 18,
        "location": "225, Huddle 1",
        "host": "Mr. T"
    }
    """
    oh = Officehours(16, 18, "Tu", "225, Huddle 1" , "Mr. T")
    oh.is_happening_at(17, "Tu")
    print(oh.is_happening_at(17, "Sa"))

main()

    