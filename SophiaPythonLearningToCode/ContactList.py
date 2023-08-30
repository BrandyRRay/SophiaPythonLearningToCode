#an already working contact list:
import csv

# Creating a menu view
def showMenu():
  print("Welcome to Contact Books. What do you want to do?")
  print("1. View contact")
  print("2. Change contact")
  print("3. Add contact")
  print("4. Delete contact")
  print("5. Exit")
  selectMenu()

def selectMenu():
  repeat = True
  while repeat == True:
    try:
      option = int(input("Choose[1-5]: "))
    except ValueError:
      print("Please input number.")
      # fill the option with 0 so the application won't error
      option = 0
    if option > 0 and option < 6: repeat = False
    if option == 1:
      #showContacts()
      #showMenu()
      print("1 selected")
    elif option == 2:
      print("\n==============")
      print("Change Contact")
      print("==============")
      #updateContact()
      #showMenu()
    elif option == 3:
      print("\n===========")
      print("Add Contact")
      print("===========")
      #addContact()
       #showMenu()
    elif option == 4:
      #deleteContact()
      #showMenu()
      print("4 selected")
    elif option == 5:
      print("Good bye!")
      break
    else: 
      print("Option unavailable.")
        
showMenu()

file=open("contacts.csv", 'w')
g=int(input("How many contacts do you want to save?"))

writer=csv.writer(file)
writer.writerow(fields) #ERRORS OUT AT THIS LINE HERE - VARIABLE 'FIELDS' NOT DEFINED

for i in range(0,g):
    name=input("Enter Contact Name:")
    number=input("Enter Contact No.:")
    a=[]
    a.append(name)
    a.append(number)
    writer.writerow(a)
   
file.close()


#How to create new csv from original csv:
import csv

with open("demo_csv.csv", mode="r") as old_file:
    reader_obj = csv.reader(old_file) #read the current csv file

    with open("new_demo_csv.csv", mode="w") as new_file:
        writer_obj = csv.writer(new_file, delimiter="-") # Writes to the new CSV file 

        for data in reader_obj:
            #loop through the read data and write each row in new_demo_csv.csv
            writer_obj.writerow(data)