from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None
current_word = {}
to_learn = {}

# --------------------Read from cvs file-------------
try:
    data_file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_file = pandas.read_csv("data/french_words.csv")
    to_learn = original_file.to_dict(orient="records")
else:
    to_learn = data_file.to_dict(orient="records")


# -----------------------Generate Random Word---------------------------------------
def generate_word():
    global timer, current_word
    window.after_cancel("timer")
    current_word = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(canvas_title, text="French", fill="Black")
    canvas.itemconfig(canvas_word, text=current_word["French"], fill="Black")
    timer = window.after(3000, translate_word)


# ----------------------generate translation-------------------------------------

def translate_word():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(canvas_title, text="English", fill="White")
    canvas.itemconfig(canvas_word, text=current_word["English"], fill="White")


def is_known():
    to_learn.remove(current_word)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
canvas_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

wrong_button = PhotoImage(file="images/wrong.png")
x_button = Button(image=wrong_button, command=generate_word, highlightthickness=0)
x_button.grid(row=1, column=0)

right_button = PhotoImage(file="images/right.png")
check_button = Button(image=right_button, command=is_known, highlightthickness=0)
check_button.grid(row=1, column=1)

generate_word()

window.mainloop()
