import tkinter as tk
import PopulateMatrix

def main():
    root = tk.Tk()
    root.title("Welcome to GeeksForGeeks")
    root.geometry('700x500')
    
    # matrix = PopulateMatrix()
    options_list = ["Option 1", "Option 2", "Option 3", "Option 4"]
    value_inside = tk.StringVar(root)
    value_inside.set("Select an Option")
    question_menu = tk.OptionMenu(root, value_inside, *options_list)
    question_menu.pack()
      
    def print_answers():
        print("Selected Option: {}".format(value_inside.get()))
        return None
    
    submit_button = tk.Button(root, text='Submit', command=print_answers)
    submit_button.pack()
    root.mainloop()

    # label.pack()
    # window.mainloop()
    
if __name__ == "__main__":
    main()