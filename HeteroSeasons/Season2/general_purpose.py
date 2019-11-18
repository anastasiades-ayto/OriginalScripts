#Andrew Anastasiades
#This project is intended to apply OOP models to better understand the MTV game show "Are You The One?"
#If John and Brianna are a match then holy fuck

#Import 3rd party modules
from itertools import permutations
import openpyxl

#Import Classes
from week_class import Week

#Import Data
import info

# Instantiate all weeks
weeks = [Week(0), Week(1), Week(2), Week(3), Week(4), Week(5), Week(6), Week(7), Week(8), Week(9), Week(10)] 
#Define size of game
number_of_matches = 10

def get_total(pairs):
    baseline = list(permutations(range(pairs)))
    totes = list()
    for each in baseline:
        for i in range(10):
            new = (i,) + each
            totes.append(new)
    print("There are " + str(len(totes)) + " total matches possible")
    return totes

def write_to_file(week_obj, timeout_tracking = False):
    filename = week_obj.text_filename
    set_to_save = week_obj.ending_set
    with open(filename, mode='w', encoding='utf-8') as f:
        for i in range(len(set_to_save)):
            f.write(str(set_to_save[i]))
            f.write('\n')
            if timeout_tracking:
                if (i%1000000==0):
                    print(str(i) + " lines written")
              
def write_to_workbook(week_obj):
  wb = openpyxl.Workbook()
  ws = wb.active
  ws.title = week_obj.string
  set_to_save = week_obj.ending_set
  for i in range(len(set_to_save)):
    this_match = set_to_save[i]
    for j in range(len(this_match)):
      this_cell = ws.cell(i+1, j+1, this_match[j])
  wb.save(week_obj.workbook_filename)

#This function should only be executed at the beginning of the season (it's very time consuming)
def begin_game(num):
    total_possible = get_total(num)
    write_to_file(total_possible, "Total Matches.txt")
#begin_game(number_of_matches)

def build_week_with_dict(week_obj, week_dict, prev_week_obj):
    week_obj.ceremony = week_dict["ceremony"]
    week_obj.matches = week_dict["matches"]
    week_obj.booth = week_dict["booth"]
    week_obj.booth_is_match = week_dict["booth_is_match"]
    week_obj.build_starting_set_from_file(prev_week_obj.text_filename)

def analyze_week(week_obj, week_dict):
    week_obj.build_ending_set()
    week_obj.narrow_ending_set( week_dict["booth"], week_dict["booth_is_match"])
    if week_dict["christina_is_match"] != -1:
        temp_tuple = tuple([0, week_dict["booth"][1]])
        week_obj.narrow_ending_set( temp_tuple, week_dict["christina_is_match"])
    week_obj.print_number_possible()

def save_week(week_obj):
    write_to_file(week_obj)
    if len(week_obj.ending_set) < 10000:
        write_to_workbook(week_obj)

def build_analyze_save(week_obj, week_dict, prev_week_obj):
    build_week_with_dict(week_obj, week_dict, prev_week_obj)
    analyze_week(week_obj, week_dict)
    save_week(week_obj)
    
#build_analyze_save(weeks[1], info.week_1, weeks[0])
#build_analyze_save(weeks[2], info.week_2, weeks[1])
#build_analyze_save(weeks[3], info.week_3, weeks[2])
#build_analyze_save(weeks[4], info.week_4, weeks[3])
build_analyze_save(weeks[5], info.week_5, weeks[4])
build_analyze_save(weeks[6], info.week_6, weeks[5])
build_analyze_save(weeks[7], info.week_7, weeks[6])
build_analyze_save(weeks[8], info.week_8, weeks[7])
build_analyze_save(weeks[9], info.week_9, weeks[8])

    
