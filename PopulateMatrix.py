from pickle import FALSE
from CarnivalObject import CarnivalObject
from random import randint
import json

# PopulateMatrix Function will return a variable matrix
# populated with CarnivalObject Objects


def PopulateMatrix():
    # Reading objects from JSON File
    with open("CarnivalSetup.json") as file:
        data = json.load(file)

    boardWidth, boardHeight = data["Board"]["height"], data["Board"]["width"]
    tempMatrix = [[0 for x in range(boardWidth)] for y in range(boardHeight)]

    # Making every block a path
    for row in range(0, boardHeight):
        for coloms in range(0, boardWidth):
            tempMatrix[row][coloms] = CarnivalObject("path", "#964B00")

    # Placing Objects
    for attractionNum in range(len(data["Attractions"])):
        print("\n attractionNum: {}".format(attractionNum))
        print(data["Attractions"][attractionNum]["name"])

        canInsert = False
        while (not canInsert):
            print("run Loop")
            rowValue = randint(0, boardHeight - 1)
            colomValue = randint(0, boardWidth - 1)
            print("rowValue: {}".format(rowValue))
            print("colomValue: {}".format(colomValue))

            objectHeight = data["Attractions"][attractionNum]["height"]
            objectWidth = data["Attractions"][attractionNum]["width"]

            canInsert = True
            if((rowValue + objectHeight < boardHeight) and (colomValue + objectWidth < boardWidth)):
                for h in range(0, objectHeight):
                    for w in range(0, objectWidth):
                        if ((tempMatrix[rowValue + h][colomValue + w].getObjectName() != "path")):
                            canInsert = False
            else:
                canInsert = False

            if (canInsert == True):
                for h in range(rowValue, rowValue + objectHeight):
                    for w in range(colomValue, colomValue + objectWidth):
                        tempMatrix[h][w].setObjectName(
                            data["Attractions"][attractionNum]["name"])
                        tempMatrix[h][w].setObjectColor(
                            data["Attractions"][attractionNum]["color"])

    for i in range(0, boardHeight):
        print("\n")
        line = ""
        for j in range(0, boardWidth):
            # print(tempMatrix[i][j].getObjectName())
            line = line + tempMatrix[i][j].getObjectName() + " "
        print(line)

    return tempMatrix
