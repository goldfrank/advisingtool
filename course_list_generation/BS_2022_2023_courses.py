from BS_2019_2020_2021_courses import *

del possible_courses['cs2501']
possible_courses["ethics"] = getFullNameFromNum(all_courses, ["CSCI 2211", "PHIL 2135", "CSCI 4532"])

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

with open("possible_courses_2022_2023.json", "w") as fp: 
	json.dump(possible_courses , fp) 