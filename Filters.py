from timetable_generating_algorithm import *
import pickle

def Filter(TimeTables, filters, mode):
    """put the filter names wanted in a list in filters argument, filters will be applied in the order of the list
    supported Filters:
    1- "same_section" --> return all timetables that has the same section number in each subject

    mode="debug" --> return modified timetable and prints number of timetables after filtering
    mode="exec" --> reutrn modified timetables only"""
    if "same_section" in filters:
        new = []
        for i in TimeTables:
            condition = True
            for c, a in enumerate(i):
                for d, b in enumerate(i):
                    if c != d:
                        if a.name.split('-')[0] == b.name.split('-')[0]:
                            if a.section != b.section:
                                condition = False
            else:
                if condition:
                    new.append(i)
        if mode == "debug":
            print(f"Number of possible Timetables with same section in each subject: {len(new)}")
        elif mode == "exec":
            pass
        else:
            raise ValueError("Mode not supported")
    return new

if __name__ == "__main__":
    TimeTables = retrieveTimeTable()
    # applying filters
    modifiedTimeTables = Filter(TimeTables, ["same_section"], "debug")
    #  exporting filtered timetables into csv files
    exportTimeTable(createCSVlists(modifiedTimeTables, False), False)
