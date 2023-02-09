from tkinter import *
# a function not a class, so it is not added with the *
from tkinter import messagebox
import pyperclip
# import xsel

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import randint, choice, shuffle
# ran_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
# vs
# ran_letters = [choice(letters) for _ in range(randint(8, 10))]

def generate_password():
  password_entry.delete(0,END)
  
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
  
  password_list = []
  # choose a random item from the list a certain number of times :/
  ran_letters = [choice(letters) for _ in range(randint(8, 10))]
  ran_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  ran_numbers = [choice(numbers) for _ in range(randint(2, 4))]
  password_list = ran_letters + ran_symbols + ran_numbers
  shuffle(password_list)

  # join puts items in lisst/tuple/etc together 
  # password = ""
  # for char in password_list:
  #   password += char
  password = "".join(password_list)
  password_entry.insert(0, password)
  # adds whatever is in () to clipboard, ready to be pasted
  pyperclip.copy(password)
  pyperclip.paste()

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_information():
  website = website_entry.get()
  username = username_entry.get()
  password = password_entry.get()

  if len(website) == 0 or len(password) == 0:
    is_empty = messagebox.showerror(title="Oops!", message=f"You forgot to enter your information")
  else:
    # messagebox returns a boolean
    is_correct = messagebox.askyesnocancel(title=website, message=f"These are the details entered:\nEmail: {username}\nPassword: {password}")
    if is_correct:
      with open("login_information.txt", mode="a") as new_passwords:
          new_passwords.writelines(f"{website},{username},{password}\n")
    website_entry.delete(0,END)
    password_entry.delete(0,END)
    # else:
    #   website_entry.delete(0,END)
    #   password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height = 200, bg="white", highlightthickness=0)

lock_img = PhotoImage(file="logo.png")
# create image needs a tuple of x and y positions and image
canvas.create_image(100, 100, image = lock_img)
canvas.grid(column=1,row=0)

# labels
website_label = Label(text="Website:", font=(FONT_NAME, 14), bg="white", highlightthickness=0)
website_label.grid(column=0,row=1)
username_label = Label(text="Email/Username:", font=(FONT_NAME, 14), bg="white", highlightthickness=0)
username_label.grid(column=0,row=2)
password_label = Label(text="Password:", font=(FONT_NAME, 14), bg="white", highlightthickness=0)
password_label.grid(column=0,row=3)

# entries
website_entry = Entry(width=42)
website_entry.grid(column=1,row=1,columnspan=2)
# starts cursor in this entry
website_entry.focus()
username_entry = Entry(width=42)
username_entry.grid(column=1,row=2,columnspan=2)
# prepopulated with commonly used username/password_label
username_entry.insert(0, "jaja0304@gmail.com")
password_entry = Entry(width=24)
password_entry.grid(column=1,row=3)

# buttons
generate_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_button.grid(column=2,row=3)
add_button  = Button(text="Add", width=40, bg="white", command=add_information)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()

################### BECAUSE PYPERCLIP COULDNT FIND COPY/PASTE MECHANISM FOR MY SYSTEM ##################
'''
COPY TO CLIPBOARD WORKS IN PYCHARM JUST A REPLIT ISSUE?

~/passwordmanager4$ xclip
xclip: command not installed, but was located via Nix.
Would you like to run xclip from Nix and add it to your replit.nix file? [Yn]: Y
Adding xclip to replit.nix
success

fixed error: pyperclip could not find a copy/paste mechanism for your system
but still not able to copy to clipboard
'''
