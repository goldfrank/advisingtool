from BS_2022_2023_courses import *


possible_courses["ethics"] = getFullNameFromNum(all_courses, ["CSCI 2211", "PHIL 2135", "CSCI 4532", "CSCI 3532", "ANTH 3625"])

del possible_courses["seas_hss_1"]
del possible_courses["seas_hss_2"]
del possible_courses["seas_hss_3"]

long_gpac = all_GPAC_courses['Critical Thinking in the Humanities'] + all_GPAC_courses['Critical Thinking, Quantitative Reasoning or Scientific Reasoning in the Social Sciences'] + \
			all_GPAC_courses['Creative or Critical Thinking in the Arts'] + all_GPAC_courses['Global or Cross-Cultural Perspectives'] + \
			all_GPAC_courses['Local/Civic Engagement'] + all_GPAC_courses['Oral Communication']
long_gpac_cleaned = getFullNameFromNum(all_courses, long_gpac)
possible_courses["gpac_1"] = long_gpac_cleaned
possible_courses["gpac_2"] = long_gpac_cleaned
possible_courses["gpac_3"] = long_gpac_cleaned

result = {"requirements": possible_courses}
with open("possible_courses_BS_2024.json", "w") as fp: 
	json.dump(result , fp) 

big_dict = reformatForFrontEnd(possible_courses)
big_dict["degree"] = "BS 2024-2025"
semesters = [
        ["cs1010", "cs1111", "calc_1", "seas1001", "uw1020", "gened_ss_1"],
        ["cs1112", "cs1311", "calc_2", "sci_seq_1", "gened_ss_2"],
        ["cs2113", "cs2312", "cs3410", "sci_seq_2", "gened_hum"],
        ["cs_architecture", "cs2541W", "cs3313", "ethics","stats"],
        ["cs3212", "cs3411", "cs_tech_track_4000_1", "gpac_1"],
        ["cs_tech_track_4000_2","elective_1", "linear_alg", "elective_2", "gpac_2"],
        ["cs4243W", "cs_tech_track_4000_3", "elective_3", "elective_4", "gpac_3"],
        ["cs4244","elective_5", "elective_6", "elective_7", "elective_8"]
    ]
big_dict["semesters"] = semesters
with open("BS_2024-2025.json", "w") as fp: 
	json.dump(big_dict , fp) 