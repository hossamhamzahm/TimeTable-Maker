import csv

# a list that will contain the rows of the csv file after proper formating
main_timetable = []

time_periods = ["8:30 - 9:20", "9:30 - 10:20", "10:30 - 11:20",
                "11:30 - 12:20", "12:30 - 13:20", "13:30 - 14:20", 
                "14:30 - 15:20", "15:30 - 16:20"]

week_days = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY"]


# opening the csv file
with open("Fall2021.csv", "r", encoding='mac_roman', newline='') as csv_file:
    # read the csv file using csv module
    csv_reader = csv.reader(csv_file, dialect=csv.excel)
    # append each row (list containing the elements of the row) 
    # of the csv file to main_timetable list
    for line in csv_reader:
        main_timetable.append(line)


# lecture info class
class subject_unorganised:
    def __init__(self, name, activity, instructor, room, day, time):
        self.name = name
        self.code = self.name.split('-')[0]
        try:
            self.section = self.name.split('-')[1][:2]
            self.division = self.name.split('-')[1][-1]
        except Exception:
            pass
        self.activity = activity
        self.instructor = instructor
        self.room = room
        self.day = day
        self.time = time
        self.time_from = time.split(' ')[0]
        self.time_to = time.split(' ')[2]
        # .split(' ')[1]

    def concatenate(self):
        self.name = f"{self.name}-{self.activity}"

    def __eq__(self, other) -> bool:
        str1 = self.name + self.activity + \
            self.instructor + self.room + self.day + self.time
        str2 = other.name + other.activity + \
            other.instructor + other.room + other.day + other.time
        return str1==str2

    def __ne__(self, other) -> bool:
        str1 = self.name + self.activity + \
            self.instructor + self.room + self.day + self.time
        str2 = other.name + other.activity + \
            other.instructor + other.room + other.day + other.time
        return str1 != str2

    def print(self):
        str = self.name + self.activity + \
            self.instructor + self.room + self.day + self.time
        return str



class subject:
    def __init__(self, name, activity, instructor, times, room="NA"):
        self.name = name
        self.code = self.name.split('-')[0]
        try:
            self.section = int(name.split('-')[1])
        except Exception:
            self.section = int(name.split('-')[1][:-1])
            self.division = name.split('-')[1][2]
        self.activity = activity
        self.instructor = instructor
        self.times = times
        self.room = room



# a list that will contain the number of the first row of each day 
days = []


# append the number of the row if it contains a day
for row in main_timetable:
    for day in week_days:
        if row[1] == day:
            days.append(int(row[0]))


# turn row number from string to int
for row in main_timetable:
    if row[0] != "":
        row[0] = int(row[0])


# collecting all courses in ALL_CLASSES_unorganised list 
# while using subject_unorganized class
ALL_CLASSES_unorganised = []

for idx, li in enumerate(main_timetable):
    if idx <= 1: continue

    for i in range(0, 5):
        if li[0] >= days[i]: 
            if(i<4 and li[0] >= days[i+1]): continue

            for j in range(2, 31, 4):
                if(li[j]) != "":
                    ALL_CLASSES_unorganised.append(
                        subject_unorganised(li[j], li[j+1], li[j+2], li[j+3], week_days[i], time_periods[j//4]))




# Separating lecs from tuts and labs
LEC = []
TUT = []
LAB = []

for course in ALL_CLASSES_unorganised:
    if course.activity[0:3] == "LEC":
        LEC.append(course)
    elif course.activity[0:3] == "TUT":
        TUT.append(course)
    elif course.activity[0:3] == "LAB":
        LAB.append(course)


# a part that is not used
# from dicts import *
