import json
from CarnivalObject import CarnivalObject
import collections
from random import randint
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
    

# start = ()
# end = ()
# pitStops = []

# attractDict = {}
wall = []
# #find Location of Attractions
# for row in range(len(tempMatrix)):
#     for colom in range(len(tempMatrix[0])):
#         if (tempMatrix[row][colom].getObjectName() != "path"):
#             attractDict[tempMatrix[row][colom].getObjectName()] = (row, colom)    
#             wall.append((row,colom))      

start = (0,0)

matrixHeight = len(tempMatrix)
matrixWidth = len(tempMatrix[0])

queue = collections.deque([[start]])
seen = set([start])
while queue:
    print("Enter")
    path = queue.popleft()
    x, y = path[-1]
    if tempMatrix[y][x].getObjectName() == "kidCoaster":
        print("SUSUSUSUUSs")
        print(path)
        exit(0)
    for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
        if 0 <= x2 < matrixWidth and 0 <= y2 < matrixHeight and tempMatrix[y2][x2] != wall and (x2, y2) not in seen:
            queue.append(path + [(x2, y2)])
            seen.add((x2, y2))
            
print("end")