from CarnivalObject import CarnivalObject
from random import randint

#PopulateMatrix Function will return a 10x10 matrix
#populated with CarnivalObject Objects
def PopulateMatrix():
    tempMatrix = [10][10]
    
    #Making every block a path
    #This ensures our 
    for row in range(0,10):
        for coloms in range(0,10):
            tempMatrix[row][coloms] = CarnivalObject("path")
    
    #Placing Objects
    print(randint(0,9))
    print(randint(0,9))
    objectsToPlace = []
    

    return tempMatrix