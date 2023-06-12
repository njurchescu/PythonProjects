from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    global rep
    rep = 0
    check_label.config(text="")
    canvas.itemconfig(timer_set, text="00:00")
    timer_label.config(text="Timer")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 1

    global rep
    rep += 1
    # print(f"l break {rep} % {8} = {rep % 8}")
    # print(f"l break {rep} % {2} = {rep % 2}")
    if rep % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="L_Break", fg=RED)
    elif rep % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work")
        count_down(work_sec)
        # timer_label.config(text="Break")
        # count_down(short_break_sec)
        work_on = False


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_set, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(rep / 2)
        for _ in range(work_sessions):
            marks += "✔"
            check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 110, image=tomato_img)
timer_set = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
