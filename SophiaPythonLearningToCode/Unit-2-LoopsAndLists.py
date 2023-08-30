#Unit 2: Lists and Loops


pythonList = ['Ford', 10, 'Chevrolet', -4.5]

parkingLot = ['motorcycle', '', 'truck', 'car', 'car']

petsList = ['dog', 'cat', 'fish']
numbersList = [17, 123]
emptyList = []


petsList = ['dog', 'cat', 'fish']
print(petsList[0])


numbersList = [17, 123]
numbersList[1] = 5
print(numbersList)


petsList = ['dog', 'cat', 'fish']
print(petsList[5-4])


petsList = ['dog', 'cat', 'fish']
print(petsList[-1])


my_first_list = ['a', 'b', 'c']
my_second_list = ['d', 'e', 'f', 'g']
my_third_list = my_first_list + my_second_list
my_third_list.extend('h')
print (my_third_list[1:5])


my_first_list = ['a', 'b', 'c']
my_second_list = ['d', 'e', 'f', 'g']
my_third_list = my_first_list * 3
my_third_list.extend('h')
print (my_third_list[5:])


petsList = ['dog', 'cat', 'fish']
print('dog' in petsList)
print('monkey' in petsList)


petsList = ['dog', 'cat', 'fish']
petsList[1] = 'hamster'
print(petsList)


firstList = [1, 2, 3]
secondList = [4, 5, 6]
thirdList = firstList + secondList
print(thirdList)


petsList = ['dog', 'cat', 'fish']
resultList = petsList * 3
print(resultList)


#Important to remember that for slice count starts at 0 and does not include final number
#this result is ['cat', 'fish'] (index numbers 1 & 2)
petsList = ['dog', 'cat', 'fish','rabbit','hamster','bird']
petSlice = petsList[1:3]
print(petSlice)



petsList = ['dog', 'cat', 'fish','rabbit','hamster','bird']
petSlice = petsList[:3]
print(petSlice)
#returns  ['dog', 'cat', 'fish'] 


petsList = ['dog', 'cat', 'fish','rabbit','hamster','bird']
petSlice = petsList[3:]
print(petSlice)
#returns ['rabbit','hamster','bird']


petsList = ['dog', 'cat', 'fish','rabbit','hamster','bird']
petSlice = petsList[:]
print(petSlice)
#returns ['dog', 'cat', 'fish','rabbit','hamster','bird']


petsList = ['dog', 'cat', 'fish','rabbit','hamster','bird']
petsList[1:3] = ['dinosaur','robot']
print(petsList)


petsList = ['dog', 'cat', 'fish','rabbit','hamster','bird']
petsList.append('dinosaur')
print(petsList)



petsList = ['dog', 'cat', 'fish','rabbit','hamster','bird']
petsList.insert(3,'dinosaur')
print(petsList)


firstPetsList = ['dog', 'cat', 'fish']
secondPetsList = ['rabbit','hamster']
firstPetsList.extend(secondPetsList)
print(firstPetsList)


petsList = ['dog', 'cat', 'fish','rabbit','hamster','bird']
petsList.sort()
print(petsList)


numList = [2, 45, 9, 17, 1, 2]
numList.sort()
print(numList)


petsList = ['dog', 'cat', 'fish', 'rabbit','hamster','bird']
removedPet = petsList.pop(3)
print('remaining: ', petsList)
print('removed: ', removedPet)



petsList = ['dog', 'cat', 'fish', 'rabbit','hamster','bird']
removedPet = petsList.pop()
print("Remaining: ", petsList)
print("Removed: ", removedPet)
#removes last item in list: 'bird'


petsList = ['dog', 'cat', 'fish', 'rabbit','hamster','bird']
del petsList[3]
print("Remaining: ", petsList)


petsList = ['dog', 'cat', 'fish', 'rabbit','hamster','bird']
petsList.remove('rabbit')
print("Remaining: ", petsList)


petsList = ['dog', 'cat', 'fish', 'rabbit','cat','bird']
petsList.remove('cat')
print("Remaining: ", petsList)


numList = [2, 45, 9, 17, 1, 4]
print("Max: ",max(numList))
print("Min: ",min(numList))
print("Length: ",len(numList))
print("Sum: ",sum(numList))
print("Average: ",sum(numList)/len(numList))


numList = [2, 45, 9, 17, 1, 4]
listElement = iter(numList)
print(next(listElement))
print(next(listElement))
print(next(listElement))
print(next(listElement))
print(next(listElement))
print(next(listElement))


myString = "sophia"
listElement = iter(myString)
print(next(listElement))
print(next(listElement))
print(next(listElement))
print(next(listElement))
print(next(listElement))
print(next(listElement))


myList = ["apple","pear","banana"] #use square brackets
mySet = {"apple","pear","banana"} #use curly braces
myTuple = ("apple","pear","banana") #use parenths
myDict = {'apple': 'red', 'pear': 'green', 'banana': 'yellow'} #use curly praces AND colons


mySet = {"fun","sun","run"}
print(mySet)


mySet = {"fun","sun","run","fun"}
print(mySet) #won't print the second 'fun'


mySet = {"fun","sun","run"}
mySet.add("bun")
print(mySet)


myPets = {"dog","cat","rabbit"}
yourPets = {"lion","tiger","bear"}
myPets.update(yourPets)
print(myPets)


myPets = {"dog","cat","rabbit"} #this is the set
yourPets = ["dog","dog","fish"] #this is the list
myPets.update(yourPets)
print(myPets) 


myPets = {"dog","cat","rabbit"}
myPets.remove("dog")
print(myPets)


myPets = {"dog","cat","rabbit"}
myPets.discard("dog")
print(myPets)
myPets.discard("dinosaur")
print(myPets)



myTuple = ("ice cream","frozen yogurt","sorbet")
print(myTuple)


lonelyTuple = ("ice cream")
print(lonelyTuple)
print(type(lonelyTuple))

lonelyTuple = ("ice cream",)
print(lonelyTuple)
print(type(lonelyTuple))


myTuple = ("fun",10,-2.0,"sun")
print(myTuple)
print(type(myTuple))


myTuple = ("ice cream","frozen yogurt","sorbet")
print(myTuple[0])


myTuple = ("ice cream","frozen yogurt","sorbet")
print(myTuple[-1])


#workaround: convert to a list, add element, convert back to tuple
myTuple = ("ice cream","frozen yogurt","sorbet")
myList = list(myTuple)
myList[1] = "gelato"
myTuple = tuple(myList)
print(myTuple)


eng2span = dict()
eng2span = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2span)
print(eng2span['two'])


myPets = {'caine': 'dog', 'feline': 'cat', 'primate' : 'monkey'}
print (len(myPets))


eng2span = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
myVals = list(eng2span.values())
print ('uno' in myVals)


multiplesList = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
print(multiplesList)

multiplesList = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
print(multiplesList[0])

multiplesList = [[1, 2, 3, 4, 5], 
[2, 4, 6, 8, 10], 
[3, 6, 9, 12, 15], 
[4, 8, 12, 16, 20]]
print(multiplesList[0][2])


multiplesList = [[1, 2, 3, 4, 5], 
                 [2, 4, 6, 8, 10], 
                 [3, 6, 9, 12, 15], 
                 [4, 8, 12, 16, 20]]
print(multiplesList[2][3])
print(multiplesList[3][2])


multiplesList = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
multiplesList.append([5, 10, 15, 20, 25])
print(multiplesList)


multiplesList = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
multiplesList[0].append(6)
print(multiplesList)


multiplesList = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
multiplesList[0].append([6, 7, 8])
print(multiplesList)


multiplesList = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
multiplesList[0].extend([6, 7, 8])
print(multiplesList)


myString = " Fun things for Us "
myString = myString.strip()
print(myString)


myFirstList = ["ice cream","frozen yogurt","sorbet"]
myElement = "gelato"
#each test line goes here…
#myFirstList.append(myElement) - works
#myFirstList = myFirstList + [myElement] - works
#myFirstList.append([myElement]) - adds as list
#myFirstList = myFirstList.append(myElement) - does not work
#myFirstList + [myElement] - only original list
#myFirstList = myFirstList + myElement - error, only works on strings
print(myFirstList)


myFirstList = ["ice cream","frozen yogurt","sorbet"]
anotherList = myFirstList[:]
anotherList.sort()
print(anotherList)
print(myFirstList)


#Tic-Tac-Toe, row & col starts at 0:
board = [ ["-", "-", "-"],
		["-", "-", "-"],
		["-", "-", "-"] ]

col = int(input("X player, select a column: "))
row = int(input("X player, select a row: "))
 
board[row][col] = "X"
print(board[0])
print(board[1])
print(board[2])


#Tic-Tac-Toe, row & col starts at 1:
#the following code creates the board
board = [ ["-", "-", "-"],
          ["-", "-", "-"],
          ["-", "-", "-"] ]
 
print(board[0])
print(board[1])
print(board[2])
 
#this is player X’s first move
col = int(input("X player, select a column 1-3: "))
row = int(input("X player, select a row 1-3: "))
col -= 1
row -= 1
 
board[row][col] = "X"
print(board[0])
print(board[1])
print(board[2])
 
#this is player O’s first move
col = int(input("O player, select a column 1-3: "))
row = int(input("O player, select a row 1-3: "))
col -= 1
row -= 1
 
if board[row][col] == '-':
  board[row][col] = "O"
else:
  print("Oops, that spot was already taken. ")
print(board[0])
print(board[1])
print(board[2])
 
#this is player X’s second move
col = int(input("X player, select a column 1-3: "))
row = int(input("X player, select a row 1-3: "))
col -= 1
row -= 1
 
if board[row][col] == '-':
  board[row][col] = "X"
else:
  print("Oops, that spot was already taken. ")
print(board[0])
print(board[1])
print(board[2])
 
#this is player O’s second move
col = int(input("O player, select a column 1-3: "))
row = int(input("O player, select a row 1-3: "))
col -= 1
row -= 1
 
if board[row][col] == '-':
  board[row][col] = "O"
else:
  print("Oops, that spot was already taken. ")
print(board[0])
print(board[1])
print(board[2])
 
#this is player X’s third move
col = int(input("X player, select a column 1-3: "))
row = int(input("X player, select a row 1-3: "))
col -= 1
row -= 1
 
if board[row][col] == '-':
  board[row][col] = "X"
else:
  print("Oops, that spot was already taken. ")
print(board[0])
print(board[1])
print(board[2])
 
#this is player O’s third move
col = int(input("O player, select a column 1-3: "))
row = int(input("O player, select a row 1-3: "))
col -= 1
row -= 1
 
if board[row][col] == '-':
  board[row][col] = "O"
else:
  print("Oops, that spot was already taken. ")
print(board[0])
print(board[1])
print(board[2])
 
#this is player X’s fourth move
col = int(input("X player, select a column 1-3: "))
row = int(input("X player, select a row 1-3: "))
col -= 1
row -= 1
 
if board[row][col] == '-':
  board[row][col] = "X"
else:
  print("Oops, that spot was already taken. ")
print(board[0])
print(board[1])
print(board[2])
 
#this is player O’s fourth move
col = int(input("O player, select a column 1-3: "))
row = int(input("O player, select a row 1-3: "))
col -= 1
row -= 1
 
if board[row][col] == '-':
  board[row][col] = "O"
else:
  print("Oops, that spot was already taken. ")
print(board[0])
print(board[1])
print(board[2])
 
#this is player X’s fifth move
col = int(input("X player, select a column 1-3: "))
row = int(input("X player, select a row 1-3: "))
col -= 1
row -= 1
 
if board[row][col] == '-':
  board[row][col] = "X"
else:
  print("Oops, that spot was already taken. ")
print(board[0])
print(board[1])
print(board[2])



myNum = 5 
while myNum > 0:
     myNum = myNum - 1
     print(myNum)
print("Our loop is done")


myNum = 0
while myNum > 0:
     myNum = myNum - 1
     print(myNum)
print("Our loop did nothing")


productList = ("card", "paper", "glue", "pencil")
for product in productList:
  print(product)


for counter in range(0,5):
    print("Counter is set to:",counter)


for counter in range(5):
   print("Counter is set to:",counter)


for counter in range(1,5):
   print("Counter is set to:",counter)


for counter in range(-2,3):
    print("Counter is set to:",counter)


for counter in range(10,1,-2):
    print("Counter is set to:",counter) #counts down by 2's


for char in "Python":
   print(char)


for pet in ("dog","cat","fish"):
  print(pet)


myNumber = 6
while myNumber > 0:
    myNumber = myNumber - 1
    print(myNumber)
print('Blastoff!')


textEntered = ""
stringBuilder = ""
while textEntered != "quit":
  textEntered = input("Enter in a string, enter quit to exit the loop:")
  if textEntered != "quit":
    stringBuilder += textEntered + " "
print(stringBuilder)


myNumber = 6
while myNumber > 0:
    myNumber = myNumber - 1
    if myNumber == 2:
        break
    print(myNumber)
print('Blastoff!')



myNumber = 6
while myNumber > 0:
    myNumber = myNumber - 1
    if myNumber == 2:
        continue
    print(myNumber)
print('Blastoff!')


myNumber = 6
while myNumber > 0:
   myNumber = myNumber - 1
   if myNumber == 2:
       break
   print(myNumber)
else:
 print('Blastoff!')


myNumber = 6
while myNumber > 0:
   myNumber = myNumber - 1
   print(myNumber)
else:
 print('Blastoff!')


friendsList = ['Joseph', 'Glenn', 'Sally']
for friend in friendsList:
    print('Happy New Year:', friend)
print('Done!')


friendsList = ['Joseph', 'Glenn', 'Sally']
for foo in friendsList:
    print('Happy New Year:', foo)
print('Done!')


countItems = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    countItems = countItems + 1
print('Count: ', countItems)


totalItems = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    totalItems = totalItems + itervar
print('Total: ', totalItems)


largestValue = None
print('Before', largestValue)
for itervar in [3, 41, 12, 74, 15]:
  if largestValue is None or itervar > largestValue :
    largestValue = itervar
  print('Loop: ', itervar, largestValue)
print('Largest: ', largestValue)


smallestValue = None
print('Before', smallestValue)
for itervar in [3, 41, 12, 74, 15]:
  if smallestValue is None or itervar < smallestValue :
    smallestValue = itervar
  print('Loop: ', itervar, smallestValue)
print('Smallest: ', smallestValue)



numberToFind = 12
for itervar in [3, 41, 12, 9, 74, 15]:
   if itervar == numberToFind:
       print('Number found!')
       break
else:
 print('Number not found.')


multiples = []
for outer in range(1,5):
  multiples.append([])
  for inner in range(1,6):
    print("Outer: ",outer, ", Inner: ", inner, "Outer x inner: ",inner * outer)
    multiples[outer-1].append( outer * inner)
print(multiples)


multiples = []
for outer in range(1,5):
  multiples.append([])
  for inner in range(1,6):
    multiples[outer-1].append( outer * inner)
print(multiples)

for outerList in multiples:
  for innerValue in outerList:
    print (innerValue," ",end ='')
  print()



multiples = []
for outer in range(1,4):
  multiples.append([])
  for inner in range(1,4):
    multiples[outer-1].append( outer * inner)
print(multiples)

for outerList in multiples:
  for innerValue in outerList:
    print (innerValue," ",end ='')
  print()


multiples = []
for outer in range(1,11):
  multiples.append([])
  for inner in range(1,11):
    multiples[outer-1].append( outer * inner)
print(multiples)

for outerList in multiples:
  for innerValue in outerList:
    print (innerValue," ",end ='')
  print()


board = [ ["-", "-", "-"],
          ["-", "-", "-"],
          ["-", "-", "-"] ]
 
print(board[0])
print(board[1])
print(board[2])
col=0
row=0
playerTurn = "X"

for counter in range(1,10):

    validMove = False #setting the validMove variable to False
    while (validMove == False): #while loop checking the validMove variable
      col=0
      row=0
      while (col < 1 or col > 3):
        col = int(input(playerTurn + " player, select a column 1-3: "))
        if (col < 1 or col > 3):
          print("The column must be between 1 and 3.")
      while (row < 1 or row > 3):
        row = int(input(playerTurn + " player, select a row 1-3: "))
        if (row < 1 or row > 3):
          print("The row must be between 1 and 3.")
      col -= 1
      row -= 1
      if board[row][col] == '-':
        board[row][col] = playerTurn
        validMove=True; #setting validMove to True to exit loop
      else:
        print("Oops, that spot was already taken. Please select another spot.")
 
    print(board[0])
    print(board[1])
    print(board[2])
 
    if playerTurn =="X":
      playerTurn="O"
    else:
      playerTurn="X"


def print_stuff(comment):
    print("#######################")
    print(comment)
    print("#######################")

myVar = "My comment section"
print_stuff(myVar)


def display_add_two_num(val1, val2):
    print(val1,"+",val2, "=", val1+val2)

display_add_two_num(2, 4)
display_add_two_num(3, 8)


def display_add_four_num(val1, val2, val3, val4):
    print(val1,"+",val2,"+",val3,"+",val4, "=", val1+val2+val3+val4)

display_add_four_num(2, 4, 3, 8)


def return_one_hundred():
    return 100
    
something = return_one_hundred();
print(something)
print(type(something))


def return_one_hundred():
    return 100
    
print(return_one_hundred())
print(return_one_hundred() + return_one_hundred())
print(return_one_hundred() * 5)


print("Average: ",sum([2, 45, 9, 17, 1, 4])/len([2, 45, 9, 17, 1, 4]))


def calculate_average(numbers):
  return sum(numbers)/len(numbers)

print(calculate_average([10, 20, 30, 40]))


def calculate_average(numbers):
 my_avg = sum(numbers)/len(numbers)
 return my_avg

print(calculate_average([1,2,3,4]))


def calculate_multiple(numbers):
  return sum(numbers), len(numbers), sum(numbers)/len(numbers) 

print(calculate_multiple([10, 20, 30, 40]))


print(divmod(21, 5)) #divmod returns result and remainder
print(divmod(15, 5))


def calculate_absolute(number):
  if number > 0:
    return number
  elif number < 0:
    return -number #this is taking a negative number and turning it into a positive number
  else:
    return 0

print(calculate_absolute(-5))
print(calculate_absolute(5))
print(calculate_absolute(0))


def calculate_absolute(number):
  if number >= 0:
    return number
  else:
    return -number 

print(calculate_absolute(-5))
print(calculate_absolute(5))
print(calculate_absolute(0))


def calculate_absolute(number):
  if number >= 0:
    return number
  return -number 

print(calculate_absolute(-5))
print(calculate_absolute(5))
print(calculate_absolute(0))


def outer_func(what):
  def inner_func():
    print("I like", what)
  inner_func()

outer_func("Python")


def countdown(n):
  print(n)
  if n == 0:
    return
  else:
    countdown(n - 1)

countdown(15)


def factorial(number):
  if not isinstance(number, int):
    raise TypeError("Sorry, number must be an integer")
  if number < 0:
    raise ValueError("Sorry, number must be 0 or positive")
  def inner_factorial(number):
    if number <= 1:
      return 1
    return number * inner_factorial(number - 1)
  return inner_factorial(number)

print(factorial(4))


def function_4(num):
   if num > 1:
      num = num - 2
   else:
      num = num + 2
   return num
 
def function_3(num):
   if num > 1:
      num = num / 2
   else:
      num = num / -2
   return num

def function_2(num):
   if num > 1:
      num = num * 2
      num = function_3(num)
   else:
      num = num * -2
      num = function_4(num)
   return num

def function_1(num):
   if num > 0:
      num += 1
      num = function_2(function_3(num))
   else:
      num -=1
      num = function_2(function_4(num))
   return num
 
print('output = ', function_1(-9))



def priceInformation(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')

priceInformation(12, 'strawberries', 5.99)


def priceInformation(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')

priceInformation(price=5.99, item='strawberries', qty=12)


#tic-tac-toe working board:
board = [ ["-", "-", "-"],
          ["-", "-", "-"],
          ["-", "-", "-"] ]
 
#printing the board
def printBoard(board):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[0][0], board[0][1], board[0][2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[1][0], board[1][1], board[1][2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[2][0], board[2][1], board[2][2]))
    print("\t     |     |")
    print("\n")
 
def checkWinner(currPlayer, board):
  #Checking for the winner in the row
  for row in range(0,3):
    if board[row][0]==board[row][1]==board[row][2] and board[row][0] != '-':
      if board[row][0]==currPlayer:
        print("{} is winner".format(currPlayer))
        return True
  #used to check the winner in column
  for col in range(0,3):
    if board[0][col]==board[1][col]==board[2][col] and board[0][col] != '-':
      if board[0][col]==currPlayer:
        print("{} is winner".format(currPlayer))
        return True
  #used to check winner in one diagonal
  if board[0][0]==board[1][1]==board[2][2] and board[0][0] !='-':
    if board[0][0]==currPlayer:
      print("{} is winner".format(currPlayer))
      return True
  #used to check winner in another diagonal
  if board[0][2]==board[1][1]==board[2][0] and board[0][2]!='-':
    if board[0][2]==currPlayer:
      print("{} is winner".format(currPlayer))
      return True
  return False
 
printBoard(board)
col=0
row=0
playerTurn = "X"
 
for counter in range(1,10):
    validMove = False
    while (validMove == False):
      col=0
      row=0
      while (col < 1 or col > 3):
        col = int(input(playerTurn + " player, select a column 1-3: "))
        if (col < 1 or col > 3):
          print("The column must be between 1 and 3.")
      while (row < 1 or row > 3):
        row = int(input(playerTurn + " player, select a row 1-3: "))
        if (row < 1 or row > 3):
          print("The row must be between 1 and 3.")
      col -= 1
      row -= 1
      if board[row][col] == '-':
        board[row][col] = playerTurn
        validMove=True;
      else:
        print("Oops, that spot was already taken. Please select another spot.")
        validMove=False
        row=0
        col=0
 
    printBoard(board)
    if (checkWinner(playerTurn,board)):
      break
 
    if playerTurn =="X":
      playerTurn="O"
    else:
      playerTurn="X"


