#Unit 4: Project
import csv
import sys
import os

#Welcome Statement. Ask for imported .csv file to begin, or ask user to name file if creating new
FILENAME = input("Enter the existing file name. If Creating new file, enter name of new file: ")

#Loop Menu

#If USER selects Add New Contact:
def add_contact(contacts):
  fname = input("Enter your contacts First Name: ")
  lname = input("Enter your contacts Last Name: ")
  address = input("Enter your contacts Address: ")
  phnum = input("Enter your contacts phone number: ")
  email = input("Enter your contacts email: ")
  fbook = input("Enter your contacts Facebook: ")
  twit = input("Enter your contacts twitter: ")
  ig = input("Enter your contacts instagram: ")
  contact = [fname,lname,address,phnum,email,fbook,twit,ig]
  contacts.append(contact)
  write_contacts(contacts)
  print(f"Your new contacts {fname} {lname}, {address}, {phnum}, {email}, {fbook}, {twit}, {ig} was added\n")

#If USER selects View Existing Contact:
def view_contact(contacts):
  lname = input("Enter your contacts last name: ")
  with open(FILENAME, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      if lname in row:
        print(row)

#If USER selects Edit Existing Contact:

#If USER selects Delete Existing Contact (possibly better by phone number?):
def delete_contact(contacts):
  lname = input("Enter your contacts last name: ")
  with open(FILENAME,"r+") as r, open("output.csv","w") as f:
    #pass the file object to reader() to get the reader object
    reader = csv.reader(r)
    writer = csv.writer(f)
    # Iterate over each row in the csv using reader object
    for row in reader:
      # row variable is a list that represents a row in csv
      if row[0] == lname:
        print(f'{row} to be deleted')
        #show the line that will be deleted
      else:
        writer.writerow(row)
        
        os.remove(FILENAME)
        os.rename('output.csv', FILENAME)
        
  """with open(FILENAME,"w") as w:
    writer = csv.writer(w)
    for row in writer:
      if row[0] == lname:
        print(f'{row} will be deleted')
      else:
        print("Contact was not fount\n")
        writer.writerow(row)"""

#read contacts from file
def read_contacts():
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
    
#write contacts to file
def write_contacts(contacts):
  try:
    with open(FILENAME, "w", newline="") as file:
      writer = csv.writer(file)
      writer.writerows(contacts)
  except Exception as e:
    print(type(e), e)
    exit_program()

#If USER selects Exit:
	#Quit Program
def exit_program():
  print("Ending program")
  sys.exit()

#Provide a USER MENU of options
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
        add_contact(contacts)
    elif command.lower() == "view":
        view_contact(contacts)
    elif command.lower() == "edit":
        edit_contacts(contacts)
    elif command.lower() == "del":
        delete_contact(contacts)
    elif command.lower() == "exit":
        break
    else:
        print("Not a valid command. Please try again.\n")
print("Ending Program")