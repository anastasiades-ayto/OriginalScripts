#Andrew Anastasiades
#This project is intended to apply OOP models to better understand the MTV game show "Are You The One?"
#If John and Brianna are a match then holy fuck

#Import 3rd party modules
from itertools import permutations
import openpyxl

#Import Classes
from week_class import Week

#Import Data manipulation
import workbook_io as io


# Instantiate all weeks
weeks = [Week(0), Week(1), Week(2), Week(3), Week(4), Week(5), Week(6), Week(7), Week(8), Week(9), Week(10)] 

#Define size of game
number_of_matches = 10

def get_total(pairs):
    baseline = list(permutations(range(pairs)))
    return baseline

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
    weeks[0].starting_set = total_possible
    weeks[0].build_ending_set()
    write_to_file(weeks[0], True)

def build_week_dict(week_obj, pairs = number_of_matches):
    all_booths = io.get_booths()
    cer_list = io.get_ceremony(pairs, week_obj.workbook_range)
    return_dict = all_booths[week_obj.week_number]
    return_dict["ceremony"] = cer_list[0]
    return_dict["matches"] = cer_list[1]
    return return_dict
    
def build_week_with_dict(week_obj, prev_week_obj):
    week_dict = build_week_dict(week_obj, number_of_matches)
    week_obj.ceremony = week_dict["ceremony"]
    week_obj.matches = week_dict["matches"]
    week_obj.booth = week_dict["booth"]
    week_obj.booth_is_match = week_dict["booth_is_match"]
    week_obj.build_starting_set_from_file(prev_week_obj.text_filename)

def analyze_week(week_obj):
    week_dict = build_week_dict(week_obj, number_of_matches)
    week_obj.build_ending_set()
    week_obj.narrow_ending_set( week_dict["booth"], week_dict["booth_is_match"])
    week_obj.print_number_possible()

def save_week(week_obj):
    write_to_file(week_obj)
    if len(week_obj.ending_set) < 20000:
        write_to_workbook(week_obj)

def build_analyze_save(week_obj, prev_week_obj):
    build_week_with_dict(week_obj, prev_week_obj)
    analyze_week(week_obj)
    save_week(week_obj)

def segment_set(set_to_segment, segmentor):
    holding_list = list()
    for i in range(len(segmentor)+1):
        holding_list.append(list())
        
    for each in set_to_segment:
        count = 0
        for i in range(len(segmentor)):
            if (each[i] == segmentor[i]):
                count+=1
        holding_list[count].append(each)
    return holding_list

begin_game(number_of_matches)
#build_analyze_save(weeks[1], weeks[0])
#build_analyze_save(weeks[2], weeks[1])
#build_analyze_save(weeks[3], weeks[2])
#build_analyze_save(weeks[4], weeks[3])
#build_analyze_save(weeks[5], weeks[4])
#build_analyze_save(weeks[6], weeks[5])
#build_analyze_save(weeks[7], weeks[6])
#build_analyze_save(weeks[8], weeks[7])
#build_analyze_save(weeks[9], weeks[8])


def print_segmented_set( distributed_set ):
    for i, val in enumerate(distributed_set):
        print( "With", i, "match(es) there are", len(val), "possible")


