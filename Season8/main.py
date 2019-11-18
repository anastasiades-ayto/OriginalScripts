#Andrew Anastasiades
#Combinatorial work

#3rd Party Libraries
import itertools
import math
import openpyxl

#Local Libraries
import gameinfo as game


def partitions(s, r):
    s = set(s)
    assert(len(s) % r == 0)
    if len(s) == 0:
        yield ()
        return
    first = next(iter(s))
    rest = s.difference((first,))
    for c in itertools.combinations(rest, r - 1):
        first_subset = (first,) + c
        for p in partitions(rest.difference(c), r):
            yield (first_subset,) + p

def write_to_file(fileName, set_to_save):
    with open(fileName, mode='w', encoding='utf-8') as f:
            for i in range(len(set_to_save)):
                    f.write(str(set_to_save[i]))
                    f.write('\n')


def read_from_file(fileName):
    new_list = list()
    with open(fileName, mode='r', encoding='utf-8') as f:
        for line in f:
            #First we clean the String
            line = line[1:]
            line = line[0:-2]
            line = line[1:]
            line = line[0:-1]
            line = line.replace('), (', ', ')
            #Then we convert it to a list of strings
            line_list = line.split(', ')
            #Now we make it a list of integers
            for i, val in enumerate(line_list):
                line_list[i] = int(val)
            #Now we need to make it a list of tuples
            line_list_of_tuples = list()
            for i in range(8):
                i_1 = 2*i
                i_2 = 2*i+1
                temp_tuple = tuple([line_list[i_1], line_list[i_2]])
                line_list_of_tuples.append(temp_tuple)
            #Lastly, we append it to the output list
            new_list.append(line_list_of_tuples)
    return new_list

def narrow_set_with_ceremony(set_to_narrow, ceremony_list, number_of_matches):
    new_set = list()
    for each in set_to_narrow:
        count = 0
        for couple in ceremony_list:
            if couple in each:
                count+=1
        if count == number_of_matches:
            new_set.append(each)
    return new_set
          
def narrow_set_with_booth(set_to_narrow, booth_tuple, booth_is_match):
    new_set = list()
    for each in set_to_narrow:
        count = 0
        if (booth_tuple in each):
            count+=1
        if (count==booth_is_match):
            new_set.append(each)
    return new_set

def write_to_workbook(filename, set_to_save):
  wb = openpyxl.Workbook()
  ws = wb.active
  for i in range(len(set_to_save)):
    this_match = set_to_save[i]
    for j in range(len(this_match)):
      this_cell = ws.cell(i+1, j+1, str(this_match[j]))
  wb.save(filename)


#
start_filename = "Total Possible.txt"

def booth_update(week_num, booth_tup, is_match):
    input_filename = "Ceremony_"+str(week_num-1)+"_Output.txt"
    input_set = read_from_file(input_filename)
    output_set = narrow_set_with_booth(input_set, booth_tup, is_match)
    print("After booth "+str(week_num)+", there are "+str(len(output_set))+" possibilities")
    output_filename_txt = "Booth_"+str(week_num)+"_Output.txt"
    output_filename_xlsx = "Booth_"+str(week_num)+".xlsx"
    write_to_file(output_filename_txt, output_set)
    if len(output_set) < 10000:
        write_to_workbook(output_filename_xlsx, output_set)
          
def ceremony_update(week_num, cer_list, num_matches):
    input_filename = "Booth_"+str(week_num)+"_Output.txt"
    input_set = read_from_file(input_filename)
    output_set = narrow_set_with_ceremony(input_set, cer_list, num_matches)
    print("After ceremony "+str(week_num)+", there are "+str(len(output_set))+" possibilities")
    output_filename_txt = "Ceremony_"+str(week_num)+"_Output.txt"
    output_filename_xlsx = "Ceremony_"+str(week_num)+".xlsx"
    write_to_file(output_filename_txt, output_set)
    if len(output_set) < 10000:
        write_to_workbook(output_filename_xlsx, output_set)

##Booth 1 - This has to be done manually for now
##start_set = read_from_file(start_filename)
##booth_1 = (8,13)
##booth_1_match = False
##booth_1_filename = "Booth_1_Output.txt"
##booth_1_output = narrow_set_with_booth(start_set, booth_1, booth_1_match)
##write_to_file(booth_1_filename, booth_1_output)

##ceremony_update(1, game.cer_dict["1"], game.cer_matches_dict["1"])
##booth_update(2, game.booth_dict["2"], game.booth_match_dict["2"])
##ceremony_update(2, game.cer_dict["2"], game.cer_matches_dict["2"])
##booth_update(3, game.booth_dict["3"], game.booth_match_dict["3"])
##ceremony_update(3, game.cer_dict["3"], game.cer_matches_dict["3"])
##booth_update(4, game.booth_dict["4"], game.booth_match_dict["4"])
ceremony_update(4, game.cer_dict["4"], game.cer_matches_dict["4"])
booth_update(5, game.booth_dict["5"], game.booth_match_dict["5"])
ceremony_update(5, game.cer_dict["5"], game.cer_matches_dict["5"])
booth_update(6, game.booth_dict["6"], game.booth_match_dict["6"])
ceremony_update(6, game.cer_dict["6"], game.cer_matches_dict["6"])
booth_update(7, game.booth_dict["7"], game.booth_match_dict["7"])
ceremony_update(7, game.cer_dict["7"], game.cer_matches_dict["7"])
booth_update(8, game.booth_dict["8"], game.booth_match_dict["8"])
ceremony_update(8, game.cer_dict["8"], game.cer_matches_dict["8"])
booth_update(9, game.booth_dict["9"], game.booth_match_dict["9"])
ceremony_update(9, game.cer_dict["9"], game.cer_matches_dict["9"])

        

