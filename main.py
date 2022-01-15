import tkinter as tk
import json
from PopulateMatrix import PopulateMatrix
from PathFinder import PathFinder

def main():
    print("starting carnival Routing")
    # main GUI window
    window = tk.Tk()
    # GUI Window initial size
    window.geometry("900x900")

    # create necessary frames for buttons and matrix output
    topFrame = tk.Frame(window)
    topFrame.pack(side = 'top')

    botFrame = tk.Frame(window)
    botFrame.pack(side = "bottom")

    # top label
    header = tk.Label(topFrame, text = "WEC Carnival Grounds", font=(112))
    header.pack(side ="top")

    info = tk.Label(topFrame, text = "The first stop added is the start point. The last stop added is the end point.")
    info.pack(side ="top")
    info2 = tk.Label(topFrame, text = "All stops inbetween are what is calculated.")
    info2.pack(side ="top")

    # drop down menu for start point, stops and end point
    # myAttractions = ["bathroom", "ferrisWheel", "bigRollerCoaster", "smallCoaster", "kidCoaster", "bumperCars", "popcornStand", "pizzaStand"]
    with open("CarnivalSetup.json") as file:
        data = json.load(file)
        attractionList = []
        for i in range(0, len(data["Attractions"])):
            attractionList.append(data["Attractions"][i]["name"])
         
        variable = tk.StringVar(topFrame)
        variable.set("Choose a stop to add") # set default value
        dropDown = tk.OptionMenu(topFrame, variable, *attractionList)
        dropDown.pack(side = "bottom")

    myStops = []
    allStops = []
    # add a stop to the array for the path chosen
    def addStopClick():
        # count = 0
        myStops=variable.get()
        allStops.append(variable.get())
        notAppend = True
        currStops = tk.Label(topFrame, text=myStops, bg="blue")
        if notAppend==True:
            currStops = tk.Label(topFrame, text=myStops, bg="blue")
            currStops.pack(side = "left")
            notAppend = False
        else:
            currStops.configure(text=myStops)

        print(allStops)
        

    # add a stop button
    addStop = tk.Button(topFrame, text="Add a Stop", activebackground = "blue", command = addStopClick)
    addStop.pack(side = "top")

    # printing the table 
    with open("CarnivalSetup.json") as file:
        data = json.load(file)
        matrixHeight = data["Board"]["height"]
        matrixWidth = data["Board"]["width"]
        print(matrixHeight)
        print(matrixWidth)

        ourMatrix = PopulateMatrix()

        
        for currHeight in range(0, matrixHeight):
            newFrame = tk.Frame(botFrame)
            newFrame.pack(side = "top")
            for currWidth in range(0, matrixWidth):
                attractionObject = tk.Label(newFrame, text = ourMatrix[currHeight][currWidth].getObjectName() + " " + str(currHeight) + " " + str(currWidth) , bg = ourMatrix[currHeight][currWidth].getObjectColor(), height=3, width=15)
                attractionObject.pack(side ="left")
                print(ourMatrix[currHeight][currWidth].getObjectName())

        def calculateClick():
            answer = PathFinder(allStops, ourMatrix)
            print(answer)
            answerFrame = tk.Frame(botFrame)
            answerFrame.pack(side = "bottom")
            answerLabel = tk.Label(answerFrame, text=answer)
            answerLabel.pack()

        calculateRoute = tk.Button(topFrame, text="Calculate Route", activebackground = "blue", command = calculateClick)
        calculateRoute.pack(side = "top")
        


    window.mainloop()

if __name__ == "__main__":
    main()
