import json

# get the latest courses lists generated via bulletin_scraper.py
json_file = open("./all_courses.json") 
all_courses = set(json.loads(json_file.read()))
json_file.close()

json_file = open("./all_GPAC_courses.json") 
all_GPAC_courses = json.loads(json_file.read())
json_file.close()
#dict_keys(['Quantitative Reasoning in Mathematics or Statistics', 'Scientific Reasoning in Natural and/or Physical Lab Sciences', 'Critical Thinking in the Humanities', 'Critical Thinking, Quantitative Reasoning or Scientific Reasoning in the Social Sciences', 'Creative or Critical Thinking in the Arts', 'Global or Cross-Cultural Perspectives', 'Local/Civic Engagement', 'Oral Communication'])

json_file = open("./exceptions.json") 
exceptions = set(json.loads(json_file.read()))
json_file.close()

json_file = open("./cs_offerings.json") 
cs_offerings = set(json.loads(json_file.read()))
json_file.close()

def getFullNameFromNum(all_courses, manual):
	cleaned_manual = []
	for mini in manual:
		for course in all_courses:
			course_num = course.split("#")[0]
			if course_num in mini:
				cleaned_manual.append(course)
			elif "*" in mini:
				root = mini.split(" ")[0]
				if root in course:
					cleaned_manual.append(course)
	return cleaned_manual

possible_courses = {}


# CS courses ##################################################################################################
possible_courses["seas1001"] = getFullNameFromNum(all_courses, ["SEAS 1001"])
possible_courses["cs1010"] = getFullNameFromNum(all_courses, ["CSCI 1010"])

possible_courses["cs1111"] = getFullNameFromNum(all_courses, ["CSCI 1111"])
possible_courses["cs1112"] = getFullNameFromNum(all_courses, ["CSCI 1112"])
possible_courses["cs2113"] = getFullNameFromNum(all_courses, ["CSCI 2113"])
possible_courses["cs2312"] = getFullNameFromNum(all_courses, ["CSCI 2312"])
possible_courses["cs_architecture"] = getFullNameFromNum(all_courses, ["CSCI 3401", "CSCI 2461"])

possible_courses["cs1311"] = getFullNameFromNum(all_courses, ["CSCI 1311"])
possible_courses["cs2501"] = getFullNameFromNum(all_courses, ["CSCI 2501"])
possible_courses["cs2541W"] = getFullNameFromNum(all_courses, ["CSCI 2541W"])
possible_courses["cs3212"] = getFullNameFromNum(all_courses, ["CSCI 3212"])
possible_courses["cs3313"] = getFullNameFromNum(all_courses, ["CSCI 3313"])
possible_courses["cs3410"] = getFullNameFromNum(all_courses, ["CSCI 3410"])
possible_courses["cs3411"] = getFullNameFromNum(all_courses, ["CSCI 3411"])
possible_courses["cs4243W"] = getFullNameFromNum(all_courses, ["CSCI 4243W"])
possible_courses["cs4244"] = getFullNameFromNum(all_courses, ["CSCI 4244"])

# TODO: do we need to include the grad versions of all these courses for 5-year masters students?
possible_courses["cs_tech_track_2113_1"] = getFullNameFromNum(all_courses, ["CSCI 3462", "CSCI 4223", "CSCI 4235",  "CSCI 4431", "CSCI 4237", "CSCI 4331", "CSCI 4341", "CSCI 4342", "CSCI 4345", "CSCI 4364", "CSCI 4366", "CSCI 4415", "CSCI 4431", "CSCI 4431W", "CSCI 4454", "CSCI 4455", "CSCI 4511", "CSCI 4527", "CSCI 4531", "CSCI 4533", "CSCI 4541", "CSCI 4554", "CSCI 4561", "CSCI 4572", "CSCI 4577"])
possible_courses["cs_tech_track_2113_2"] = possible_courses["cs_tech_track_2113_1"]
possible_courses["cs_tech_track_core_1"] = getFullNameFromNum(all_courses, ["CSCI 6411", "CSCI 6421", "CSCI 4431", "CSCI 6431", "CSCI 4331", "CSCI 6331", "CSCI 4364", "CSCI 6364", "CSCS 8331", "CSCI 4366", "CSCI 4341", "CSCI 4527", "CSCI 6527", "CSCI 6351", "EMSE 6575", "CSCI 4554", "CSCI 4237", "CSCI 4533", "CSCI 4331", "CSCI 6331", "CSCI 8331"])
possible_courses["cs_tech_track_core_2"] = possible_courses["cs_tech_track_core_1"]

cs_tech_courses = possible_courses["cs1010"] + possible_courses["cs1111"] + possible_courses["cs1112"] + possible_courses["cs2113"] + possible_courses["cs2312"] + \
	possible_courses["cs_architecture"] + possible_courses["cs1311"] + possible_courses["cs2501"] + possible_courses["cs2541W"] + possible_courses["cs3212"] + \
	possible_courses["cs3313"] + possible_courses["cs3410"] + possible_courses["cs3411"] + possible_courses["cs_tech_track_2113_1"] + \
	possible_courses["cs_tech_track_core_2"]


# math courses ##################################################################################################

possible_courses["calc_1"] = getFullNameFromNum(all_courses, ["MATH 1231", "MATH 1221"])
possible_courses["calc_2"] = getFullNameFromNum(all_courses, ["MATH 1232"])
possible_courses["stats"] = getFullNameFromNum(all_courses, ["APSC 3115", "CSCI 3362", "CSCI 6362", "CSCI 4341", "STAT 4157"]) # why was "STAT 3157" in here by Kinga?
possible_courses["linear_alg"] = getFullNameFromNum(all_courses, ["MATH 2184", "CSCI 4342", "EMSE 2705"])

# university requirements ##################################################################################################

possible_courses["uw1020"] = getFullNameFromNum(all_courses, ["UW 1020", "HONR 1015"])
possible_courses["gened_ss_1"] = getFullNameFromNum(all_courses, all_GPAC_courses['Critical Thinking, Quantitative Reasoning or Scientific Reasoning in the Social Sciences'])
possible_courses["gened_ss_2"] = getFullNameFromNum(all_courses, all_GPAC_courses['Critical Thinking, Quantitative Reasoning or Scientific Reasoning in the Social Sciences'])
possible_courses["gened_hum"] = getFullNameFromNum(all_courses, all_GPAC_courses['Critical Thinking in the Humanities'])

# other requirements ##################################################################################################
possible_courses["sci_seq_1"] = getFullNameFromNum(all_courses, ["BISC 1111", "CHEM 1111", "PHYS 1021"])
possible_courses["sci_seq_2"] = getFullNameFromNum(all_courses, ["BISC 1112", "CHEM 1112", "PHYS 1022"])
possible_courses["sci_2"] = possible_courses["sci_seq_1"] + possible_courses["sci_seq_2"]

# the courses below were manually collected from this pdf: https://engineering.gwu.edu/sites/g/files/zaxdzs5436/files/downloads/SEAS%20Non-Technical%20Course%20List_0.pdf
manual_seas = ["AMST 1050", "AMST 1160", "AMST 1200", "AMST 2010", "AMST 2011", "AMST 2020", "AMST 2020W", "AMST 2120W ", "PSC 2120W", "AMST 2210", "AMST 2320", "AMST 2350", "AMST 2380", "AMST 2410", "AMST 2440", "AMST 2520", "AMST 2521", "AMST 2530", "AMST 2710", "AMST 2730", "AMST 2730W", "AMST 2750W", "AMST 3352", "AMST 3352W", "ANTH 2750", "ANTH 2750W", "AH *", "ARAB *", "CLAS *", "GREK *", "LATN *", "HEBR *", "PERS *", "TURK *", "YDSH *", "CHIN *", "KOR *", "JAPN *", "EALL 3811", "EALL 3814", "EALL 3814W", "EALL 3821", "EALL 3831", "EALL 3832", "ENGL *", "HIST *", "HONR 1016", "HONR 2016", "HONR 2053", "HONR 2053W", "HONR 2054", "SMPA 2110W", "SMPA 3230", "SMPA 3236W", "SMPA 3241W", "SMPA 3243W", "SMPA 3245", "SMPA 3246", "MUS 1103", "MUS 1104", "MUS 1107", "MUS 1108", "MUS 2101", "MUS 2102", "MUS 2109", "MUS 2110", "MUS 2111", "MUS 2121", "NSC 2126", "NSC 2180", "PSTD 1010", "NSC 4176", "PHIL *", "PSC 2120W", "SPAN *", "ITAL *", "FREN *", "PORT *", "GER *", "SLAV *", "REL *", "SLHS 1072", "SLHS 1081", "SLHS 1082", "TRDA 1015", "TRDA 1020", "TRDA 1025", "TRDA 3245", "TRDA 3246", "TRDA 2191", "WGSS 2380", "WGSS 3352", "WGSS 3353", "WGSS 3981", "WLP 1020", "AMST 2490", "AMST 2532", "AMST 3324", "AMST 3350", "ANTH 1002", "ANTH 1002W", "ANTH 1003", "ANTH 1004", "ANTH 2008", "ANTH 2008W", "ANTH 2502", "ANTH 2506", "ANTH 3501", "ANTH 3502", "ANTH 3503", "ANTH 3504", "ANTH 3505", "ANTH 3506", "ANTH 3507", "ANTH 3508", "ANTH 3509", "ANTH 3513", "ANTH 3522", "ANTH 3601", "ANTH 3602", "ANTH 3603", "ANTH 3701", "ANTH 3702", "ANTH 3703", "ANTH 3704", "ANTH 3705", "ANTH 3707", "ANTH 3708", "ANTH 3709", "ANTH 3801", "ANTH 3802", "ANTH 3803", "ANTH 3804", "ANTH 3806", "ANTH 3813", "ANTH 3814", "ANTH 3838", "ANTH 3838W", "COMM 1025", "COMM 1040", "COMM 1041", "ECON *", "GEOG 1001", "GEOG 1002", "GEOG 1003", "GEOG 2110", "GEOG 2127", "GEOG 2133", "GEOG 2134", "GEOG 2141", "GEOG 2144", "GEOG 2145", "GEOG 2146", "GEOG 3120", "GEOG 2120", "GEOG 3143", "GEOG 3154", "GEOG 3161", "GEOG 3164", "HSCI 2101", "HSCI 2103", "HLWL 1109", "HONR 2043", "HONR 2044", "HONR 2047", "HONR 2047W", "HONR 2048", "HMSR 2171", "HMSR 2172", "HMSR 2177", "IAFF 2090", "IAFF 2091", "IAFF 2092", "IAFF 2093", "MAE 2170", "SMPA 1050", "SMPA 2101", "SMPA 2102", "SMPA 2173", "SMPA 2177", "SMPA 3428", "SMPA 3470", "SMPA 3471", "SMPA 3472", "SMPA 3474", "SMPA 3476", "NSC 1051", "NSC 2160", "NSC 2175", "PSC *", "PSYC *", "SOC *", "SLHS 1071", "SLHS 1071W", "SLHS 1084", "SUST 1001", "TSTD 3001", "WGSS 1020", "WGSS 2120", "WGSS 2125"]
cleaned_manual_seas = getFullNameFromNum(all_courses, manual_seas)
possible_courses["seas_hss_1"] = cleaned_manual_seas
possible_courses["seas_hss_2"] = cleaned_manual_seas
possible_courses["seas_hss_3"] = cleaned_manual_seas

# go through and remove all the CS course numbers from all possible courses
# TODO: should we also remove math, stats, and linear algebra courses here because they are technical? 
# 		The requirement is as follows: "the content must meet a broad requirement that it not be closely related to the discipline of computing."
#		This is too nebulously defined in the bulletin, so I am choosing to only exclude CS courses from NTT since they are the discipline of computing.
# There are also a list of explicit exceptions for NTT courses in the bulletin, which I have included.
# The extremely nebulous and overly complicated, and often contradictory, Bulletin requirements for NTT are here: https://cs.engineering.gwu.edu/bachelor-science-non-technical-track-requirement
def setRemove(original, delete):
	new = []
	for long_course in original:
		course_num = long_course.split("#")[0]
		if course_num not in delete:
			new.append(long_course)
	return new

ntt = setRemove(all_courses, cs_tech_courses) # remove CS courses from NTT
ntt = setRemove(ntt, exceptions) # remove PCSC and PSIS courses from NTT

bulletin_exceptions = ["BADM 2301", "EMSE 4197", "ISTM 3119", "ISTM 4120", "ISTM 4121", "ISTM 4123", "STAT 1051", "STAT 1053", "STAT 1129"]
ntt = setRemove(ntt, bulletin_exceptions)

manually_chosen_exceptions = ["BME 2820", "BME 2825", "DNSC 4211", "ECE 1120", "EMSE 4571", "EMSE 4574", "GEOG 4308", "INFR 4103", "ISTM 3119"]
ntt = setRemove(ntt, manually_chosen_exceptions)

poorvi_exceptions = ["UW 1099", "ECON 1001"]
ntt = ntt = setRemove(ntt, poorvi_exceptions)

possible_courses["ntt_1"] = ntt
possible_courses["ntt_2"] = ntt
possible_courses["ntt_3"] = ntt

# electives are similar in requirements to NTT, but they do allow you to take additional CS courses (with some restrictions)
electives = []
for course in all_courses:
	if "CSCI" in course:
		for cs in cs_offerings: # add in any valid CS courses
			cs_name = cs.split("#")[0]
			cs_num = cs_name.split(" ")[1]
			if int(cs_num[:4]) > 2461 and "CSCI "+cs_num in course:
				electives.append(course)
	else:
		electives.append(course)

possible_courses["elective_1"] = electives
possible_courses["elective_2"] = electives
possible_courses["elective_3"] = electives
possible_courses["elective_4"] = electives

with open("possible_courses_2019_2020_2021.json", "w") as fp: 
	json.dump(possible_courses , fp) 