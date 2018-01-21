# CAA14 Productions 2015
# Created 06/24/2015

#	A program to randomize Mount and Blade: War Band Napoleonic Wars maps.
#	It overwrites the following .txt M&B command files in the commandline argument server directory:
# - random_map_reg_NW.txt: Sets and adds all regular maps.
# - random_map_cb_NW.txt: Sets and adds all large random maps.
# - random_map_sieg_NW.txt: Sets and adds all siege maps.
# - random_map_conq_NW.txt: Sets and adds all conquest maps.

# CommandLine Usage:
# 	python randomizeThoseMaps.py <server_dir>

# NOTE: If no second argument is provided, it is assumed the server is in the same directory as randomizeThoseMaps_NW.py

import sys
import random
from sys import argv

if (len(argv) < 2):
	print "Getting server directory from local..."
	regPath = "random_map_reg_NW.txt"
	cbPath = "random_map_cb_NW.txt"
	siegPath = "random_map_sieg_NW.txt"
	conqPath = "random_map_conq_NW.txt"
else:
	regPath = argv[1] + "random_map_reg_NW.txt"
	cbPath = argv[1] + "random_map_cb_NW.txt"
	siegPath = argv[1] + "random_map_sieg_NW.txt"
	conqPath = argv[1] + "random_map_conq_NW.txt"


regMaps = [
		  "mp_ambush",
		  "mp_ambush_fog",
		  "mp_arabian_harbour",
		  "mp_arabian_harbour_night",
		  "mp_arabian_village",
		  "mp_arabian_village_morning",
		  "mp_ardennes",
		  "mp_ardennes_morning",
		  "mp_avignon",
		  "mp_avignon_morning",
		  "mp_bavarian_river",
		  "mp_bavarian_river_cloudy",
		  "mp_beach",
		  "mp_beach_morning",
		  "mp_borodino",
		  "mp_borodino_morn",
		  "mp_champs_elysees",
		  "mp_champs_elysees_rain",
		  "mp_charge_to_the_rhine",
		  "mp_charge_to_the_rhine_cloudy",
		  "mp_citadelle_napoleon",
		  "mp_citadelle_napoleon_morning",
		  "mp_columbia_farm_morning",
		  "mp_columbia_hill_farm",
		  "mp_countryside",
		  "mp_countryside_fog",
		  "mp_dust",
		  "mp_dust_morning",
		  "mp_european_city_summer",
		  "mp_european_city_winter",
		  "mp_floodplain",
		  "mp_floodplain_storm",
		  "mp_forest_pallisade",
		  "mp_forest_pallisade_fog",
		  "mp_french_farm",
		  "mp_french_farm_storm",
		  "mp_german_village",
		  "mp_german_village_rain",
		  "mp_hougoumont",
		  "mp_hougoumont_night",
		  "mp_hungarian_plains",
		  "mp_hungarian_plains_cloud",
		  "mp_la_haye_sainte",
		  "mp_la_haye_sainte_night",
		  "mp_landshut",
		  "mp_landshut_night",
		  "mp_minden",
		  "mp_minden_night",
		  "mp_naval",
		  "mp_oaksfield_day",
		  "mp_oaksfield_storm",
		  "mp_outlaws_den",
		  "mp_outlaws_den_night",
		  "mp_quatre_bras",
		  "mp_quatre_bras_night",
		  "mp_river_crossing",
		  "mp_river_crossing_morning",
		  "mp_roxburgh",
		  "mp_roxburgh_raining",
		  "mp_russian_river_cloudy",
		  "mp_russian_river_day",
		  "mp_russian_village",
		  "mp_russian_village_fog",
		  "mp_saints_isle",
		  "mp_saints_isle_rain",
		  "mp_schemmerbach",
		  "mp_schemmerbach_storm",
		  "mp_siege_of_toulon",
		  "mp_siege_of_toulon_night",
		  "mp_sjotofta",
		  "mp_sjotofta_night",
		  "mp_slovenian_village",
		  "mp_slovenian_village_raining",
		  "mp_spanish_farm",
		  "mp_spanish_farm_rain",
		  "mp_spanish_mountain_pass",
		  "mp_spanish_mountain_pass_evening",
		  "mp_spanish_village",
		  "mp_spanish_village_evening",
		  "mp_strangefields",
		  "mp_strangefields_storm",
		  "mp_swamp",
		  "mp_theisland",
		  "mp_venice",
		  "mp_venice_morning",
		  "mp_walloon_farm",
		  "mp_walloon_farm_night"
		 ]

cbMaps = [
		  "random_multi_desert_forest_large",
		  "random_multi_desert_forest_medium",
		  "random_multi_desert_large",
		  "random_multi_desert_medium",
		  "random_multi_forest_large",
		  "random_multi_forest_large_rain",
		  "random_multi_forest_medium",
		  "random_multi_forest_medium_rain",
		  "random_multi_plain_large",
		  "random_multi_plain_large_rain",
		  "random_multi_plain_medium",
		  "random_multi_plain_medium_rain",
		  "random_multi_snow_forest_large",
		  "random_multi_snow_forest_large_snow",
		  "random_multi_snow_forest_medium",
		  "random_multi_snow_forest_medium_snow",
		  "random_multi_snow_large",
		  "random_multi_snow_large_snow",
		  "random_multi_snow_medium",
		  "random_multi_snow_medium_snow",
		  "random_multi_steppe_forest_large",
		  "random_multi_steppe_forest_medium",
		  "random_multi_steppe_large",
		  "random_multi_steppe_medium"
		 ]

siegMaps = [
			"mp_fort_al_hafya",
			"mp_fort_al_hafya_night",
			"mp_fort_bashir",
			"mp_fort_bashir_morning",
			"mp_fort_beaver",
			"mp_fort_beaver_morning",
			"mp_fort_boyd",
			"mp_fort_boyd_raining",
			"mp_fort_brochet",
			"mp_fort_brochet_raining",
			"mp_fort_de_chartres",
			"mp_fort_de_chartres_raining",
			"mp_fort_fleetwood",
			"mp_fort_fleetwood_storm",
			"mp_fort_george",
			"mp_fort_george_raining",
			"mp_fort_hohenfels",
			"mp_fort_hohenfels_night",
			"mp_fort_lyon",
			"mp_fort_lyon_night",
			"mp_fort_mackinaw",
			"mp_fort_mackinaw_raining",
			"mp_fort_nylas",
			"mp_fort_nylas_raining",
			"mp_fort_refleax",
			"mp_fort_refleax_night",
			"mp_fort_vincey",
			"mp_fort_vincey_storm"
		   ]

conqMaps = [
			"mp_russian_village_conq_night",
			"mp_arabian_village_conq",
			"mp_russian_village_conq",
			"mp_arabian_village_conq_morning"
		   ]
		 
		 
		 
# Open files
reg = open(regPath, "w", 0)
cb = open(cbPath, "w", 0)
sieg = open(siegPath, "w", 0)
conq = open(conqPath, "w", 0)


# Logic:

random.shuffle(regMaps)
reg.write("set_map " + regMaps[0] + "\n")
del regMaps[0]
for map in regMaps:
	reg.write("add_map " + map + "\n")


random.shuffle(cbMaps)
cb.write("set_map " + cbMaps[0] + "\n")
del cbMaps[0]
for map in cbMaps:
	cb.write("add_map " + map + "\n")


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
cb.close()
sieg.close()
conq.close()

print "Completed;\nThank you for using randomizeThoseMaps by Night_Blader"






