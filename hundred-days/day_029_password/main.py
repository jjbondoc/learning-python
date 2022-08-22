from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ('Arial', 10, 'normal')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    
    entry_pass.delete(0, END)
    entry_pass.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_website.get().lower()
    user = entry_user.get()
    password = entry_pass.get()
    new_data = {
        website:{
            "email": user,
            "password": password,
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
    else:
        try:
            with open("./passwords.json", 'r') as open_file:
                #Read the old data
                data = json.load(open_file)
                
        except FileNotFoundError:
            with open("./passwords.json", 'w') as open_file:
                #If the file doesn't exist, create a file
                json.dump(new_data, open_file, indent=4)
        else:
            #Update the old data with new data
            data.update(new_data)
            with open("./passwords.json", 'w') as open_file:
                #Saving the updated data
                json.dump(data, open_file, indent=4)
        finally:
            entry_website.delete(0, END) #delete characters starting from the first character, to the last (END)
            entry_pass.delete(0, END)
            
# ---------------------------- SEARCH --------------------------------- #
def search_password():
    search_website = entry_website.get().lower()
    try:
        with open("./passwords.json", 'r') as data_file:
            data = json.load(data_file)
    except:
        messagebox.showerror(title="Oops", message="No passwords saved yet.")
    else:
        if search_website in data:
            email = data[search_website]["email"]
            password = data[search_website]["password"]
            messagebox.showinfo(title=search_website.title(), message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Oops", message=f"No password found for {search_website.title()}.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_png = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=lock_png)
canvas.grid(column=1, row=0)

#label: website
label_website = Label(text="Website:", font=FONT)
label_website.grid(column=0, row=1)

#label: email/username
label_user = Label(text="Email/Username:", font=FONT)
label_user.grid(column=0, row=2)

#label: password
label_pass = Label(text="Password:", font=FONT)
label_pass.grid(column=0, row=3)

#entry: website
entry_website = Entry(width=28)
entry_website.grid(column=1, row=1)
entry_website.focus()

#entry: email/username
entry_user = Entry(width=50)
entry_user.insert(END, "example@email.com") #END is a tkinter constant that signifies the last position of a line of text
entry_user.grid(column=1, columnspan=2, row=2)

#entry: password
entry_pass = Entry(width=28)
entry_pass.grid(column=1, row=3)

#button: search
button_website = Button(text="Search", width=15, font=FONT, command=search_password)
button_website.grid(column=2, row=1)

#button: password
button_pass = Button(text="Generate Password", width=15, font=FONT, command=generate_password)
button_pass.grid(column=2, row=3)

#button: add
button_add = Button(text="Add", width=37, font=FONT, command=save_password)
button_add.grid(column=1, columnspan=2, row=4)

window.mainloop()