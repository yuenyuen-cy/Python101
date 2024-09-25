from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip

FONT = "Arial"
FONT_SIZE = 10
FONT_TYPE = "normal"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_input.delete(0, 'end')

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()

    new_data = {
        website_data: {
        "email":email_data,
        "password": password_data
        }
    }

    if website_data == "" or email_data == "" or password_data == "":
        messagebox.showinfo(title="Opps", message="Please do not leave any fields empty!!")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open ("data.json", "w") as data_file:
               json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, 'end')
            password_input.delete(0, 'end')

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website_data = website_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")

    if len(website_data) == 0:
        messagebox.showinfo(title="Opps", message="Please input a website.")

    elif website_data in data:
        email = data[website_data]["email"]
        password = data[website_data]["password"]
        messagebox.showinfo(title=website_data, message=f"Email:{email}\n Password: {password}")

    else:
        messagebox.showinfo(title="Not Found", message="No entry found for this website.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(85, 100, image=logo_img)
canvas.grid(row=1, column=2)

## Labels ##
website_label = Label(text="Website:", font=(FONT, FONT_SIZE, FONT_TYPE), bg="white")
email_label = Label(text="Email/Username:", font=(FONT, FONT_SIZE, FONT_TYPE), bg="white")
password_label = Label(text="Password:", font=(FONT, FONT_SIZE, FONT_TYPE), bg="white")

website_label.grid(row=2, column=1)
email_label.grid(row=3, column=1)
password_label.grid(row=4, column=1)

## Inputs ##
website_input = Entry(width=32)
email_input = Entry(width=42)
email_input.insert(0, "default@gmail.com")
password_input = Entry(width=32)

website_input.grid(row=2, column=2)
email_input.grid(row=3, column=2, columnspan=2)
password_input.grid(row=4, column=2)

## Buttons ##
generate_button = Button(text="Generate", command=generate_password)
add_button = Button(text="Add", width=36, command=save_password)

generate_button.grid(row=4, column=3)
add_button.grid(row=5, column=2, columnspan=2,pady=10)

search_button = Button(text="Search", padx=5.5, command=find_password)
search_button.grid(row=2, column=3)
window.mainloop()
