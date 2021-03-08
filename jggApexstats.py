import requests
import json
from legend import Legend

#process the trackergg API
def processTrackerGGLegendData(o, all_legend_names):
	legend_data = list()
	#process reponse data
	for legend in all_legend_names:
		#set default kills to 0
		kills = 0;
		for item in o["data"]:
			#if legend name matches a player data legend name then attempt to get kill data
			if item.get("metadata").get("name") == legend:
				#if kill data is available then set value of kills
				if item.get("stats") and item.get("stats").get("kills") and item.get("stats").get("kills").get("value"):
					kills = int(item["stats"]["kills"]["value"])
		#initialise Legend object for each legend using name and kills as parameters.
		legend_data.append(Legend(legend, kills))
		pass

	return legend_data

#process the Mozambiquehere API
def processMozHereLegendData(o, all_legend_names):
	legend_data = list()

	print(json.dumps(o))
	return legend_data

all_legend_names = ["Bloodhound", "Gibraltar", "Lifeline", "Pathfinder", "Wraith", "Bangalore", "Caustic", "Mirage", 
"Octane", "Wattson", "Crypto", "Revenant", "Loba", "Rampart", "Horizon", "Fuse"]

legend_data = None

#setup
#select which API service to use
x= "GG"
#select a player name
player_name = "MajorQuazar"
if x == "GG":
	filename = "trackerggAPIKey.txt"
	APIKey_file = open(filename, "rt")
	APIKey = APIKey_file.read()
	segment_type = "legend"
	url = "https://public-api.tracker.gg/v2/apex/standard/profile/origin/" + player_name + "/segments/" + segment_type
	payload = {}
	headers = {'TRN-Api-Key': APIKey}
	#HTTP request to selected api
	response = requests.request("GET", url, headers=headers, data=payload)
	legend_data = processTrackerGGLegendData(response.json(), all_legend_names)

elif x == "MOZ":
	filename = "mozhereAPIKey.txt"
	APIKey_file = open(filename, "rt")
	APIKey = APIKey_file.read()
	print(APIKey)
	url = "https://api.mozambiquehe.re/bridge?platform=PC&uid=" + player_name + "&auth=" + APIKey
	payload = {}
	headers = {}

	#HTTP request to selected api
	response = requests.request("GET", url, headers=headers, data=payload)
	print(response)
	legend_data = processMozHereLegendData(response.json(), all_legend_names)

#end setup

#if legend data was retrieved then display it
if(legend_data):
	#sort based by kill count (descending)
	legend_data.sort(key= lambda x: x.getKills(), reverse = True)
	#print name with formatting
	print("-----\r" + player_name + "\r-----")
	#print all legend data
	for legend in legend_data:
		print(str(legend.getKills()) + " kills with " + legend.getName())
else:
	print("Legend Data Not Retrieved")
