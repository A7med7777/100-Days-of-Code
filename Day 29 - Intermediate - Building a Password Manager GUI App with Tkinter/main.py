from cryptography.fernet import Fernet
from tkinter import messagebox
from tkinter import *
import pyperclip
import random
import json
import os


# ---------------------------- SECURITY SETUP ------------------------------- #
def load_or_generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()

        with open("key.key", "wb") as file:
            file.write(key)
    else:
        with open("key.key", "rb") as file:
            key = file.read()

    return Fernet(key)


cipher = load_or_generate_key()


def encrypt_data(data):
    return cipher.encrypt(data.encode()).decode()


def decrypt_data(data):
    return cipher.decrypt(data.encode()).decode()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()

    if website:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

            email = decrypt_data(data[website]["email"])
            password = decrypt_data(data[website]["password"])
            pyperclip.copy(password)
            messagebox.showinfo(website, message=f"Email/Username: {email}\nPassword: {password}")
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found.")
        except KeyError:
            messagebox.showwarning("Error", "No details for the website exists.")


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
    pass_entry.delete(0, "end")
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = email_entry.get()
    password = pass_entry.get()

    new_data = {
        website: {
            "email": encrypt_data(username),
            "password": encrypt_data(password),
        }
    }

    if website and username and password:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4, sort_keys=True)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4, sort_keys=True)
        finally:
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
website_entry = Entry(width=30, font=("arial", 10, "normal"))
website_entry.grid(row=1, column=1)

email_label = Label(text="Email/Username: ", font=("arial", 10, "normal"))
email_label.grid(row=2, column=0)
email_entry = Entry(width=45, font=("arial", 10, "normal"))
email_entry.grid(row=2, column=1, columnspan=2, sticky="WE")

pass_label = Label(text="Password: ", font=("arial", 10, "normal"))
pass_label.grid(row=3, column=0)
pass_entry = Entry(width=30, font=("arial", 10, "normal"))
pass_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", width=14, command=password_generator)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
