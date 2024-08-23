from tkinter import *
from tkinter import messagebox
import pyperclip
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = (
            [random.choice(letters) for _ in range(nr_letters)] +
            [random.choice(symbols) for _ in range(nr_symbols)] +
            [random.choice(numbers) for _ in range(nr_numbers)]
    )

    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"Your password is: {password}")
    pass_entry.delete(0, "end")
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = email_entry.get()
    password = pass_entry.get()

    if website and username and password:
        with open("pass.txt", "a") as pass_file:
            pass_file.write(f"{website} | {username} | {password}\n")

        website_entry.delete(first=0, last="end")
        email_entry.delete(first=0, last="end")
        pass_entry.delete(first=0, last="end")
    else:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=20, padx=20)

logo = PhotoImage(file="./logo.png")
canvas = Canvas(width=202, height=190)
canvas.create_image(101, 95, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", font=("arial", 10, "normal"))
website_label.grid(row=1, column=0)
website_entry = Entry(width=45, font=("arial", 10, "normal"))
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username: ", font=("arial", 10, "normal"))
email_label.grid(row=2, column=0)
email_entry = Entry(width=45, font=("arial", 10, "normal"))
email_entry.grid(row=2, column=1, columnspan=2)

pass_label = Label(text="Password: ", font=("arial", 10, "normal"))
pass_label.grid(row=3, column=0)
pass_entry = Entry(width=29, font=("arial", 10, "normal"))
pass_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
