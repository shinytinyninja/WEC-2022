import tkinter as tk
import PopulateMatrix

def main():
    print("starting carnival Routing")
    window = tk.Tk()
    window.geometry("400x400")
    label = tk.Label(
        text="Western Enginnering",
        width=40,
        height=20,
        bg="purple",
        )
    
    matrix = PopulateMatrix()
    
    label.pack()
    window.mainloop()
    
if __name__ == "__main__":
    main()