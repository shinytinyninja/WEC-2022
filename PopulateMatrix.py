from pickle import FALSE
from CarnivalObject import CarnivalObject
from random import randint
import json

# PopulateMatrix Function will return a 10x10 matrix
# populated with CarnivalObject Objects


def PopulateMatrix():
    w, h = 10, 10
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
    for attractionNum in range(len(data["Attractions"])):
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
                canInsert = True

            if (canInsert == False):
                for h in range(0, objectHeight):
                    for w in range(0, objectWidth):
                        tempMatrix[h][w].setObjectName(
                            data["Attractions"][attractionNum]["name"])
                        tempMatrix[h][w].setObjectColor(
                            data["Attractions"][attractionNum]["color"])

    for i in range(0, 9):
        for j in range(0, 9):
            print(tempMatrix[i][j])

    return tempMatrix
