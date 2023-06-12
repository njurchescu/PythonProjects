from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=200, height=90)
window.config(padx=10, pady=10)


def calculate():
    miles = int(miles_entry.get())
    km = round(miles * 1.609344, 2)
    converted_km_label.config(text=f"{km}")


miles_entry = Entry(width=10)
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)


equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)
equal_to_label.config(padx=5, pady=5)

converted_km_label = Label(text="0")
converted_km_label.grid(column=1, row=1)
converted_km_label.config(padx=5, pady=5)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=5, pady=5)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=3)



window.mainloop()
