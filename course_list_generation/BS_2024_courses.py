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