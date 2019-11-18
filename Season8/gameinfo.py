#Andrew Anastasiades

cer_dict = {
    "1" : [(0,14), (1,13), (10,11), (8,12), (2,7), (3,15), (5,6), (4,9)],
    "2" : [(6,9), (2,7), (5,8), (1,13), (10,11), (0,3), (4,15), (12,14)],
    "3" : [(3,7), (0,12), (1,14), (4,9), (6,8), (2,15), (10,11), (5,13)],
    "4" : [(2,4), (7,11), (9,10), (8,12), (1,13), (0,15), (3,5), (6,14)],
    "5" : [(6,11), (1,13), (7,8), (3,12), (2,15), (4,10), (5,14), (0,9)],
    "6" : [(1,6), (2,7), (5,11), (4,9), (10,14), (8,12), (13,15), (0,3)],
    "7" : [(5,9), (8,12), (11,13), (1,4), (6,14), (2,7), (10,15), (0,3)],
    "8" : [(5,13), (2,7), (8,12), (4,11), (9,15), (1,14), (6,10), (0,3)],
    "9" : [(6,14), (1,11), (8,15), (10,12), (2,7), (5,13), (4,9), (0,3)],
    "10" : list(),#NA
    }

cer_matches_dict = {
    "1" : 2,
    "2" : 2,
    "3" : 2,
    "4" : 1,
    "5" : 0,
    "6" : 3,
    "7" : 3,
    "8" : 3,
    "9" : 6,
    "10" : 0#NA
    }

booth_dict = {
    "1" : (8,13),
    "2" : (3,15),
    "3" : (6,9),
    "4" : (4,6),
    "5" : (10,11),
    "6" : (0,3),
    "7" : (5,6),
    "8" : (14,15),
    "9" : (1,12),
    "10" : tuple()#NA
    }

booth_match_dict = {
    "1" : False,
    "2" : False,
    "3" : False,
    "4" : False,
    "5" : False,
    "6" : True,
    "7" : False,
    "8" : False,
    "9" : False,
    "10" : bool()#NA
    }

game = {
    "Season" : 8,
    "Game Type" : "Bisexual",
    "Number of Contestants" : 16,
    "Ceremonies" : cer_dict,
    "Ceromony Matches" : cer_matches_dict,
    "Booths" : booth_dict,
    "Booth Matches" : booth_match_dict
    }
