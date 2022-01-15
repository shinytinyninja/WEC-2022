import tkinter as tk
import json
import PopulateMatrix

def main():
    print("starting carnival Routing")
    # main GUI window
    window = tk.Tk()
    # GUI Window initial size
    window.geometry("400x400")

    # create necessary frames for buttons and matrix output
    topFrame = tk.Frame(window)
    topFrame.pack(side = 'top')

    botFrame = tk.Frame(window)
    botFrame.pack(side = "bottom")

    # top label
    header = tk.Label(topFrame, text = "WEC Carnival Grounds", font=(512))
    header.pack(side ="top")

    info = tk.Label(topFrame, text = "The first stop added is the start point. The last stop added is the end point.")
    info.pack(side ="top")
    info2 = tk.Label(topFrame, text = "All stops inbetween are what is calculated.")
    info2.pack(side ="top")

    # drop down menu for start point, stops and end point
    myAttractions = ["bathroom", "ferrisWheel", "bigRollerCoaster", "smallCoaster", "kidCoaster", "bumperCars", "popcornStand", "pizzaStand"]
    variable = tk.StringVar(topFrame)
    variable.set("Choose a stop to add") # set default value
    dropDown = tk.OptionMenu(topFrame, variable, *myAttractions)
    dropDown.pack(side = "bottom")

    myStops = []
    # add a stop to the array for the path chosen
    def addStopClick():
        myStops.append(variable.get())
        print(myStops)

    # add a stop button
    addStop = tk.Button(topFrame, text="Add a Stop", activebackground = "blue", command = addStopClick)
    addStop.pack(side = "top")

    # printing the table 
    with open("CarnivalSetup.json") as file:
        data = json.load(file)
        print(data["Board"]["Height"])
        print(data["Board"]["Width"])

    window.mainloop()

if __name__ == "__main__":
    main()
