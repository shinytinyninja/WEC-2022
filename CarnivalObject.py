# Carnival objects for the carnival grounds
# bathroom, ferrisWheel, path, bigRollerCoaster, smallCoaster, kidCoaster, bumperCars, popcornStand, pizzaStand
class CarnivalObject:
    # constructor for the class, sets the carnival's object name
    def __init__(self, carnivalObjectName, carnivalObjectColor):
        self.carnivalObjectName = carnivalObjectName
        self.carnivalObjectColor = carnivalObjectColor

    # getter for the carnival object name
    # returns the name of the carnival object
    def getObjectName(self):
        return self.carnivalObjectName

    # setter for the carnival object name
    # sets the name of the carnival object
    def setObjectName(self, newObjectName):
        self.carnivalObjectName = newObjectName

    # getter for the carnival object color
    # returns the color of the carnival object
    def getObjectColor(self):
        return self.carnivalObjectColor

    # setter for the carnival object color
    # sets the color of the carnival object
    def setObjectColor(self, newObjectColor):
        self.carnivalObjectColor = newObjectColor