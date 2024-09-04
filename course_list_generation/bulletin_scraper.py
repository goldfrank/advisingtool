# This file downloads agents' MSWL webpage links, and their contents, for the current calendar year.

# These websites above are the source of all the topic modeling we have for agents in this paper.

# It is very slow to run due to a 1s delay we added between attempts to download each URL.

# need to try other pages on MSWL for the same agent bcause different data exists on
# https://mswishlist.com/agent/BookySaul
# vs
# https://www.manuscriptwishlist.com/mswl-post/abby-saul/

import subprocess
import requests
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, HTTPError
from time import sleep

# converts a sequence of characters in an html file to a list of strings
def convert_html_to_lines(raw):
	lines = []
	string = ""
	for char in raw:
		if char != '\n':
			string += str(char)
		else:
			lines.append(string)
			string = ""
	return lines

# downloads the HTML at a specific URL
def get_url_data(url = ""):
	try:
		request = Request(url, headers = {'User-Agent' :\
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"})
		#print(request)
		response = urlopen(request)
		data = response.read().decode("utf8", errors='ignore')
		return data
	except HTTPError as e:
		print(url)
		print(e)
		return str(e)

# extracts the texts elements from a HTML file at a specific URL using BeautifulSoup
def extract_text(url):
	html = get_url_data(url)
	soup = BeautifulSoup(html, features="html.parser")

	# kill all script and style elements
	for script in soup(["script", "style"]):
		script.extract()	# rip it out

	# get text
	text = soup.get_text()
	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)

	#print(text)
	return text


def generateBulletinLinks():

	majors = []
	all_courses = []
	exceptions = []
	cs_offerings = []

	webpage = convert_html_to_lines(get_url_data("https://bulletin.gwu.edu/courses/"))
	for line in webpage:
		#print(line)
		if "<ul><li><a href=\"/courses/" in line: 
			pieces = line.split('<li><a href="/courses/')
			for major in pieces:
				major = major.split('/')[0]
				if '<ul>' not in major:
					print(major)
					majors.append(major)

	for major in majors:
		major_webpage = convert_html_to_lines(get_url_data("https://bulletin.gwu.edu/courses/" + major + "/"))
		for line in major_webpage:
			if '<p class="courseblocktitle"><strong>' in line:
				pieces = line.split('<p class="courseblocktitle"><strong>')[1].split('.</strong></p>')[0].split(".")
				course_num = pieces[0].strip().replace(" ", " ")
				course_name = pieces[1].strip().replace(" ", " ")
				course_credits = pieces[2].strip().replace(" ", " ")
				if "UW 1020" in course_name: # check if any course happens to satisfy this requirement also, like HONR 1015
					print(course_num)
					print(course_name)
					print(course_credits)

				if "PSIS" in course_num or "PSCS" in course_num:
					print("adding " + course_name + " as NTT/elective exception due to overlap")
					exceptions.append(course_num+"#"+course_name)
				elif "programming" in course_name.lower():
					print("consider manually excluding " + course_num + " " + course_name + " as NTT/elective exception due to overlap")
					exceptions.append(course_num+"#"+course_name)

				if "CSCI" in course_num:
					cs_offerings.append(course_num+"#"+course_name)

				all_courses.append(course_num+"#"+course_name)

	with open("all_courses.json", "w") as fp: 
		json.dump(all_courses , fp) 
	with open("exceptions.json", "w") as fp: 
		json.dump(exceptions , fp) 
	with open("cs_offerings.json", "w") as fp: 
		json.dump(cs_offerings , fp) 

def generateGPACLinks():

	flavors = {}
	webpage = convert_html_to_lines(get_url_data("https://advising.columbian.gwu.edu/gpac-course-list"))
	for line in webpage:
		#print(line)
		if "<dt>" in line: 
			flavor = line.split('<dt>')[1].split("</dt>")[0]
			flavors[flavor] = []
		else:
			if 'a href="http://bulletin.gwu.edu/search/?P=' in line:
				course = line.split('a href="http://bulletin.gwu.edu/search/?P=')[1].split('"')[0].replace('+', ' ').upper()

				# GPAC website has bugs because of course they do...
				if course == "HIST%202520":
					course = "HIST 2520"

				print(flavor + " " +course)
				flavors[flavor].append(course)

	with open("all_GPAC_courses.json", "w") as fp: 
		json.dump(flavors , fp) 

if __name__ == '__main__':
	print("grabbing all courses in bulletin.................................")
	generateBulletinLinks()

	print("grabbing all courses in GPAC lists.................................")
	generateGPACLinks()


