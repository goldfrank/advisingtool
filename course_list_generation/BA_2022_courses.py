import json

# get everything that is shared with the previous version
from BA_2021_courses import *

del possible_courses["sci_3"]

possible_courses["stats"].append("DNSC 1001")

possible_courses["cs3212"] = getFullNameFromNum(all_courses, ["CSCI 3212"])

del possible_courses["cs_tech_track_2113_1"] 
del possible_courses["cs_tech_track_2113_2"]
del possible_courses["cs_tech_track_2113_3"] 
del possible_courses["cs_tech_track_short_1"]
del possible_courses["cs_tech_track_short_2"]

# from the bulletin: "All students in the BA in computer science program are required to take four technical courses (for a minimum of 12 credits) of 
# computer science courses numbered 2400 and above. Of these courses, at least two (for a minimum of 6 credits) must be at the 4000 level or above. 
# CSCI 4243, CSCI 4243W, CSCI 4244 may not be used toward the advanced CS elective requirement."
cs_tech_track_2000 = ["CSCI 2410", "CSCI 3212", "CSCI 3313", "CSCI 3362" "CSCI 3401", "CSCI 3410", "CSCI 3411", "CSCI 3462", "CSCI 3532", "CSCI 3551", "CSCI 3552", "CSCI 3571", "CSCI 3907", "CSCI 3908", "CSCI 4223", "CSCI 4235", "CSCI 4237", "CSCI 4331", "CSCI 4341", "CSCI 4342", "CSCI 4345", "CSCI 4364", "CSCI 4366", "CSCI 4414", "CSCI 4415", "CSCI 4417", "CSCI 4418", "CSCI 4431", "CSCI 4431W", "CSCI 4454", "CSCI 4455", "CSCI 4511", "CSCI 4521", "CSCI 4525", "CSCI 4527", "CSCI 4531", "CSCI 4532", "CSCI 4533", "CSCI 4541", "CSCI 4551", "CSCI 4552", "CSCI 4553", "CSCI 4554", "CSCI 4561", "CSCI 4572", "CSCI 4577", "CSCI 4907"]
cs_tech_track_4000 = ["CSCI 4223", "CSCI 4235", "CSCI 4237", "CSCI 4331", "CSCI 4341", "CSCI 4342", "CSCI 4345", "CSCI 4364", "CSCI 4366", "CSCI 4414", "CSCI 4415", "CSCI 4417", "CSCI 4418", "CSCI 4431", "CSCI 4431W", "CSCI 4454", "CSCI 4455", "CSCI 4511", "CSCI 4521", "CSCI 4525", "CSCI 4527", "CSCI 4531", "CSCI 4532", "CSCI 4533", "CSCI 4541", "CSCI 4551", "CSCI 4552", "CSCI 4553", "CSCI 4554", "CSCI 4561", "CSCI 4572", "CSCI 4577", "CSCI 4907"]
possible_courses["cs_tech_track_2000_1"] = getFullNameFromNum(all_courses, cs_tech_track_2000)
possible_courses["cs_tech_track_2000_2"] = possible_courses["cs_tech_track_2000_1"]
possible_courses["cs_tech_track_4000_1"] = getFullNameFromNum(all_courses, cs_tech_track_4000)
possible_courses["cs_tech_track_4000_2"] = possible_courses["cs_tech_track_4000_1"]

# in this year any CS course above 2400 (not just about 2461) counts as an elective
# but here they restirct to only 2 CS electives, the rest are other major/minor so we have to regenerate what it means to be an elective

del possible_courses["elective_1"]
del possible_courses["elective_2"]
del possible_courses["elective_3"]
del possible_courses["elective_4"]
del possible_courses["elective_5"]
del possible_courses["elective_6"]
del possible_courses["elective_7"]
del possible_courses["elective_8"]
del possible_courses["elective_9"]
del possible_courses["elective_10"]
del possible_courses["elective_11"]
del possible_courses["elective_12"]

# add in a few more allowed CS electives for this 2022 year
BA_2022_cs_allowed_electives = electives.copy()
for course in cs_tech_courses:
	cs_name = course.split("#")[0]
	cs_num = cs_name.split(" ")[1]
	if int(cs_num[:4]) > 2400 and int(cs_num[:4]) <= 2461:
		BA_2022_cs_allowed_electives.append(course)

possible_courses["elective_1_CS_okay"] = BA_2022_cs_allowed_electives
possible_courses["elective_2_CS_okay"] = BA_2022_cs_allowed_electives
possible_courses["elective_1_ntt"] = ntt
possible_courses["elective_2_ntt"] = ntt
possible_courses["elective_3_ntt"] = ntt
possible_courses["elective_4_ntt"] = ntt
possible_courses["elective_5_ntt"] = ntt
possible_courses["elective_6_ntt"] = ntt
possible_courses["elective_7_ntt"] = ntt
possible_courses["elective_8_ntt"] = ntt
possible_courses["elective_9_ntt"] = ntt
possible_courses["elective_10_ntt"] = ntt
possible_courses["elective_11_ntt"] = ntt

result = {"requirements": possible_courses}
with open("possible_courses_BA_2022.json", "w") as fp: 
	json.dump(result , fp) 