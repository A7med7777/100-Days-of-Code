from tkinter import *


def mile_to_km():
    try:
        mile = float(miles_entry.get())
    except ValueError as ve:
        print(ve)
    else:
        km = round(mile * 1.609344, 6)
        num_label.config(text=f"{km}")


window = Tk()
window.config(padx=20, pady=20)
window.title("Mile to Kilometers Converter")

miles_entry = Entry(window, width=10, font=('Arial', 15, 'bold'), justify="center")
miles_entry.grid(row=0, column=1)

miles_label = Label(window, text=" Miles ", font=('Arial', 15, 'normal'))
miles_label.grid(row=0, column=2)

is_equal_label = Label(window, text=" is equal to ", font=('Arial', 15, 'normal'))
is_equal_label.grid(row=1, column=0)

num_label = Label(window, text=" 0 ", font=('Arial', 15, 'bold'))
num_label.grid(row=1, column=1)

km_label = Label(window, text=" Km ", font=('Arial', 15, 'normal'))
km_label.grid(row=1, column=2)

button = Button(window, text=" Calculate ", font=('Arial', 15, 'bold'), command=mile_to_km)
button.grid(row=2, column=1)

window.mainloop()
