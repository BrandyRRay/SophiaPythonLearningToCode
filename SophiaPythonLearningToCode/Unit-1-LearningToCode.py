#Unit 1: Learning to Code

print("Hello World")

#deliberate error
print('Hello World") 

#This code outputs Hello World 5 times
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")

#This code outputs Hello World 5 times
print("Hello World 1")
print("Hello World 2")
#print(Hello World 3)
print("Hello World 4")
print("Hello World 5")

#This is a way of having
#comments that span multiple
#lines of code so that you can
#add your notes without
#scrolling on one line.

def max_of_two( firstNumber, secondNumber ):
  if firstNumber > secondNumber:
    return firstNumber
  return secondNumber
def max_of_three( firstNumber, secondNumber, thirdNumber ):
  return max_of_two( firstNumber, max_of_two( secondNumber, thirdNumber ))
print(max_of_three(20, 30, -10))


#Author: Sophia
#Created Date: August, 21, 2021
#Description: This program has two functions to find the maximum
#value of three numbers.
#Example of usage: print(max_of_three(20, 30, -10))
#Result: function returns 30
#Function: max_of_two
#Purpose: This function accepts two numbers, compares them,
#and returns the value that is larger.
def max_of_two( firstNumber, secondNumber ):
  if firstNumber > secondNumber:
    return firstNumber
  return secondNumber
#Function: max_of_three
#Purpose: This function accepts three numbers and sends the second and third
#numbers to max_of_two. It then takes the result of that comparison to
#send the first number and the result to get the larger value
#of all three.
def max_of_three( firstNumber, secondNumber, thirdNumber ):
  return max_of_two( firstNumber, max_of_two( secondNumber, thirdNumber ) )
#Testing the function max_of_three
print(max_of_three(20, 30, -10))


#flawed program
score = int(input("What is your exam score (0-100): "))
if score > 90 and score < 100:
  print('You got an A! Congrats!')
elif score > 80 and score < 90:
  print('You got a B! Well done!')
elif score > 70 and score < 80:
  print('You got a C.')
else:
  print("You did not pass the exam.")


score = int(input("What is your exam score (0-100): "))
if score >= 90 and score <= 100:
  print('You got an A! Congrats!')
elif score >= 80 and score < 90:
  print('You got a B! Well done!')
elif score >= 70 and score < 80:
  print('You got a C.')
else:
  print("You did not pass the exam.")


#Tells you what type the variable is:
print(type("Hello World"))


#Assigns value to myVar and prints
myVar = 1
print(myVar)

#Assigns value to myVar and prints, then reassigns value and prints
myVar = 1
print(myVar)
myVar = 2
print(myVar)


myFirstInt = 100
mySecondInt = 0
myThirdInt = -999
myInt = 123456789123456789123456789123456789123456789123456789
print(myFirstInt, mySecondInt, myThirdInt, myInt)


myDecimalNum = 16
myBinaryNum = 0b10000
myOctNum = 0o20
myHexNum = 0x10

print("Decimal", myDecimalNum)
print("Binary", myBinaryNum)
print("Octal", myOctNum)
print("Hexadecimal", myHexNum)


myFirstFloat = 8.2
mySecondFloat = 0.0001
myThirdFloat = 192.12387

print(myFirstFloat, mySecondFloat, myThirdFloat)


x = 10
print(x + 17)


x = 10
result = x + 17
print(result)


myValue = 2
myValue = myValue + 2
print(myValue)


myValue = 2
myValue += 2
print(myValue)


myValue = 2
print(myValue)
myValue += 2
print(myValue)
myValue *= 2
print(myValue)
myValue -= 3
print(myValue)
myValue /= 2
print(myValue)


base = 10
exponent = 2
result = base ** exponent
print(result)


remainder = 7 % 3
print(remainder)


pizzaSlices = 20
remainingSlices = (pizzaSlices - 2) / 2
print(remainingSlices)

investment = 300
money = ((investment * 2/3) - 50) * 5
print(money)

investment = 300
profit = ((investment * 2/3) - 50) * 5 - investment
print(profit)


#myVar originally declared as an integer, then switched to a string:
myVar=1
print(myVar)
myVar="I am now a string"
print(myVar)


#Use a \ to successfully insert a ' or " in printed text:
myString1 = "Here's how to write a contraction"
print(myString1)
myString2 = 'It\'s working'
print(myString2)
myDirections = "When you've finished, press the \"submit\" button"
print(myDirections)


print("First Line.")
print("Second Line.")
print("Third Line.")
print("First Line.\nSecond Line.\nThird Line.")


myString1, myString2, myString3 = "Python", "is", "Fun"
print(myString1)
print(myString2)
print(myString3)


myString1 = myString2 = myString3 = "We're the same"
print(myString1)
print(myString2)
print(myString3)


myVar1 = 'Learning'
myVar2 = 'Python'
result = myVar1 + myVar2
print(result)
result = myVar1 + ' ' + myVar2
print(result)


myVar1 = 111
myVar2 = 222
result = myVar1 + myVar2
print(result)


myVar1 = '111'
myVar2 = '222'
result = myVar1 + myVar2
print(result)


myString = 'Python is great '
result = myString * 5
print(result)


myString = 'Python is great\n'
result = myString * 5
print(result)


stringToFind = 'some'
sentence = 'Python is quite a fun language to learn. There can be some great string functions to use.'
result = stringToFind in sentence
print(result)


stringToFind = 'grrr'
sentence = 'Python is quite a fun language to learn. There can be some great string functions to use.'
result = stringToFind in sentence
print(result)


#Three double quotes or three single quotes can sub for newline
outputString = """This is my first line
and now my second line
and lastly my last line."""
print(outputString)


myVar1 = 111
myVar2 = 222
result = str(myVar1) + str(myVar2)
print(result)


myVar1 = '111'
myVar2 = '222'
result = myVar1 + myVar2
print(result)


myVar1 = '111'
myVar2 = '222'
result = int(myVar1) + int(myVar2)
print(result)



#We are importing a module that we need to be able to generate random numbers
import random
#We are creating a random even number between 2 and 10 by
#first randomizing an integer between 1 and 5. This will be our
#final number. The number to add will take this final number and multiply it by 2.
randomFinalNumber = random.randrange(1, 5)
numberToAdd = randomFinalNumber * 2

#Asking the user to enter in their name
name = input("Hello! What is your name? ")

#Script to walk through each of the steps
print("Welcome " +name +", we’ll perform some mind reading on you.")
print("First, think of a number between 1 and 10.")
answer = input("Ready for the next step? ")
print("Multiply the result by 2.")
answer = input("Ready for the next step? ")
print("Now, add...let's see...")
print(numberToAdd)
answer = input("Ready for the next step?")
print("Now, divide the number you have by 2.")
answer = input("Ready for the next step? ")
print("Now, subtract the original number that you thought about.")
answer = input("Ready for the last step? ")

#Guessing the number
print("Well " +name +", let me read your mind...The number that you have right now is....")
print(randomFinalNumber)


#We are importing a module that we need to be able to generate random numbers
import random
#We are creating a random even number between 2 and 10 by
#first randomizing an integer between 1 and 5. This will be our
#final number. The number to add will take this final number and multiply it by 2.
randomFinalNumber = random.randrange(1, 5)
numberToAdd = randomFinalNumber * 2

#Asking the user to enter in their name
name = input("Hello! What is your name? ")

#Script to walk through each of the steps
print("Welcome " +name +", we’ll perform some mind reading on you.")
print("First, think of a number between 1 and 10.")
#enteredNumber = int(input("Enter in a number between 1 and 10: ")) 
print("Multiply the result by 2.")

#userNumber = enteredNumber * 2
#print(">> userNumber at this step = " + str(userNumber))
answer = input("Ready for the next step? ")
print("Now, add...let's see...")
print(numberToAdd)

#userNumber = userNumber + numberToAdd
#print(">> userNumber at this step = " + str(userNumber))
answer = input("Ready for the next step? ")
print("Now, divide the number have by 2.")
answer = input("Ready for the next step? ")

#userNumber = userNumber / 2
#print(">> userNumber at this step = " + str(userNumber))
print("Now, subtract the original number that you thought about.")
answer = input("Ready for the last step? ")

#Guessing the number
print("Well " +name +", let me read your mind...The number that you have right now is....")
print(randomFinalNumber)



#We are importing a module that we need to be able to generate random numbers
import random

#We are creating a random even number between 2 and 10 by
#first randomizing an integer between 1 and 5. This will be our
#final number. The number to add will take that and multiply it by 2.
randomFinalNumber = random.randrange(1, 5)
numberToAdd = randomFinalNumber * 2

#Asking the user to enter in their name
name = input("Hello! What is your name? ")

#Script to walk through each of the steps
print("Welcome " +name +", we’ll perform some mind-reading on you.")
print("First, think of a number between 1 and 10.")
print("Multiply the result by 2.")
answer = input("Ready for the next step? ")
print("Now, add...let's see...")
print(numberToAdd)
answer = input("Ready for the next step? ")
print("Now, divide the number have by 2.")
answer = input("Ready for the next step? ")
print("Now, subtract the original number that you thought about.")
answer = input("Ready for the last step? ")

#Guessing the number
print("Well " +name +", let me read your mind...The number that you have right now is....")
print(randomFinalNumber)

#Validating the results
enteredNumber = int(input(">> Enter in the number the individual guessed between 1 and 10: "))
userNumber = enteredNumber * 2
print(">> Muliplied by 2 = " + str(userNumber))
userNumber = userNumber + numberToAdd
print(">> Told to add "+ str(numberToAdd) + " = " + str(userNumber))
userNumber = userNumber / 2
print(">> Divided by 2 = " + str(userNumber))
userNumber = userNumber - enteredNumber
print(">> Subtracted the original number "+ str(enteredNumber) +" = " + str(userNumber))



#first we define the function definition by using the reserved keyword “def” to define it
#then set up the function myFunction with three parameters firstName, middleInitial, and lastName.
#to end a function, we place a colon at the end

def myFunction(firstName, middleInitial, lastName):

#finally we will print to screen so we can see it work
  print(firstName, middleInitial, lastName)

#here is where we call myFunction and pass it the actual values as arguments
myFunction("John", "R", "Doe")


myString = 'Python is fun!'
print(len(myString))


print(int(100))
print(int(2.95))
print(int("200"))


print(float(100))
print(float(2.95))
print(float("200"))


print(str(100))
print(str(2.95))
print(str("200"))


#first location of char
myString = 'Python is fun!'
print(myString.index("n"))

#first char to uppercase
outputString = 'I AM YELLING!'
print(outputString.capitalize())


#all char to lowercase
outputString = 'ThIs Is My TeSt StRiNg!'
print(outputString.lower())


#all char to uppercase
outputString = 'ThIs Is My TeSt StRiNg!'
print(outputString.upper())


#all char swap case to upper to lower
outputString = 'ThIs Is My TeSt StRiNg!'
print(outputString.swapcase())


#each word first letter is uppercase, all others to lower
outputString = 'ThIs Is My TeSt StRiNg!'
print(outputString.title())


#this is assigning variable temperature the integer 82
temperature = 82

#below is the if statement
if temperature > 0 : #this is the header line that ends with a “:”
  print('temperature is positive')  #this is the indented block
if temperature < 0 :
  pass #need to handle negative temperatures!!


#all elif statements
grade = 85
if grade > 90:
  print("you got an A")
elif grade >= 80:
  print("you got a B")
elif grade >= 70:
  print("you got a C")
elif grade >= 61:
  print("you got a D")
elif grade <= 60:
  print("you got an F")


#closing elif with else
grade = 85
if grade > 90:
  print("you got an A")
elif grade >= 80:
  print("you got a B")
elif grade >= 70:
  print("you got a C")
elif grade >= 61:
  print("you got a D")
else:
  print("you got an F")



temperature = -5
if temperature > 0:
  print("temperature is positive")
elif temperature == 0:
  print("temperature is 0")
else:
  print("temperature is negative")


num = 1
if num == 1:
  print('True')
else:
  print('False')


num = 1
if not (num == 1):
  print('True')
else:
  print('False')



num1 = 1
num2 = 2
if num1 == 0 and num2 == 0:
    print('A is False, B is False: True')
else:
    print('A is False, B is False: False')
 
if num1 == 0 and num2 == 2:
    print('A is False, B is True: True')
else:
    print('A is False, B is True: False')
 
if num1 == 1 and num2 == 0:
    print('A is True, B is False: True')
else:
    print('A is True, B is False: False')
 
if num1 == 1 and num2 == 2:
    print('A is True, B is True: True')
else:
    print('A is True, B is True: False')



num1 = 1
num2 = 2
if num1 == 0 or num2 == 0:
    print('A is False, B is False: True')
else:
    print('A is False, B is False: False')
 
if num1 == 0 or num2 == 2:
    print('A is False, B is True: True')
else:
    print('A is False, B is True: False')
 
if num1 == 1 or num2 == 0:
    print('A is True, B is False: True')
else:
    print('A is True, B is False: False')
 
if num1 == 1 or num2 == 2:
    print('A is True, B is True: True')
else:
    print('A is True, B is True: False')



a = 5
b = 15
c = 10
d = 0
if a > b:
 d = 4
elif b > c:
 d = 5
else:
 d = 6
print(d)



carSpeed = int(input("Enter in the car's speed between 0 and 200: "))
if carSpeed > 100:
    print("The car's speed is fast!")
elif carSpeed < 100:
    print("The car's speed is slow.")
else:
    print("The car's speed is exactly at 100.")



carSpeed = int(input("Enter in the car's speed between 0 and 200: "))
if carSpeed > 100:
    print("The car's speed is fast!")
else:
  if carSpeed < 100:
    print("The car's speed is slow.")
  else:
    print("The car's speed is exactly at 100.")


grade = 85
if grade > 90:
    print("You got an A")
else:
    if grade > 80:
        print("You got a B")
    else:
        if grade > 70:
            print("You got a C")
        else:
            if grade > 60:
                print("You got a D")
            else:
                if grade <= 60:
                    print("You got a F")


hungry = "y"
healthy = "y"
if hungry == "n":
    if healthy == "n":
      print("Not hungry.")
    else:
      print("Not hungry.")
else:
    if healthy == "n":
        print("Getting some junk food.")
    else:
        print("Getting a healthy meal.")


hungry = input("Are you hungry? Enter y if you are and n if you are not: ")
if hungry == "n":
    print("You are not hungry.")
else:
    healthy = input("Did you want a healthy meal? Enter y if you do and n if you do not: ")
    if healthy == "n":
        print("Getting some junk food.")
    else:
        print("Getting a healthy meal.")



inp = input('Enter Fahrenheit Temperature:')
try:
  fahr = float(inp)
  cel = (fahr - 32.0) * 5.0 / 9.0
  print(cel)
except:
  print('Oops, you did not enter in a number. Please enter a number next time.')




drinkDetails=""
drink = input('What type of drink would you like to order?\nWater\nCoffee\nTea\nEnter your choice: ')
if drink == "Water":
    drinkDetails=drink
    temperature = input("Would you like your water? Hot or Cold: ")
    if temperature == "Hot":
        drinkDetails += ", " + temperature
    elif temperature == "Cold":
        drinkDetails += ", " + temperature  
        ice = input("Would you like ice? Yes or No: ")
        if ice == "Yes":
            drinkDetails += ", Ice"
    else:
        drinkDetails += ", unknown temperature entered."
elif drink == "Coffee":
    drinkDetails=drink
    decaf = input("Would you like decaf? Yes or No: ")
    if decaf == "Yes":
        drinkDetails += ", Decaf"
    milkCream = input("Would you like Milk, Cream or None: ")
    if milkCream == "Milk":
        drinkDetails += ", Milk"
    elif milkCream == "Cream":
        drinkDetails += ", Cream"
    sugar = input("Would you like sugar? Yes or No: ")
    if sugar == "Yes":
        drinkDetails += ", Sugar"
elif drink == "Tea":
    drinkDetails=drink
    teaType = input("What type of tea would you like? Black or Green: ")
    if teaType == "Black":
        drinkDetails += ", " + teaType
    elif teaType == "Green":
        drinkDetails += ", " + teaType
else:
    print("Sorry, we did not have that drink available for you.")
print("Your drink selection: ",drinkDetails)


