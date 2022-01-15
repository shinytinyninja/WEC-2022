from CarnivalObject import CarnivalObject
from random import randint
import json

#PopulateMatrix Function will return a 10x10 matrix
#populated with CarnivalObject Objects
def PopulateMatrix():
    tempMatrix = [10][10]
    
    #Making every block a path
    #This ensures our 
    for row in range(0,10):
        for coloms in range(0,10):
            tempMatrix[row][coloms] = CarnivalObject("path")
    
    #Reading objects from JSON File
    with open("CarnivalSetup.json") as file:
        data = json.load(file)
    
    #Placing Objects
    for attractionNum in len(data["Attractions"]):
        data["Attractions"][attractionNum]
        errorInsert = False
        
        while (errorInsert):
            rowValue = randint(0,9)
            colomValue = randint(0,9)
            
            objectHeight = data["Attractions"][attractionNum]["height"]
            objectWidth = data["Attractions"][attractionNum]["width"]
            
            if((rowValue + objectHeight <= 9) and (colomValue + objectWidth <= 9)):
                for h in range (0,objectHeight):
                    for w in range (0,objectWidth):
                        if ((tempMatrix[rowValue + h][colomValue + w].getObjectName() != "path")):
                            errorInsert = True
            else:
                errorInsert = True

            if (errorInsert == False):
                for h in range (0, objectHeight):
                    for w in range (0, objectWidth):
                        tempMatrix[h][w].setObjectName(data["Attractions"][attractionNum]["name"])
                        tempMatrix[h][w].getObjectColor(data["Attractions"][attractionNum]["color"])
           
    for i in range(0,9):
        for j in range(0,9):
            print(tempMatrix[i][j])
    
    return tempMatrix