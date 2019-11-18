#Andrew Anastasiades
#Defines the class "Week" which includes all information derived from one week of the show


class Week:

    all_weeks = list()
    
    #Intializer
    def __init__(self, week_number, starting_set = list(), booth = (-1, -1), booth_is_match = bool(), ceremony = tuple(), matches = 0):
        self.week_number = week_number
        self.string = "Week "+str(week_number)
        Week.all_weeks.append(self.string)
        self.starting_set = starting_set
        self.ending_set = list()
        self.booth = booth
        self.booth_is_match = booth_is_match
        self.ceremony = ceremony
        self.matches = matches
        self.text_filename = self.string + " Possibilities.txt"
        self.workbook_filename = self.string + " Possibilities.xlsx"
        self.workbook_range = "Cer_"+str(week_number)

    def build_starting_set_from_file(self, starting_filename):
        self.starting_set = list()
        with open(starting_filename, mode='r', encoding='utf=8') as f:
            for line in f:
                line = line[1:29] #they all have a '(' at the beginning and end
                line_string_list = line.split(', ')
                for i in range(len(line_string_list)):
                    line_string_list[i] = int(line_string_list[i])
                line_int_tuple = tuple(line_string_list)
                self.starting_set.append(line_int_tuple)

    def build_ending_set(self):
        temp_list = list()
        if (self.week_number == 0):
            temp_list = self.starting_set
        else:
            for each in self.starting_set:
                count = 0
                for i in range(len(self.ceremony)):
                    if (each[i] == self.ceremony[i]):
                        count+=1
                if (count == self.matches):
                    temp_list.append(each)
        self.ending_set = temp_list

    def get_ceremony(self, cer_list):
        self.ceremony = cer_list[0]
        self.matches = cer_list[1]

    def get_truth_booth(self, booth_dict):
        self.booth = (booth_dict["index"], booth_dict["value"])
        self.booth_is_match = booth_dict["is_match"]
                    
    def narrow_ending_set(self, match_tuple, match_bool):
        new_list = list()
        match_index = match_tuple[0]
        match_value = match_tuple[1]
        if (match_bool == True):
            for each in self.ending_set:
                if each[match_index] == match_value:
                    new_list.append(each)
        else:
            for each in self.ending_set:
                if (each[match_index] != match_value):
                    new_list.append(each)
        self.ending_set = new_list
         
    def print_number_possible(self):
        print("There are "+ str(len(self.ending_set)) + " possible matches at the end of " +self.string)


        
