#use open command to access information in database: bayareahikes.csv
import csv

new_list = []

with open("bayareahikes.csv")as csvfile:
	my_file = csv.DictReader(csvfile)
	#convert csv into list, each element is a dictionary within list
	global new_list
	for row in my_file:
		new_list.append(row) 


	# print "So you want to go for a hike!  Great, let's see which hikes we can do!"

	# #ask user to search hikes by: 
	# print """Bay Area Regions:
	# 	1-San Francisco
	# 	2-North Bay 
	# 	3-East Bay
	# 	4-Peninsula and South Bay"""
region_select = "San Francisco" #raw_input("Please select the Bay Area region that you would like to hike: ")

def region_select(new_list, region_select):
	#creates new list of possible hikes in region
	region_specific_hikes = []
	for hike in new_list:
		if region_select == hike['Region'].strip():
			region_specific_hikes.append(hike)
	return region_specific_hikes

print region_select(new_list, 'San Francisco')
			#print all hikes in San Francisco
		


	#2-Hike duration (in hours)
	#how long do you want to hike?

	#3-Intensity level (Easy, Moderate, or Strenuous)
	#at what intensity level?

	#4-Hike length (in miles)
	#how many miles do you want to hike?

	#print full description(s) of narrowed list of hikes

	#5-Check weather of selected hike's location (city, state)
	#print "By the way, the weather at s% is currently s%. % (location, temperature)"