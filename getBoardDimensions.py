import json

with open("CarnivalSetup.json") as file:
    data = json.load(file)

print(data["Board"]["Height"])
print(data["Board"]["Width"])