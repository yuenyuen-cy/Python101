from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

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

    if website_data == "" or email_data == "" or password_data == "":
        messagebox.showinfo(title="Opps", message="Please do not leave any fields empty!!")

    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f"Would like to save these details?\n"
                                                           f"Email: {email_data}\n"
                                                           f"Password: {password_data}")
        if is_ok:

            with open("data.txt", "a") as data:
                data.write(f"{website_data} | {email_data} | {password_data}\n")

            website_input.delete(0, 'end')
            email_input.delete(0, 'end')
            email_input.insert(0, "default@gmail.com")
            password_input.delete(0, 'end')

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
website_input = Entry(width=42)
email_input = Entry(width=42)
email_input.insert(0, "default@gmail.com")
password_input = Entry(width=32)

website_input.grid(row=2, column=2, columnspan=2)
email_input.grid(row=3, column=2, columnspan=2)
password_input.grid(row=4, column=2)

## Buttons ##
generate_button = Button(text="Generate", command=generate_password)
add_button = Button(text="Add", width=36, command=save_password)

generate_button.grid(row=4, column=3)
add_button.grid(row=5, column=2, columnspan=2,pady=10)


window.mainloop()