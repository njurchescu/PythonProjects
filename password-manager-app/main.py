from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """function to generate random password"""
    # Clear generated password
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = ''.join(password_list)
    # Generate the password in Password field
    password_entry.insert(END, password)
    pyperclip.copy(password)


# -----------------------------SEARCH BUTTON----------------------------------#

def search(before_save=False):
    website_exists = False
    website = website_entry.get().lower()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, ValueError):
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        for (key, value) in data.items():
            if website == key:
                website_exists = True
                email = data[key]["email"]
                password = data[key]["password"]
                # Check for entry before saving
                if before_save:
                    messagebox.showinfo(title="Already Exists",
                                        message=f"Found entry for {website.title()}.")
                    return True
                else:
                    messagebox.showinfo(title=website.title(), message=f" Email: {email}\n Password: {password}")
        # return nothing if no entry exists
        if before_save:
            return
        if len(website) == 0:
            messagebox.showinfo(title="Empty Field", message=f"Please fill in the {website_label.cget('text')}.")
        elif website_exists:
            pass
        else:
            messagebox.showinfo(title="No Details", message="No details for the website exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get().lower()
    email = email_entry.get().lower()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,

        }
    }
    if len(website) == 0:
        messagebox.showinfo(title="Empty Fields", message=f"Please fill in the {website_label.cget('text')}.")
    elif len(password) == 0:
        messagebox.showinfo(title="Empty Fields", message=f"Please fill in {password_label.cget('text')}.")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, ValueError):
            with open('data.json', 'w') as file:
                save = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email}'
                                                                     f'\nPassword: {password} \nIs it ok to save?')
                if save:
                    json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            # Check for entry before saving
            if search(True):
                if messagebox.askokcancel(title="Found", message="Would you like to update the password? "):
                    pass
                else:
                    return
            if messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email}'
                                                             f'\nPassword: {password} \nIs it ok to save?'):
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)

logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

website_entry = Entry()
website_entry.config(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry()
email_entry.config(width=51)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "njurchescu@yahoo.com")

password_entry = Entry()
password_entry.config(width=32)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)
search_button.config(width=15)

window.mainloop()
