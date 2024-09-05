import json

# get everything that is shared with the previous version
from BA_2022_courses import *

del possible_courses["calc_2"]
possible_courses["elective_12_ntt"] = ntt

with open("possible_courses_BA_2023.json", "w") as fp: 
	json.dump(possible_courses , fp) 