import csv
import sys

FILENAME = "statement.csv"

#exiting the program
def exit_program():
  #If User selects Exit
  print("Ending program")
  #Quit program
  sys.exit()

#read transaction data from the csv file
def read_transactions():
#Place try/catch/except statement here for error issues
  try:
  	#here we are taking the variable 'transactions' and assigning it
    #the value of an empty list, a list containing no elements
    transactions = []
    #open the file we are working with. newline="\n" is needed for proper formatting
    with open(FILENAME, newline="\n") as file:
      #call .csv reader for import and export of spreadsheet data
      reader = csv.reader(file)
      #row in reader allows us to read and return data in the rows
      for row in reader:
        return transactions
  except FileNotFoundError:
    print(f"{FILENAME} file not found")
    exit_program()
  except Exception as e:
    print(type(e), e)
    exit_program()

#write transaction data to the csv file
def write_transactions(transactions):
#print transactions takes the data out of transactions memory and writes it into the .csv file
  print(transactions)
  #Place try/catch/except statement here for error issues
  try:
  	#open the file we are working with. newline="\n" is needed for proper formatting
    with open(FILENAME, "a", newline="\n") as file:
    #call .csv writer to be able to write data to the spreadsheet
      writer = csv.writer(file)
      #write the transaction to the row in the spreadsheet
      writer.writerow(transactions)
  except Exception as e:
    print(type(e), e)
    exit_program()

#add a transaction to csv file
def add_transactions():
  #User enters transaction date
  tdate = input("When was this transaction date? (yyyy-mm-dd): ")
  #User enters transaction location
  tloc = input("Where was this transaction completed?: ")
  #User enters transaction amount
  tamt = input("What was the transaction amount?: ")
  #New row is added (appended) to the .csv file containing the user added data
  newtransaction = [tdate, tloc, tamt,]
  #New row is added (appended) to the .csv file containing the user added data
  write_transactions(newtransaction)
  #confirmation is printed to User that data was added successfully
  print(f"New transaction {tdate} at {tloc} for {tamt} was added\n")
  #Loops back to Display Menu Command

#check the total of all entered transactions
def check_transactions():
#open the file we are working with.
  with open(FILENAME) as file:
      next(file)
      #this line sums the third row (row[2]) that contains all transaction amounts User has entered.
      total = sum(float(r[2]) for r in csv.reader(file))
      #line returns total amount for User
      print(total)
      #Loops back to Display Menu Command

def display_menu():
	#a simple display menu of commands for the User
    print("Bank balance program")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("LIST OF COMMANDS")
    print("check - Check current balance")
    print("add -  Add a Transaction")
    print("exit - Exit program")
    print()    

display_menu()
#display menu inputs. Each command entered directs which function is called:
while True:    
    command = input("Command: ")
    if command.lower() == "check":
        check_transactions()
    elif command.lower() == "add":
        add_transactions()
    elif command.lower() == "exit":
        break
    else:
        print("Not a valid command. Please try again.\n")
print("Ending Program")