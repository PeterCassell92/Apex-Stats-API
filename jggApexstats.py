import requests
import json

class Legend:
	def __init__(self, name, kills):
		self.name = name
		self.kills = kills
	def getKills(self):
		return self.kills
	def getName(self):
		return self.name

def getLegendKills(legend):
	return legend.getKills()

#setup
APIKey_file = open("Apex.txt", "rt")
APIKey = APIKey_file.read()

all_legend_names = ["Bloodhound", "Gibraltar", "Lifeline", "Pathfinder", "Wraith", "Bangalore", "Caustic", "Mirage", 
"Octane", "Wattson", "Crypto", "Revenant", "Loba", "Rampart", "Horizon", "Fuse"]

url = 'https://public-api.tracker.gg/v2/apex/standard/profile/origin/'

player_name = 'MajorQuazar'

segment_type = 'legend'

full_url = url + player_name + "/segments" + "/" + segment_type

payload = {}

headers = {'TRN-Api-Key': APIKey}

legend_data = list();

#end setup


#HTTP request to tracker.gg api
response = requests.request("GET", full_url, headers=headers, data=payload)
player_data = response.json()
#process reponse data
for legend in all_legend_names:
	#set default kills to 0
	kills = 0;
	for item in player_data["data"]:
		#if legend name matches a player data legend name then try to get kill data
		if item.get("metadata").get("name") == legend:
			#if kill data is available then set value of kills
			if item.get("stats") and item.get("stats").get("kills") and item.get("stats").get("kills").get("value"):
				kills = int(item["stats"]["kills"]["value"])
	#initialise Legend object for each legend using name and kills as parameters.
	legend_data.append(Legend(legend, kills))
	pass

#sort based by kill count (descending)
legend_data.sort(key= getLegendKills, reverse = True)
#print name with formatting
print("-----\r" + player_name + "\r-----")
#print all legend data
for legend in legend_data:
	print(str(legend.getKills()) + " kills with " + legend.getName())
