import json

# get everything that is shared with the previous version
from BA_2023_courses import *

del possible_courses["cs_tech_track_2000_1"]
del possible_courses["cs_tech_track_2000_2"]
cs_tech_track_3000 = ["CSCI 3212", "CSCI 3313", "CSCI 3362" "CSCI 3401", "CSCI 3410", "CSCI 3411", "CSCI 3462", "CSCI 3532", "CSCI 3551", "CSCI 3552", "CSCI 3571", "CSCI 3907", "CSCI 3908", "CSCI 4223", "CSCI 4235", "CSCI 4237", "CSCI 4331", "CSCI 4341", "CSCI 4342", "CSCI 4345", "CSCI 4364", "CSCI 4366", "CSCI 4414", "CSCI 4415", "CSCI 4417", "CSCI 4418", "CSCI 4431", "CSCI 4431W", "CSCI 4454", "CSCI 4455", "CSCI 4511", "CSCI 4521", "CSCI 4525", "CSCI 4527", "CSCI 4531", "CSCI 4532", "CSCI 4533", "CSCI 4541", "CSCI 4551", "CSCI 4552", "CSCI 4553", "CSCI 4554", "CSCI 4561", "CSCI 4572", "CSCI 4577", "CSCI 4907"]
possible_courses["cs_tech_track_3000_1"] = getFullNameFromNum(all_courses, cs_tech_track_3000)
possible_courses["cs_tech_track_3000_2"] = possible_courses["cs_tech_track_3000_1"]

ntt_electives_2024 = ntt.copy()
for course in all_courses:
	if "LSPA" in course:
		ntt_electives_2024.remove(course)

# in this year any CS course above 3000 counts as an elective
# but here they restirct to only 2 CS electives, the rest are other major/minor so we have to regenerate what it means to be an elective
BA_2024_cs_allowed_electives = ntt_electives_2024.copy()
for course in cs_tech_courses:
	cs_name = course.split("#")[0]
	cs_num = cs_name.split(" ")[1]
	if int(cs_num[:4]) >= 3000:
		BA_2024_cs_allowed_electives.append(course)

possible_courses["elective_1_CS_okay"] = BA_2024_cs_allowed_electives
possible_courses["elective_2_CS_okay"] = BA_2024_cs_allowed_electives
possible_courses["elective_1_ntt"] = ntt_electives_2024
possible_courses["elective_2_ntt"] = ntt_electives_2024
possible_courses["elective_3_ntt"] = ntt_electives_2024
possible_courses["elective_4_ntt"] = ntt_electives_2024
possible_courses["elective_5_ntt"] = ntt_electives_2024
possible_courses["elective_6_ntt"] = ntt_electives_2024
possible_courses["elective_7_ntt"] = ntt_electives_2024
possible_courses["elective_8_ntt"] = ntt_electives_2024
possible_courses["elective_9_ntt"] = ntt_electives_2024
possible_courses["elective_10_ntt"] = ntt_electives_2024
possible_courses["elective_11_ntt"] = ntt_electives_2024
possible_courses["elective_12_ntt"] = ntt_electives_2024

result = {"requirements": possible_courses}
with open("possible_courses_BA_2024.json", "w") as fp: 
	json.dump(result , fp) 


big_dict = reformatForFrontEnd(possible_courses)
big_dict["degree"] = "BA 2024-2025"
semesters = [
        ["cs1010", "cs1111", "calc_1", "seas1001", "uw1020", "gened_ss_1"],
        ["cs1112", "cs1311", "elective_12_ntt", "sci_1", "gened_ss_2"],
        ["cs2113", "elective_1_CS_okay", "sci_2", "stats", "gened_hum_1"],
        ["cs2441W", "cs_architecture", "elective_2_CS_okay", "elective_1_ntt", "gened_hum_2"],
        ["cs_tech_track_3000_1", "", "elective_2_ntt", "elective_3_ntt", "elective_4_ntt", "gened_arts"],
        ["cs3212", "gened_global_1", "elective_5_ntt", "elective_6_ntt", "gened_hum_3"],
        ["cs_tech_track_3000_2", "cs_tech_track_4000_1", "elective_7_ntt", "elective_8_ntt", "gened_global_2"],
        ["cs_tech_track_4000_2", "elective_9_ntt", "elective_10_ntt", "elective_11_ntt", "gened_hum_4"]
    ]
big_dict["semesters"] = semesters

with open("BA_2024-2025.json", "w") as fp: 
	json.dump(big_dict , fp) 