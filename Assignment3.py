# Program Name: Assignment3.py 
# Course: IT3883/Section W01
# Student Name: Teraya Damm
# Assignment Number: Lab#3
# Due Date: 10/03/2025
# Purpose: The purpose of this program is to allow users to input a value to have converted from miles per gallon into kilometers per liter.
# List Specific resources used to complete the assignment. Module learning resources. 

#opening the tkinter module
from tkinter import *

#creating the conversation function
def Conversion(event=None):
  try:
    miles_input = int(entry.get())
    result = miles_input * 0.425143707
    result_label.config(text=f"{result} Kilometers per Liter")
  except ValueError:
    result_label.config(text="Invalid input. Please enter a number.")

#creating window
window = Tk()
window.title("Miles per Gallon into Kilometers per Liter Converter.")
window.geometry("400x400")

#creating attributes for the window
title_label = Label(window, text="Miles per Gallon into Kilometers per Liter Converter.")
input_label = Label(window, text="Enter integer value for Miles per Gallon:")
entry = Entry(window)
#printing the results 
result_label = Label(window, text="Result: ")

#packs
title_label.pack()
input_label.pack()
entry.pack()
result_label.pack()

entry.bind("<Return>", Conversion)

window.mainloop()
