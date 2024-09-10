import json

# get everything that is shared with the previous version
from BA_2022_courses import *

del possible_courses["calc_2"]
possible_courses["elective_12_ntt"] = ntt

result = {"requirements": possible_courses}
with open("possible_courses_BA_2023.json", "w") as fp: 
	json.dump(result , fp) 

big_dict = reformatForFrontEnd(possible_courses)
big_dict["degree"] = "BA 2023-2024"
semesters = [
        ["cs1010", "cs1111", "calc_1", "seas1001", "uw1020", "gened_ss_1"],
        ["cs1112", "cs1311", "elective_12_ntt", "sci_1", "gened_ss_2"],
        ["cs2113", "elective_1_CS_okay", "sci_2", "stats", "gened_hum_1"],
        ["cs2441W", "cs_architecture", "elective_2_CS_okay", "elective_1_ntt", "gened_hum_2"],
        ["cs_tech_track_2000_1", "", "elective_2_ntt", "elective_3_ntt", "elective_4_ntt", "gened_arts"],
        ["cs3212", "gened_global_1", "elective_5_ntt", "elective_6_ntt", "gened_hum_3"],
        ["cs_tech_track_2000_2", "cs_tech_track_4000_1", "elective_7_ntt", "elective_8_ntt", "gened_global_2"],
        ["cs_tech_track_4000_2", "elective_9_ntt", "elective_10_ntt", "elective_11_ntt", "gened_hum_4"]
    ]
big_dict["semesters"] = semesters

with open("BA_2023-2024.json", "w") as fp: 
	json.dump(big_dict , fp) 

