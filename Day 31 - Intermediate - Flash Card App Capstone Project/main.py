from tkinter import *
import pandas
import os

BACKGROUND_COLOR = "#B1DDC6"
count = 0


def get_words():
    if not os.path.exists("./data/words_to_learn.csv"):
        french_words = pandas.read_csv("./data/french_words.csv")
    else:
        french_words = pandas.read_csv("./data/words_to_learn.csv")

    return [[row.French, row.English] for index, row in french_words.iterrows()]


def next_card():
    global count, flip_timer
    french_word = french_words_list[count][0]
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text='French', fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global count, flip_timer
    english_word = french_words_list[count][1]
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text='English', fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")
    window.after_cancel(flip_timer)


def right_checked():
    global count
    if french_words_list:
        french_words_list.pop(count)
    next_card()


def wrong_checked():
    global count
    count += 1

    if count >= len(french_words_list):
        count = 0

    next_card()


french_words_list = get_words()

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=30, pady=30)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=False)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=False, borderwidth=0, command=wrong_checked)
wrong_button.grid(row=1, column=0)

right = PhotoImage(file="./images/right.png")
right_button = Button(image=right, highlightthickness=False, borderwidth=0, command=right_checked)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()

df = pandas.DataFrame(french_words_list, columns=["French", "English"])
df.to_csv("./data/words_to_learn.csv", index=False)
