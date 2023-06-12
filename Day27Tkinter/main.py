from tkinter import *


def button_clicked():
    new_text = new_input.get()
    my_label.config(text=new_text)


#
windows = Tk()
windows.title("My first GUI program")
# windows.minsize(width=500, height=300)
# windows.config(padx=30, pady=30)

# Label

my_label = Label(text="Write something here", font=("Courier", 15, "bold"))
my_label.config(text="New Text")
# pack the label onto the screen
# my_label.pack(side="left")
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=10)

# Button

button = Button(text="Click Me", command=button_clicked)
# button.pack(side="left")
button.grid(column=1, row=1)
button_2 = Button(text="Second Button")
button_2.grid(column=2, row=0)

# Entry

new_input = Entry(width=10)
# input.pack(side="left")
new_input.grid(column=3, row=2)

windows.mainloop()
