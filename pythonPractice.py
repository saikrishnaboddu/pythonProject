# #Use Thonny - https://thonny.org/ to debug (pref a line of code)
# #Use askpython.com fo quick reference
# # Day 1 - print , input and variables

# greeting = print("Hello " + input("Enter your name: ") + " !")
# print( len( input("Enter your name: ")))
# a = 123_456.789
# print( type(a))

# # Day 2 - type conversion and f-strings

# # round is round(8/5) --> gives 1.6
# # floor is (8//5) --> gives 1
# roundExample = round(8/5, 2)
# floorExample = 8//5
# print(roundExample, floorExample)
# #f-string
# score = 9
# print(f"your score is {score}")

# #Life in weeks
# age = int(input("What is your current age: "))
# maxAge = 90
# remainingYears = 90 - age
# print(f"You have {remainingYears*365} days, {remainingYears*52} weeks, and {remainingYears*12} months left.")

# #Split Calculator
# print("Welcome to Tip Calculator")
# totalBill = float( input("What was the total bill? $"))
# tip = float( input("What percentage of tip would you like to give? 10, 12, or 15? "))
# numberOfPeople = float( input("How many people to split the bill? "))
# splitValue = ((totalBill * (tip/100)) + totalBill)/numberOfPeople 
# print(f"Each person should pay: ${splitValue}")

# # Day 3 - conditionals and logical operators

# #Leap year
# year = int( input("Which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Is a leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Is a leap year")
# else:
#     print("Not a leap year")

# # Pizza Order
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
# if size == "s":
#     bill += 15
# elif size == "m":
#     bill += 20
# else:
#     bill += 25
# if add_pepperoni == "y" and size == "s":
#     bill += 2
# elif add_pepperoni == "y" and (size == "m" or "l"):
#     bill +=3
# if extra_cheese == "y":
#     bill += 1
# print(f"Your final bill is {bill}")

# # Love Calculator
# # string.count("key") gives the number of occurances of a character(key in this case) in a string. Note: This is case-sensitive
# # Eg: "Mississipi".count("i") ---> returns 4
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# codeWord1 = "TRUE"
# codeWord2 = "LOVE"
# digit1 = 0
# digit2 = 0
# for code in codeWord1:
#     for alphabets in name1:
#         if alphabets.upper() == code:
#             digit1 += 1
#     for alphabets in name2:
#         if alphabets.upper() == code:
#             digit1 += 1
# for code in codeWord2:
#     for alphabets in name1:
#         if alphabets.upper() == code:
#             digit2 += 1
#     for alphabets in name2:
#         if alphabets.upper() == code:
#             digit2 += 1
# totalLove = (digit1*10)+digit2
# if totalLove < 10 or totalLove > 90:
#     print(f"Your score is {totalLove}, you go together like coke and mentos.")
# elif totalLove > 40 and totalLove < 50:
#      print(f"Your score is {totalLove}, you are alright together.")
# else:
#      print(f"Your score is {totalLove}.")

# #Treasure Island
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# choice1 = input("You're at a cross-road. Where do you want to go? Type \"left\" or \"right\" \n").lower()
# if choice1 == "left":
#     choice2 = input("You came to a lake and there's an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim accross \n").lower()
#     if choice2 == "wait":
#         choice3 = input("You arrive at the island unharmed. There are three doors infront of you \"red\", \"yellow\", and \"blue\". Which door do you ant to enter? \n").lower()
#         if choice3 == "red":
#             print("Burned by fire \n\t Game-Over")
#         elif choice3 == "blue":
#             print("Eaten by beasts\n\tGame-Over")
#         elif choice3 == "yellow":
#             print("You win")
#         else:
#             print("Game-Over")
#     else:
#         print("You were attacked by trout! \n \t Game-Over")
# else:
#     print("You fell into a hole!\n\t Game-Over")

# # Day 4 randomsation and lists

# #Heads-tails
# import random
# toss = random.randint(0,1)
# toss = random.random()
# print(toss)

# #Banking roulette
# import random
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# print(f"{names[random.randint(0, (len(names)-1))]} is going to buy the meal today!")

# #Treasure Map
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# map[int(position[1])-1][int(position[0])-1] = "X"
# print(f"{row1}\n{row2}\n{row3}")

# #Rock-Paper-Scissors
# import random
# rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """

# paper = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# scissors = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """

# choices = [rock, paper, scissors]

# userChoice = choices[int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissors\n"))]
# print(userChoice)
# compChoice = choices[random.randint(0, len(choices)-1)]
# print(f"Computer chose:\n{compChoice}")
# if userChoice == rock:
#     if compChoice == paper:
#         print("You Lose!")
#     elif compChoice == scissors:
#         print("You Win!")
#     else:
#         print("Draw")
# if userChoice == paper:
#     if compChoice == scissors:
#         print("You Lose!")
#     elif compChoice == rock:
#         print("You Win!")
#     else:
#         print("Draw")
# if userChoice == scissors:
#     if compChoice == paper:
#         print("You Win!")
#     elif compChoice == rock:
#         print("You Lose!")
#     else:
#         print("Draw")
