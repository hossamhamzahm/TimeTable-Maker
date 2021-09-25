import copy
from structured_courses import(
    LAB as all_labs,
    TUT as all_tuts,
    LEC as all_lecs,
    subject
)

class Course:
    def __init__(self, code, section, times, lec, tut, lab):
        self.code = code
        self.section = section
        self.times = times
        self.lec = lec
        self.tut = tut
        self.lab = lab


# Sorting all lectures according to their names then the time
all_lecs = sorted(all_lecs, key=lambda x: x.name+x.time)
all_tuts = sorted(all_tuts, key=lambda x: x.name+x.time)
all_labs = sorted(all_labs, key=lambda x: x.name+x.time)



# class subject:
#     name
#     code
#     section
#     division
#     activity
#     instructor
#     times
#     room

# maping tuts and labs names for O(1) checking 
is_tut = {}
is_lab = {}

for tut in all_tuts:
    is_tut[tut.code] = True

for lab in all_labs:
    is_lab[lab.code] = True

def check_if_tut(tut_arg):
    try:
        if is_tut[tut_arg]: return True
        else: return False
    except Exception: return False


def check_if_lab(lab_arg):
    try:
        if is_lab[lab_arg]: return True
        else: return False
    except Exception: return False



# lists to hold the tutorial block combined 
# for example ECEN-1A 10.30 - 12.20
# instead of ECEN-1A 10.30 - 11.20
# instead of ECEN-1A 11.30 - 12.20
lecs_combined = []
tuts_combined = []
labs_combined = []

i = 0
start = None
while(i < len(all_lecs)):
    start = copy.deepcopy(all_lecs[i])
    while(i+1 < len(all_lecs) and start.code == all_lecs[i+1].code and start.section == all_lecs[i+1].section):
        i += 1

    start.time_to = all_lecs[i].time_to
    start.time = start.time_from + ' - ' + all_lecs[i].time_to
    lecs_combined.append(start)
    i += 1


i = 0
start = None
while(i < len(all_tuts)):
    start = copy.deepcopy(all_tuts[i])
    while(i+1 < len(all_tuts) and start.code == all_tuts[i+1].code and start.section == all_tuts[i+1].section and start.division == all_tuts[i+1].division):
        i += 1

    start.time_to = all_tuts[i].time_to
    start.time = start.time_from + ' - ' + all_tuts[i].time_to
    tuts_combined.append(start)
    i += 1



i = 0
start = None
while(i < len(all_labs)):
    start = copy.deepcopy(all_labs[i])
    while(i+1 < len(all_labs) and start.code == all_labs[i+1].code and start.section == all_labs[i+1].section and start.division == all_labs[i+1].division):
        i += 1

    start.time_to = all_labs[i].time_to
    start.time = start.time_from + ' - ' + all_labs[i].time_to
    labs_combined.append(start)
    i += 1


# course class initialization arguments
# (code, section, times, lec, tut, lab)


# a list contains all the courses linked to their tutorials and labs 
combined_courses = []
for lec in lecs_combined:
    all_times = {}
    all_times[lec.day] = [lec.time]

    if not check_if_tut(lec.code) and not check_if_lab(lec.code):
        combined_courses.append(
            Course(lec.code, lec.section, all_times, lec, None, None))
        continue

    if check_if_tut(lec.code):
        for tut in tuts_combined:
            if(tut.code != lec.code or tut.section != lec.section):
                continue
            all_times_t = copy.deepcopy(all_times)
            try: 
                if not all_times_t[tut.day]: all_times_t[tut.day] = [tut.time]
                else: 
                    try:
                        if all_times_t[tut.day].index(tut.time):
                            continue
                    except Exception: pass
                    all_times_t[tut.day].append(tut.time)
            except Exception: all_times_t[tut.day] = [tut.time]

            if not check_if_lab(lec.code):
                combined_courses.append(
                    Course(lec.code, lec.section, all_times_t, lec, tut, None))
                continue
            
            for lab in labs_combined:
                if(lec.code != lab.code or lec.section != lab.section):
                    continue
                all_times_l = copy.deepcopy(all_times_t)
                try: 
                    if not all_times_l[lab.day]: all_times_l[lab.day] = [lab.time]
                    else: 
                        try:
                            if all_times_l[lab.day].index(lab.time):
                                continue
                        except Exception: pass
                    all_times_l[lab.day].append(lab.time)
                except Exception: all_times_l[lab.day] = [lab.time]

                combined_courses.append(Course(lec.code, lec.section, all_times_l, lec, tut, lab))
                # print(lec.name, all_times_l)
                # break

            if not check_if_lab(lec.code): break


    if not check_if_tut(lec.code) and check_if_lab(lec.code):
        for lab in labs_combined:
            if(lec.code != lab.code or lec.section != lab.section):
                continue
            all_times_l = copy.deepcopy(all_times)
            try:
                if not all_times_l[lab.day]: all_times_l[lab.day] = [lab.time]
                else:
                    try:
                        if all_times_l[lab.day].index(lab.time):
                            continue
                    except Exception: pass
                all_times_l[lab.day].append(lab.time)
            except Exception: all_times_l[lab.day] = [lab.time]

            combined_courses.append(
                Course(lec.code, lec.section, all_times_l, lec, None, lab))


# if __name__ == '__main__':
#     for course in combined_courses:
#         print(course.lec.name, course.section)
#         print(course.times, end="\n\n")
#         try:
#             print('---'+course.tut.code, course.tut.section, course.tut.division)
#             print('------'+course.lab.code, course.lab.section, course.lab.division)
#         except Exception: pass
        
#         for d, t in course.times.items():
#             print(d, ":", end=" ")
#             for tt in t: print(tt, end=", ")
#             print()
#         print()
#         print()

    # for lec in combined_courses:
    #     print(lec.code, end="\n\n")

