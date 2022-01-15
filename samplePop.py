from CarnivalObject import CarnivalObject
from random import randint
import json

w, h = 10 ,10
tempMatrix = [[0 for x in range(w)] for y in range(h)]

# Making every block a path
# This ensures our
for row in range(0, 10):
    for coloms in range(0, 10):
        tempMatrix[row][coloms] = CarnivalObject("path", "#964B00")

# Reading objects from JSON File
with open("CarnivalSetup.json") as file:
    data = json.load(file)

# Placing Objects
for attractionNum in range(0, len(data["Attractions"])):
    print("\n attractionNum: {}".format(attractionNum))
    print(data["Attractions"][attractionNum]["name"])
    
    canInsert = False
    while (not canInsert):
        print("run Loop")
        rowValue = randint(0, 9)
        colomValue = randint(0, 9)
        print("rowValue: {}".format(rowValue))
        print("colomValue: {}".format(colomValue))
        
        
        objectHeight = data["Attractions"][attractionNum]["height"]
        objectWidth = data["Attractions"][attractionNum]["width"]
        
        canInsert = True
        if((rowValue + objectHeight <= 9) and (colomValue + objectWidth <= 9)):
            for h in range(0, objectHeight):
                for w in range(0, objectWidth):
                    if ((tempMatrix[rowValue + h][colomValue + w].getObjectName() != "path")):
                        canInsert = False          
        else:
            canInsert = False

        if (canInsert == True):
            print("pack")
            for h in range(rowValue, rowValue+objectHeight):
                for w in range(colomValue, colomValue+objectWidth):
                    tempMatrix[h][w].setObjectName(
                        data["Attractions"][attractionNum]["name"])
                    tempMatrix[h][w].setObjectColor(
                        data["Attractions"][attractionNum]["color"])
            
for i in range(0, 10):
    print("\n")
    
    line = ""
    for j in range(0, 10):
        # print(tempMatrix[i][j].getObjectName())
        line = line + (tempMatrix[i][j].getObjectName()) + " "
    print(line)   
