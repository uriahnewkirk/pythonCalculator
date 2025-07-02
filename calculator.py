import tkinter
import math

#define values/buttons on calculator interface
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
];

#placement of special calculator characters
r_symbols = ["÷", "×", "-", "+", "="];
t_symbols = ["AC", "+/-", "%"];

rows = len(button_values)
columns = len(button_values[0])

#colors to be used within calculator interface
color_faded_cyan = "#39aac6";
color_tan = "#80734d"
color_light_grey = "#D4D4D2";
color_black = "#1C1C1C";
color_dark_grey = "#505050";
color_orange = "#FF9500";
color_white = "white";

#calculator UI interface
window = tkinter.Tk();
window.title("Calculator");
window.resizable(False, False);

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black, foreground=color_faded_cyan, anchor="e", width=columns)
label.grid(row=0, column=0, columnspan=columns, sticky="we")

#apply styling to the interface interating through each UI button
for row in range(rows):
    for column in range(columns):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30), width=columns-1, height=1, command=lambda value=value: button_clicked(value))

        if value in t_symbols:
            button.config(foreground=color_white, background=color_black)
        elif value in r_symbols:
            button.config(foreground=color_white, background=color_black)
        else:
            button.config(foreground=color_faded_cyan, background=color_black)

        button.grid(row=row+1, column=column)

frame.pack();


#default arithmetic variable values
A = "0"
operator = None
B = None


#function for clearing calculator display after a "right symbol" 
#button is selected or when the "AC" button is pressed
def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None


#remove unnecessary decimal
def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


#function to evaluate each button press
def button_clicked(value):
    global r_symbols, t_symbols, label, A, B, operator
    if value in r_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                #perform appropriate operation based on chosen operator
                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)
                
                clear_all();

        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operator = value
        
    elif value in t_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    elif value == "√":
        #user types in a number then presses square root
        #button to find square root of that number
        if A is not None:
            A = label["text"]
            numA = float(A)
            label["text"] = remove_zero_decimal(math.sqrt(numA))

    #numeric digit or decimal point
    else:
        if value == ".":
            #if decimal point
            if value not in label["text"]:
                label["text"] += value
        
        elif value in "0123456789":
            #if numeric digit
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value


window.update()
#width & height of the tkinter window
window_width = window.winfo_width()
window_height = window.winfo_height()
#retrive the user's screen width & height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
#draw UI window based on size of the user's screen
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()