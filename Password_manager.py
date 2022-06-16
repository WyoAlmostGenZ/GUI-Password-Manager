from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- OLD PWD GEN -------------------------------
def generate():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
			   'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
			   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	# print("Welcome to the PyPassword Generator!")
	# nr_letters = int(input("How many letters would you like in your password?\n"))
	# nr_numbers = int(input(f"How many numbers would you like?\n"))
	# nr_symbols = int(input(f"How many symbols would you like?\n"))


	letters_ = ""
	for letter in range(3, 7):
		asd = random.choice(letters)
		letters_ += asd


	numbers_ = ""
	for number in range(3, 7):
		dsa = random.choice(numbers)
		numbers_ += dsa


	symbols_ = ""
	for symbol in range(2, 4):
		qwe = random.choice(symbols)
		symbols_ += qwe


	password = letters_ + numbers_ + symbols_
	list_password = list(password)
	random.shuffle(list_password)
	# print(list_password)
	pwd = ""
	for letter in list_password:
		pwd += letter

	contents_of_password = password_entry.get()

	if len(contents_of_password) == 0:
		password_entry.insert(0, pwd)





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SAVE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def save():
	contents_of_website = website_entry.get()
	contents_of_email = email_entry.get()
	contents_of_password = password_entry.get()

	if len(contents_of_website) or len(contents_of_email) or len(contents_of_password) == 0:
		messagebox.showinfo(title="Oops", message="Don't leave any fields empty")
	else:
		with open("data.txt", mode="a") as file:
			file.write(contents_of_website)
			file.write(" / ")
			file.write(contents_of_email)
			file.write(" / ")
			file.write(contents_of_password)
			file.write("\n")
			website_entry.delete(0, END)
			password_entry.delete(0, END)
			email_entry.delete(0, END)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GUI ~~~~~~~~~~~~~~~~~~~~~~~~~~~~



window = Tk()
window.minsize(height=200, width=200)
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_l = Label()
website_l.config(text="Website/App")
website_l.grid(column=0, row=1)


email_l = Label()
email_l.config(text="Email/Username")
email_l.grid(column=0, row=2)

password_l = Label()
password_l.config(text="Password: ")
password_l.grid(column=0, row=3)

website_entry = Entry()
website_entry.config(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry()
email_entry.config(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
# email_entry.insert(0, "test@gmail.com")


password_entry = Entry()
password_entry.config(width=17)
password_entry.grid(column=1, row=3)

generate_b = Button()
generate_b.config(text="Generate Password", command=generate)
generate_b.grid(column=2, row=3)

add_b = Button()
add_b.config(text="Add", width=30, command=save)
add_b.grid(column=1, row=4, columnspan=2)






window.mainloop()
