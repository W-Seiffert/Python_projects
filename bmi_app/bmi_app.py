'''
Created on 15.11.2020
@author: Walter
This program, the modest output of a standard programming exercise, provides a very basic GUI app 
designed to calculate the "body mass index" (BMI) as it is commonly defined (= the body weight 
divided by the square of the body height).
'''

import tkinter as tk


class Application(tk.Frame):
    
    # variables for some default values regarding the design
    def_colour = "lightyellow"
    def_font = "Georgia"


    def __init__(self, master):
        ''' Create an instance of the "Application" class, that is: allocate a new "Application"
        object and initialize its attributes (~ class constructor). '''
        tk.Frame.__init__(self, master, bg=self.def_colour)
        self.master.config(background=self.def_colour)
        self.grid()
        self.grid_columnconfigure((0,1), weight=1)
        self.create_widgets()

    
    def create_widgets(self):
        ''' Create a set of tkinter widges that, taken together, make up the application's
        graphical user interface. '''
        # title label
        self.title_label = tk.Label(root, text="Body Mass Index App", font=(self.def_font, 26), bg=self.def_colour, borderwidth=5, relief="groove", padx=10, pady=10)
        self.title_label.grid(row=0, columnspan=2, padx=20, pady=15, sticky="nsew")
        # image label visualising the meaning / interpretation of the BMI
        self.photo = tk.PhotoImage(file="BMI_pic.png")
        self.photo = self.photo.subsample(8,8)
        self.image_label = tk.Label(image=self.photo, bg=self.def_colour)
        self.image_label.image = self.photo
        self.image_label.grid(row=1, columnspan=2, padx=5, pady=5)
        
        # set of widges (labels + entries, arranged on a canvas) for the user input
        self.command_label = tk.Label(root, text="To get your BMI, please enter your data below!", font=(self.def_font, 16), bg=self.def_colour)
        self.command_label.grid(row=2, columnspan=2, padx=5, pady=5)
        
        self.inp_canvas = tk.Canvas(root, bg=self.def_colour)
        self.arrow = tk.PhotoImage(file="arrow_small.png")
        
        self.arrow_label_1 = tk.Label(self.inp_canvas, image=self.arrow, bg=self.def_colour)
        self.label_1 = tk.Label(self.inp_canvas, text="your weight (in kg): ", font=(self.def_font, 11), bg=self.def_colour)
        self.entry_1 = tk.Entry(self.inp_canvas, textvariable=value_1, font=(self.def_font, 11))
        self.arrow_label_1.grid(row=0, column=0, padx=5, pady=3)
        self.label_1.grid(row=0, column=1, padx=5, pady=5)
        self.entry_1.grid(row=0, column=2, padx=5, pady=5)
   
        self.arrow_label_2 = tk.Label(self.inp_canvas, image=self.arrow, bg=self.def_colour) 
        self.label_2 = tk.Label(self.inp_canvas, text="your height (in cm): ", font=(self.def_font, 11), bg=self.def_colour)
        self.entry_2 = tk.Entry(self.inp_canvas, textvariable=value_2, font=(self.def_font, 11))
        self.arrow_label_2.grid(row=1, column=0, padx=5, pady=3)
        self.label_2.grid(row=1, column=1, padx=5, pady=5)
        self.entry_2.grid(row=1, column=2, padx=5, pady=5)
        
        self.inp_canvas.grid(row=3, columnspan=2, padx=5, pady=5)
        
        # button to start the validation of the user input and, if possible, the calculation of the BMI
        self.calc_button = tk.Button(root, text="calculate your BMI", font=(self.def_font, 14), bg="palegoldenrod", command=self.calculate_BMI)
        self.calc_button.grid(row=4, columnspan=2, padx=5, pady=10)
        
        # label to display the calculation's result or a short error message in the case of invalid or missing inputs
        self.evaluation_label = tk.Label(root, text="EVALUATION", font=(self.def_font, 12), fg="grey", bg="lemonchiffon", borderwidth=5, relief="ridge", padx=10, pady=10)
        self.evaluation_label.grid(row=5, columnspan=2, padx=5, pady=10)
        
        # two navigation buttons: to restart or to quit the program, respectively
        self.restart_button = tk.Button(root, text="RESTART", font=(self.def_font, 12), fg="white", bg="black", borderwidth=4, width=10, command=self.restart)
        self.restart_button.grid(row=6, column=0, padx=5, pady=5)
        self.exit_button = tk.Button(root, text="EXIT", font=(self.def_font, 12), fg="white", bg="black", borderwidth=4, width=10, command=root.destroy)
        self.exit_button.grid(row=6, column=1, padx=5, pady=5)

        
    def calculate_BMI(self):
        ''' Validate the user's inputs, if there are any, and, provided they are valid, calculate 
        the Body Mass Index based on these inputs. Otherwise display a temporary error message to 
        the user. '''
        # initialise a set of control variables
        weight_ok = height_ok = False
        non_nr_inputs = 0
        unrealistic_inputs = 0
        
        # check the input for the user's weight
        try:
            user_weight = float(self.entry_1.get())
            if (user_weight < 1000) and (user_weight > 5):
                weight_ok = True
            else:
                unrealistic_inputs += 1
        except ValueError:
            non_nr_inputs += 1
        # check the input for the user's height  
        try:
            user_height = float(self.entry_2.get()) / 100
            if (user_height < 2.8) and (user_height > 0.5):
                height_ok = True
            else:
                unrealistic_inputs += 1
        except ValueError:
            non_nr_inputs += 1                        
        
        # depending on the result of the validation, calculate the BMI or provide an error message                        
        if weight_ok and height_ok:
            user_BMI = round((user_weight / user_height ** 2), 2)
            self.evaluation_label.config(text="Your BMI: " + str(user_BMI), font=(self.def_font, 14), fg="green", pady=8)
        else:
            if non_nr_inputs > 0:
                self.evaluation_label.config(text="NOTE: You have to enter numeric values in the textfields!", font=(self.def_font, 12), fg="red")
            if self.entry_1.get() and not weight_ok:
                self.entry_1.config(fg="red")
                self.entry_1.insert(0, "! ")
            if self.entry_2.get() and not height_ok:
                self.entry_2.config(fg="red")
                self.entry_2.insert(0, "! ")
            if unrealistic_inputs > 0:
                self.insert_message()
            self.after(2500, lambda: self.reset_widgets())


    def insert_message(self):
        ''' Display a request to the user to revise his input, if he has entered unrealistic values. '''
        self.message_label = tk.Label(root, text="Please enter realistic values!", font=(self.def_font, 12), fg="red", 
                                      bg="lemonchiffon", borderwidth=5, relief="ridge", padx=5, pady=10)
        self.message_label.grid(row=4, columnspan=2, padx=5, pady=5)
        self.message_label.after(2500, self.message_label.destroy)


    def reset_widgets(self):
        ''' Reset the entry fields and the evaluation label to their original state
        (after an input has been identified as invalid or the user has clicked the 
        RESTART button). '''
        # a) reset entries for user input, if necessary
        try:
            weight_input = self.entry_1.get()
            height_input = self.entry_2.get()
            if weight_input and weight_input[0] == "!":
                self.entry_1.delete(0, tk.END)
                self.entry_1.config(fg="black")
            if height_input and height_input[0] == "!":
                self.entry_2.delete(0, tk.END)
                self.entry_2.config(fg="black")
        except ValueError:
            pass
        # b) reset evaluation label
        self.evaluation_label.config(text="EVALUATION", font=(self.def_font, 12), fg="grey", pady=10)

    
    def restart(self):
        ''' "Restart" the app by clearing the entry fields and the evaluation label. '''
        self.entry_1.delete(0, tk.END)
        self.entry_1.config(fg="black")
        self.entry_2.delete(0, tk.END)
        self.entry_2.config(fg="black")
        self.evaluation_label.config(text="EVALUATION", font=(self.def_font, 12), fg="grey", pady=10)



# initialise a tcl/tk interpreter and create a root window for the app
root = tk.Tk()
root.title("BMI App 0.1")

# use two built-in functions to get the screen size values
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# define the width and height of the app's main window
app_width = 500
app_height = 600
# calculate coordinates for drawing the main window
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
# define the dimensions of the main window and its position on the user's desktop
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.grid_columnconfigure((0,1), weight=1)

# create two String variable objects, intended to store the user input
value_1 = tk.StringVar()
value_2 = tk.StringVar()

# create an instance of the Application class
app = Application(root)
# start an infinite loop that keeps updating the root window and thereby the application running
root.mainloop()
