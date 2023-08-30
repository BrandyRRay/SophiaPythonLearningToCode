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
  try:
    transactions = []
    #here we are taking the variable 'transactions' and assigning it
    #the value of an empty list, a list containing no elements
    with open(FILENAME, newline="") as file:
      #we have opened the file we are working with, as 'file'
      reader = csv.reader(file)
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
  try:
    #with open(FILENAME, "a") as file:
    with open(FILENAME, "a", newline="") as file:
      writer = csv.writer(file)
      #This is needed to put new data on new row, otherwise data is appended to already existing row
      file.write("\n")
      writer.writerows(transactions)
  except Exception as e:
    print(type(e), e)
    exit_program()

#add a transaction to csv file
def add_transactions(transactions):
  #User enters transaction date
  tdate = input("When was this transaction date? (yyyy-mm-dd): ")
  #User enters transaction location
  tloc = input("Where was this transaction completed?: ")
  #User enters transaction amount
  tamt = input("What was the transaction amount?: ")
  #New row is added (appended) to the .csv file containing the used added data
  newtransaction = [tdate, tloc, tamt,]
  transactions.append(newtransaction)
  write_transactions(transactions)
  print(f"New transaction {tdate} at {tloc} for {tamt} was added\n")
  #Loops back to Display Menu Command

#check the total of all entered transactions
def check_transactions(transactions):
  with open(FILENAME) as file:
      next(file)
      total = sum(float(r[2]) for r in csv.reader(file))
      print(total)

def display_menu():
    print("Bank balance program")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("LIST OF COMMANDS")
    print("check - Check current balance")
    print("add -  Add a Transaction")
    print("exit - Exit program")
    print()    

display_menu()
transactions = read_transactions()
while True:    
    command = input("Command: ")
    if command.lower() == "check":
        check_transactions(transactions)
    elif command.lower() == "add":
        add_transactions(transactions)
    elif command.lower() == "exit":
        break
    else:
        print("Not a valid command. Please try again.\n")
print("Ending Program")


###This works as of 08-01-2023 ; 10:20pm
###Need to fix, first added transaction is fine. Second added transaction adds the first as a duplicate and also adds a whiteline.
###Third added transaction adds the first and second as well as an additional whiteline.



#Loop Menu comments to place:
	#Place try/catch/except statement here
	#If User selects Check Current Balance
		#Open .csv {FILENAME} as read
		#Total row 2
		#Print total
		#Close {FILENAME}
		#Ask User if back to Menu or Exit
			#Loop back to Menu or
			#Exit