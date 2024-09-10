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

def setRemove(original, delete):
	new = []
	for long_course in original:
		course_num = long_course.split("#")[0]
		if course_num not in delete:
			new.append(long_course)
		else:
			print("deleted " + long_course)
	return new

electives = setRemove(all_courses, exceptions) # remove PCSC and PSIS courses from electives

bulletin_exceptions = ["BADM 2301", "EMSE 4197", "ISTM 3119", "ISTM 4120", "ISTM 4121", "ISTM 4123", "STAT 1051", "STAT 1053", "STAT 1129"]
electives = setRemove(electives, bulletin_exceptions)

manually_chosen_exceptions = ["BME 2820", "BME 2825", "DNSC 4211", "ECE 1120", "EMSE 4571", "EMSE 4574", "GEOG 4308", "INFR 4103", "ISTM 3119"]
electives = setRemove(electives, manually_chosen_exceptions)

poorvi_exceptions = ["ECON 1001"] # "UW 1099" 
electives = setRemove(electives, poorvi_exceptions)

# electives are similar in requirements to NTT, but they do allow you to take additional CS courses (with some restrictions)
cs_tech_courses = []
for course in all_courses:
	if "CSCI" in course:
		cs_tech_courses.append(course) # grab these for later
		cs_name = course.split("#")[0]
		cs_num = cs_name.split(" ")[1]
		if int(cs_num[:4]) > 2461:
			electives.append(course)
		else:
			electives.remove(course)

# go through and remove all the CS course numbers from all possible courses
# TODO: should we also remove math, stats, and linear algebra courses here because they are technical? 
# 		The requirement is as follows: "the content must meet a broad requirement that it not be closely related to the discipline of computing."
#		This is too nebulously defined in the bulletin, so I am choosing to only exclude CS courses from NTT since they are the discipline of computing.
# There are also a list of explicit exceptions for NTT courses in the bulletin, which I have included.
# The extremely nebulous and overly complicated, and often contradictory, Bulletin requirements for NTT are here: https://cs.engineering.gwu.edu/bachelor-science-non-technical-track-requirement
ntt = list(set(electives) - set(cs_tech_courses)) # remove CS courses from electives
# courses common to all CS degrees ############################################################################################

possible_courses = {}
possible_courses["seas1001"] = getFullNameFromNum(all_courses, ["SEAS 1001"])
possible_courses["cs1010"] = getFullNameFromNum(all_courses, ["CSCI 1010"])

possible_courses["cs1111"] = getFullNameFromNum(all_courses, ["CSCI 1111"])
possible_courses["cs1112"] = getFullNameFromNum(all_courses, ["CSCI 1112"])
possible_courses["cs2113"] = getFullNameFromNum(all_courses, ["CSCI 2113"])
possible_courses["cs_architecture"] = getFullNameFromNum(all_courses, ["CSCI 3401", "CSCI 2461"])
possible_courses["cs1311"] = getFullNameFromNum(all_courses, ["CSCI 1311"])

# TODO: do we need to include the grad versions of all these courses for 5-year masters students?
cs_tt_2113_prereq = ["CSCI 3462", "CSCI 4223", "CSCI 4235",  "CSCI 4431", "CSCI 4237", "CSCI 4331", "CSCI 4341", "CSCI 4342", "CSCI 4345", "CSCI 4364", "CSCI 4366", "CSCI 4415", "CSCI 4431", "CSCI 4431W", "CSCI 4454", "CSCI 4455", "CSCI 4511", "CSCI 4527", "CSCI 4531", "CSCI 4533", "CSCI 4541", "CSCI 4554", "CSCI 4561", "CSCI 4572", "CSCI 4577"]

possible_courses["calc_1"] = getFullNameFromNum(all_courses, ["MATH 1231", "MATH 1221"])
possible_courses["calc_2"] = getFullNameFromNum(all_courses, ["MATH 1232"])

possible_courses["uw1020"] = getFullNameFromNum(all_courses, ["UW 1020", "HONR 1015"])

# takes Kinga's format and converts it so something Joe's front end plays nicely with
def reformatForFrontEnd(possible_courses):
	dictionary = {"requirements":[]}
	for k in possible_courses.keys():
		req = {"req":k}
		req["courses"] = []
		for course in possible_courses[k]:
			course_num = course.split("#")[0]
			course_desc = course.split("#")[1]
			course_dict = {"id":k,"text":course_num+" "+course_desc,"num":course_num,"desc":course_desc}
			req["courses"].append(course_dict)
		dictionary["requirements"].append(req)
	#print(dictionary)
	return dictionary