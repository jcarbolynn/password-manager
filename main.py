from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

  password_list = password_letters + password_symbols + password_numbers
  shuffle(password_list)

  password = "".join(password_list)
  password_entry.insert(0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  website = website_entry.get()
  email = email_entry.get()
  password = password_entry.get()
  new_data = {
    website: {
      "email": email,
      "password": password,
    }
  }

  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
  else:
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password} \nIs it ok to save?")
    if is_ok:
      # TODO: handle FileNotFoundError, create a new data.json file if it does not exist, if file exists add new_data

      # # this creates json file if it does not exist
      # with open("data.json", "w") as data_file:
      #   data = json.dump(new_data, data_file, indent=2)

      try:
      # this has a FileNotFoundError if json file does not exist, opening in read mode dangerous because error if does not exist
        with open("data.json", "r") as data_file:
          data = json.load(data_file)

      except FileNotFoundError:
        # if file not found create it
        with open("data.json", "w") as data_file:
          # and dump new data dictionary into it
          data = json.dump(new_data, data_file, indent=2)
          # dont need to update any existing data because it fails if the file does not exist yet
      else:
        # if file is found and it does exist, update data with new_data
        # else only triggered if everything in try block successful
        new_data.update(data)
        # dump new ifnormation into data file 
        with open("data.json", "w") as data_file:
          json.dump(new_data, data_file, indent=2)  
      finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
  website = website_entry.get().lower()
  try:
    # works because we have data and a json file
    with open("data.json", "r") as data_file:
      data = json.load(data_file)
      
  except FileNotFoundError:
    # if no json  file, this will tell users they need to enter some websites and passwords
    messagebox.showinfo(title="Error", message="No data file found")

  else:    
      if website in data: # in data not data_file because you have to load the information to access/read it, loading json saves it to a dictionary
        # website not in "" because it is a variable referring to the website_entry
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
      else:
        # could raise an exception and catch but stick to if and else if you can, exceptions should happen infrequently, if/else happen a lot
        messagebox.showinfo(title="Error", message=f"No details for {website} exsist")

  
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "jaja0304@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
