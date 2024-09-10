import json

# get everything that is shared with the CS BS
from course_list_imports import *

# CS BA courses ##################################################################################################

possible_courses["cs2441W"] = getFullNameFromNum(all_courses, ["CSCI 2441W", "CSCI 2541W"])
possible_courses["cs_architecture"] = getFullNameFromNum(all_courses, ["CSCI 3401", "CSCI 2461", "CSCI 2460"])

possible_courses["cs_tech_track_2113_1"] = getFullNameFromNum(all_courses, cs_tt_2113_prereq)
possible_courses["cs_tech_track_2113_2"] = possible_courses["cs_tech_track_2113_1"]
possible_courses["cs_tech_track_2113_3"] = possible_courses["cs_tech_track_2113_1"]

cs_BA_required_electives = ["CSCI 3212", "CSCI 3313", "CSCI 3410", "CSCI 3411"]
possible_courses["cs_tech_track_short_1"] = getFullNameFromNum(all_courses, cs_BA_required_electives)
possible_courses["cs_tech_track_short_2"] = possible_courses["cs_tech_track_short_1"]

# math courses ##################################################################################################

possible_courses["stats"] = getFullNameFromNum(all_courses, ["APSC 3115", "CSCI 3362", "CSCI 6362", "CSCI 4341", "STAT 1051", "STAT 1053"]) 

# gened requirements ##################################################################################################

possible_courses["gened_ss_1"] = getFullNameFromNum(all_courses, all_GPAC_courses['Critical Thinking, Quantitative Reasoning or Scientific Reasoning in the Social Sciences'])
possible_courses["gened_ss_2"] = possible_courses["gened_ss_1"]
possible_courses["gened_hum_1"] = getFullNameFromNum(all_courses, all_GPAC_courses['Critical Thinking in the Humanities'])
possible_courses["gened_hum_2"] = possible_courses["gened_hum_1"]
possible_courses["gened_hum_3"] = possible_courses["gened_hum_1"]
possible_courses["gened_hum_4"] = possible_courses["gened_hum_1"]
possible_courses["gened_arts"] = getFullNameFromNum(all_courses, all_GPAC_courses['Creative or Critical Thinking in the Arts'])
possible_courses["gened_global_1"] = getFullNameFromNum(all_courses, all_GPAC_courses['Global or Cross-Cultural Perspectives'])
possible_courses["gened_global_2"] = possible_courses["gened_global_1"]
possible_courses["sci_1"] = getFullNameFromNum(all_courses, all_GPAC_courses['Scientific Reasoning in Natural and/or Physical Lab Sciences'])
possible_courses["sci_2"] = possible_courses["sci_1"]
possible_courses["sci_3"] = possible_courses["sci_1"]

# other requirements ##################################################################################################

possible_courses["elective_1"] = electives
possible_courses["elective_2"] = electives
possible_courses["elective_3"] = electives
possible_courses["elective_4"] = electives
possible_courses["elective_5"] = electives
possible_courses["elective_6"] = electives
possible_courses["elective_7"] = electives
possible_courses["elective_8"] = electives
possible_courses["elective_9"] = electives
possible_courses["elective_10"] = electives
possible_courses["elective_11"] = electives
possible_courses["elective_12"] = electives

result = {"requirements": possible_courses}
with open("possible_courses_BA_2021.json", "w") as fp: 
	json.dump(result , fp) 

big_dict = reformatForFrontEnd(possible_courses)
big_dict["degree"] = "BA 2021-2022"
semesters = [
        ["cs1010", "cs1111", "calc_1", "seas1001", "uw1020", "gened_ss_1"],
        ["cs1112", "cs1311", "calc_2", "sci_1", "gened_ss_2"],
        ["cs2113", "elective_1", "sci_2", "stats", "gened_hum_1"],
        ["cs2441W", "cs_architecture", "sci_3", "elective_2","gened_hum_2"],
        ["cs_tech_track_short_1", "elective_3", "elective_4", "elective_5", "gened_arts"],
        ["cs_tech_track_short_1", "gened_global_1", "elective_6", "elective_7", "gened_hum_3"],
        ["cs_tech_track_2113_1", "cs_tech_track_2113_2", "elective_8", "elective_9", "gened_global_1"],
        ["cs_tech_track_2113_3", "elective_10", "elective_11", "elective_12", "gened_hum_4"]
    ]
big_dict["semesters"] = semesters

with open("BA_2021-2022.json", "w") as fp: 
	json.dump(big_dict , fp) 