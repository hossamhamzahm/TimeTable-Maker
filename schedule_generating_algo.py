from copy import deepcopy
from combined_courses import (
    Course,
    all_labs,
    all_tuts,
    all_lecs,
    check_if_tut,
    check_if_lab,
    combined_courses
)

from structured_courses import(
    subject,
    week_days
)


empty_schedule = {}
schedules = []
for day in week_days:
    empty_schedule[day] = {}
    for period in range(8):
        empty_schedule[day][period] = False


time_idx_eq = {"8:30":0, "9:30":1, "10:30":2,
                "11:30":3, "12:30":4, "13:30":5,
                "14:30":6, "15:30":7,
                "9:20": 0, "10:20": 1,
                "11:20": 2, "12:20": 3, "13:20": 4,
                "14:20": 5, "15:20": 6, "16:20": 7}


def get_indices(time):
    idx1 = time.split(' ')[0]
    idx2 = time.split(' ')[2]
    return time_idx_eq[idx1], time_idx_eq[idx2]


def check_period(day, period):
    idx1, idx2 = get_indices(period)

    for i in range(idx1, idx2+1):
        if empty_schedule[day][i]:
            return False
    return True



def check_clash(times):
    for day, periods in times.items():
        for period in periods:
            if not check_period(day, period):
                return False
    return True


def mark(course, mark=True):
    idx1, idx2 = get_indices(course.lec.time_from + ' - ' + course.lec.time_to)
    # mark the lecture time
    for i in range(idx1, idx2+1):
        if mark: empty_schedule[course.lec.day][i] = course.lec.name
        else: empty_schedule[course.lec.day][i] = False
    
    # mark the tut time
    if check_if_tut(course.code):
        idx1, idx2 = get_indices(course.tut.time_from + ' - ' + course.tut.time_to)
        for i in range(idx1, idx2+1):
            if mark: empty_schedule[course.tut.day][i] = course.tut.name
            else: empty_schedule[course.tut.day][i] = False

    # mark the lab time
    if check_if_lab(course.code):
        idx1, idx2 = get_indices(course.lab.time_from + ' - ' + course.lab.time_to)
        for i in range(idx1, idx2+1):
            if mark: empty_schedule[course.lab.day][i] = course.lab.name
            else: empty_schedule[course.lab.day][i] = False



# (code, section, times, lec, tut, lab)
def generate_schedule(courses_arg, idx=-1):
    if(abs(idx) > len(courses_arg)):
        schedules.append(deepcopy(empty_schedule))
        return 0

    found_course = False
    for course in combined_courses:
        if course.code != courses_arg[idx]:
            continue
        found_course = True
        if not check_clash(course.times):
            continue
        
        # DO : mark the schedule
        mark(course)    
        # recurse
        generate_schedule(courses_arg, idx-1)
        # undo: unmark the schedule
        mark(course, False)

    if not found_course:
        print(f"There is no course with code {courses_arg[idx]}")


needed_courses = ["ECEN305", "NSCI102", "MATH206", "ECEN311", "ECEN313", "ECEN316"]
generate_schedule(needed_courses)


for schedule in schedules:
    print(schedule, end="\n")


# print(combined_courses[0].times)
# print(combined_courses[0].lec.time, combined_courses[0].lec.day)
# print(combined_courses[0].tut.time, combined_courses[0].tut.day)
# print(combined_courses[0].lab.time, combined_courses[0].lab.day)
# for course in combined_courses:
#     if course.code == "ECEN305":
#         if course.tut.name == course.lab.name:
#             print(course.tut.name, course.lab.name)
