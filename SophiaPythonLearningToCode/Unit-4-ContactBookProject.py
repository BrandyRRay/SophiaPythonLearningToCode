#Unit 4: Project
import csv
import sys

#Welcome Statement. Ask for imported .csv file to begin, or ask user to name file if creating new
	#If Importing, Import file {FILENAME}
	#If creating new, Create new file {FILENAME}
FILENAME = input("Enter the existing file name. If Creating new file, enter name of new file: ")


#Provide a USER MENU of options
	#View Existing Contact
	#Edit existing Contact
	#Delete existing Contact
	#Exit
def display_menu():
    print("Welcome to your Contact Creator. What do you want to do?")
    print()
    print("LIST OF COMMANDS")
    print("add -  Add a New Contact")
    print("view - View an Existing Contact")
    print("edit - Edit an Existing Contact")
    print("del -  Delete an Existing Contact")
    print("exit - Exit program")
    print()

display_menu()
contacts = read_contacts()
while True:    
    command = input("Command: ")
    if command.lower() == "add":
        add_contacts(contacts)
    elif command.lower() == "view":
        view_contacts(contacts)
    elif command.lower() == "edit":
        edit_contacts(contacts)
    elif command.lower() == "del":
        delete_contact(contacts)
    elif command.lower() == "exit":
        break
    else:
        print("Not a valid command. Please try again.\n")
print("Ending Program")

#Loop Menu
	#Place try/except error catch statement here
	#If USER selects Add New Contact:
		#Place try/except error catch statement here
		#Request input from USER
		#Name
		#Address 
		#Number
		#Email
		#Category
		#Facebook
		#Twitter / X
		#IG
	#Open {FILENAME} as Write
	#Write value(s) to new row in {FILENAME}
	#Back to USER MENU
#If USER selects View Existing Contact:
def view_contacts():
	#Place try/except error catch statement here
	try:
		contacts = []
		with open(FILENAME, newline="") as file:
			reader = csv.reader(file)
			for row in reader:
				contacts.append(row)
				return contacts
			except FileNotFoundError as error:
				print(f"Could not find {FILENAME} file")
				exit_program()
			except Exception as e:
				print(type(e), e)
				exit_program()
	
	#Request input from USER, Contact Name
	#Open {FILENAME} as Read
	#Return value of row or rows in {FILENAME}
	#Else Could not find “ “ in {FILENAME}
	#Back to USER MENU
#If USER selects Edit Existing Contact:
	#Place try/except error catch statement here
	#Request input from USER, Contact Name
	#Select value to edit
		#Address 
		#Number
		#Email
		#Category
		#Facebook
		#Twitter / X
		#IG
	#Open {FILENAME} as Write
	#Overwrite value(s) to existing row in {FILENAME}
	#Back to USER MENU
#If USER selects Delete Existing Contact:
	#Place try/except error catch statement here
	#Request input from USER, Contact Name
	#Open {FILENAME}
	#Find correct row in {FILENAME} and Delete
	#Return Contact Deleted message
	#Else Could not find “ “ in {FILENAME}
	#Back to USER MENU
#If USER selects Create New Contacts .csv File for Export:
	#Place try/except error catch statement here
	#Request input from USER, .csv File Name
	#Request input from USER, property type name to select for (Category)
	#Open Original{FILENAME} as Read
		#Create New{FILENAME} as Write
		#Loop through Original using If/else statement to select correct Category names
#If USER selects Exit:
	#Quit Program
def exit_program():
  print("Ending program")
  sys.exit()
