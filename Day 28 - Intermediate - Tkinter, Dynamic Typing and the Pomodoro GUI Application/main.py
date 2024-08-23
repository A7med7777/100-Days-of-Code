from tkinter import *
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#F8C4B4"
RED = "#FF8787"
GREEN = "#BCE29E"
YELLOW = "#E5EBB2"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
count = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global count, timer

    count = 0

    if timer:
        window.after_cancel(timer)

    timer_label.config(text="Timer")
    start_button.config(state=NORMAL)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_mechanism():
    global count

    start_button.config(state=DISABLED)
    check_mark.config(text="✔️" * int(count / 2))
    count += 1

    if count % 8 == 0:
        messagebox.showinfo(title="Long Break", message="Time for a long break!")
        timer_label.config(text="Break", fg=RED)
        countdown_mechanism(LONG_BREAK_MIN * 60)
    elif count % 2 == 0:
        messagebox.showinfo(title="Short Break", message="Time for a short break!")
        timer_label.config(text="Break", fg=PINK)
        countdown_mechanism(SHORT_BREAK_MIN * 60)
    else:
        messagebox.showinfo(title="Work Session", message="Time to work!")
        timer_label.config(text="Work", fg=GREEN)
        countdown_mechanism(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown_mechanism(time):
    global timer

    mins = int(time / 60)
    secs = int(time % 60)
    canvas.itemconfig(timer_text, text=f"{int(mins / 10)}{int(mins % 10)}:{int(secs / 10)}{int(secs % 10)}")

    if time != 0:
        timer = window.after(1000, countdown_mechanism, time - 1)
    else:
        timer_mechanism()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(bg=YELLOW, padx=44, pady=44)

timer_label = Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1, pady=22, padx=22)

start_button = Button(text="start", font=(FONT_NAME, 10, "normal"), command=timer_mechanism)
reset_button = Button(text="Reset", font=(FONT_NAME, 10, "normal"), command=timer_reset)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

check_mark = Label(window, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_mark.grid(row=2, column=1)

window.mainloop()
