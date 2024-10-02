from BS_2019_2020_2021_courses import *

del possible_courses['cs2501']
possible_courses["ethics"] = getFullNameFromNum(all_courses, ["CSCI 2211", "PHIL 2135", "CSCI 4532", "CSCI 3532"]) #count the renamed version of ethics

possible_courses["linear_alg"] = getFullNameFromNum(all_courses, ["MATH 2184", "MATH 2185","CSCI 4342", "EMSE 2705"])

del possible_courses['cs_tech_track_2113_1']
del possible_courses['cs_tech_track_2113_2']
del possible_courses['cs_tech_track_core_1']
del possible_courses['cs_tech_track_core_2']
cs_tt = []
for course in all_courses:
	if "CSCI" in course:
		for cs in cs_offerings: # add in any valid CS courses
			cs_name = cs.split("#")[0]
			cs_num = cs_name.split(" ")[1]
			if int(cs_num[:4]) >= 4000 and "CSCI "+cs_num in course:
				cs_tt.append(course)
cs_tt = list(set(cs_tt))
possible_courses['cs_tech_track_4000_1'] = cs_tt
possible_courses['cs_tech_track_4000_2'] = cs_tt
possible_courses['cs_tech_track_4000_3'] = cs_tt

del possible_courses['ntt_1']
del possible_courses['ntt_2']
del possible_courses['ntt_3']
possible_courses["elective_5"] = electives
possible_courses["elective_6"] = electives
possible_courses["elective_7"] = electives
possible_courses["elective_8"] = electives

result = {"requirements": possible_courses}
with open("possible_courses_BS_2022_2023.json", "w") as fp: 
	json.dump(result , fp) 

big_dict = reformatForFrontEnd(possible_courses)
big_dict["degree"] = "BS 2022-2023"
semesters = [
        ["cs1010", "cs1111", "calc_1", "seas1001", "uw1020", "gened_ss_1"],
        ["cs1112", "cs1311", "calc_2", "sci_seq_1", "gened_ss_2"],
        ["cs2113", "cs2312", "cs3410", "sci_seq_2", "gened_hum"],
        ["cs_architecture", "cs2541W", "cs3313", "ethics","stats"],
        ["cs3212", "cs3411", "cs_tech_track_4000_1", "seas_hss_1"],
        ["cs_tech_track_4000_2","elective_1", "linear_alg", "elective_2", "seas_hss_2"],
        ["cs4243W", "cs_tech_track_4000_3", "elective_3", "elective_4", "seas_hss_3"],
        ["cs4244","elective_5", "elective_6", "elective_7", "elective_8"]
    ]
big_dict["semesters"] = semesters
with open("BS_2022-2023.json", "w") as fp: 
	json.dump(big_dict , fp) 

big_dict["degree"] = "BS 2023-2024"
with open("BS_2023-2024.json", "w") as fp: 
	json.dump(big_dict , fp) 