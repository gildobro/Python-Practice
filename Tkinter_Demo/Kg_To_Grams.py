from tkinter import *

# Create an empty Tkinder window
window = Tk()

def from_kg():
    # Get user value from input box and multiply by 1000 to get kilograms
    grams = float(e2_value.get())*1000
    
    # Get user value from input box and multiply by 2.20462 to get pounds
    pounds = float(e2_value.get())*2.20462

    # Get user value from input box and multiply by 35.274 to get ounces
    ounces = float(e2_value.get())*35.274

    # Empty the Text boxes if they had text from the previous use and fill them with content
    t1.delete("1.0",END) # Deletes the content of the Text box from start to END
    t1.insert(END,grams) # Fills in the text boxes with the value of gram variable
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    t3.delete("1.0", END)
    t3.insert(END, ounces)

# Create a Label widget with "Kg" as label
e1 = Label(window,text="Enter an amount (in Kg):")
e1.grid(row=0,column=0) # The Label is placed in position 0, 0 in the window

e2_value = StringVar() # Create a special StringVar object
e2 = Entry(window,textvariable=e2_value) # Create an Entry box for users to enter the value
e2.grid(row=0,column=1)

e3 = Label(window,text="grams")
e3.grid(row=2,column=0)

e4 = Label(window,text="pounds")
e4.grid(row=2,column=1)

e3 = Label(window,text="ounces")
e3.grid(row=2,column=2)

# Create a button widget
# The from_kg() function is called when the button is pushed
b1 = Button(window,text="Convert",command = from_kg)
b1.grid(row=0,column=2)

# Create three empty text boxes, t1, t2, t3
t1 = Text(window, height=1,width=20)
t1.grid(row=1,column=0)

t2 = Text(window, height=1,width=20)
t2.grid(row=1,column=1)

t3 = Text(window, height=1,width=20)
t3.grid(row=1,column=2)

# This makes sure to keep the main window open
window.mainloop()