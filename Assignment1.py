# Program Name: Assignment1.py 
# Course: IT3883/Section W01
# Student Name: Teraya Damm
# Assignment Number: Lab#1
# Due Date: 09/07/2025
# Purpose: This program gives the user 4 options of things to do. Three of those options include methods for the user to manipulate the data they input and the final option allows the user to exit the menu. 
# List Specific resources used to complete the assignment. n/a 

#creating the menu function
def menu():
  print("[1] Option 1: Append data to the input buffer")
  print("[2] Option 2: Clear the input buffer")
  print("[3] Option 3: Display the input buffer")
  print("[4] Option 4: Exit the program")

#initial call of the menu and creating the user choice value
menu()
choice = int(input("Enter your choice: "))

#creating the value to hold user input
Final_Input = str()

#creating the loop to run the menu
while choice != 4:
  if choice == 1:
    User_Input = input("Enter a string: ")
    if Final_Input:
      Final_Input += " " + User_Input
    else:
      Final_Input = User_Input
    menu() 
    choice = int(input("Enter your choice: "))
  elif choice == 2:
    Final_Input = ""
    menu() 
    choice = int(input("Enter your choice: "))
  elif choice == 3:
    print (Final_Input)
    menu() 
    choice = int(input("Enter your choice: "))
  else:
    print("Invalid choice.")
    menu() 
    choice = int(input("Enter your choice: "))





