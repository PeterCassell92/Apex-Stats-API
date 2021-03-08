import requests
import json

APIKey_file = open("Apex.txt", "rt")
APIKey = APIKey_file.read()

all_legend_names = ["Bloodhound", "Gibraltar", "Lifeline", "Pathfinder", "Wraith", "Bangalore", "Caustic", "Mirage", 
"Octane", "Wattson", "Crypto", "Revenant", "Loba", "Rampart", "Horizon", "Fuse"]

url = 'https://public-api.tracker.gg/v2/apex/standard/profile/origin/'

player_name = 'majorquazar'

segment_type = 'legend'

full_url = url + player_name + "/segments" + "/" + segment_type

payload = {}

headers = {'TRN-Api-Key': APIKey}

response = requests.request("GET", full_url, headers=headers, data=payload)

player_data = response.json()

API_legend_name = []

killdata = list();

for legend in all_legend_names:
	kills = 0;
	for item in player_data["data"]:
		if item.get("metadata").get("name") == legend:
			if item.get("stats") and item.get("stats").get("kills") and item.get("stats").get("kills").get("value"):
				kills = item["stats"]["kills"]["value"];
	print(str(kills) + " kills with " + legend);
	killdata.append({"name": legend, "kills": kills});
	pass;

#print(killdata);