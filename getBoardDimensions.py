import json

with open("CarnivalSetup.json") as file:
    data = json.load(file)

print(data["Board"]["height"])
print(data["Board"]["width"])
print(data["Attractions"][0]["name"])