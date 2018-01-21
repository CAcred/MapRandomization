# CAA14 Productions 2015
# Created 06/24/2015

#	A program to randomize Mount and Blade: War Band Native multi-player maps.
#	It overwrites the following .txt M&B command files in the commandline argument server directory:
# - random_map_reg_Native.txt: Sets and adds all regular maps.
# - random_map_sieg_Native.txt: Sets and adds all siege maps.
# - random_map_conq_Native.txt: Sets and adds all conquest maps.

# CommandLine Usage:
# 	python randomizeThoseMaps.py <server_dir>

# NOTE: If no second argument is provided, it is assumed the server is in the same directory as randomizeThoseMaps_Native.py

import sys
import random
from sys import argv

if (len(argv) < 2):
	print "Getting server directory from local..."
	regPath = "random_map_reg_Native.txt"
	siegPath = "random_map_sieg_Native.txt"
	conqPath = "random_map_conq_Native.txt"
else:
	regPath = argv[1] + "random_map_reg_Native.txt"
	siegPath = argv[1] + "random_map_sieg_Native.txt"
	conqPath = argv[1] + "random_map_conq_Native.txt"


regMaps = [
		  "multi_scene_1",
		  "multi_scene_2",
		  "multi_scene_4",
		  "multi_scene_7",
		  "multi_scene_9",
		  "multi_scene_11",
		  "multi_scene_12",
		  "random_multi_plain_medium",
		  "random_multi_plain_large",
		  "random_multi_steppe_medium",
		  "random_multi_steppe_large"
		 ]

siegMaps = [
			"multi_scene_3",
			"multi_scene_8",
			"multi_scene_10"
		   ]

conqMaps = [
			"multi_scene_1",
			"multi_scene_2",
			"multi_scene_4",
			"multi_scene_11",
			"multi_scene_12",
			"random_multi_plain_medium",
			"random_multi_plain_large",
			"random_multi_steppe_medium",
			"random_multi_steppe_large"
		   ]
		 
		 
		 
# Open files
reg = open(regPath, "w", 0)
sieg = open(siegPath, "w", 0)
conq = open(conqPath, "w", 0)


# Logic:

random.shuffle(regMaps)
reg.write("set_map " + regMaps[0] + "\n")
del regMaps[0]
for map in regMaps:
	reg.write("add_map " + map + "\n")


random.shuffle(siegMaps)
sieg.write("set_map " + siegMaps[0] + "\n")
del siegMaps[0]
for map in siegMaps:
	sieg.write("add_map " + map + "\n")


random.shuffle(conqMaps)
conq.write("set_map " + conqMaps[0] + "\n")
del conqMaps[0]
for map in conqMaps:
	conq.write("add_map " + map + "\n")



# Close files:
reg.close()
sieg.close()
conq.close()

print "Completed;\nThank you for using randomizeThoseMaps by Night_Blader"






