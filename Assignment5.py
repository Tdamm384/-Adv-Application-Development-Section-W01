# Program Name: Assignment5.py
# Course: IT3883/Section W01
# Student Name: Teraya Damm
# Assignment Number: Lab#5
# Due Date: 11/16/ 2025
# Purpose: What does the program do (in a few sentences)? The purpose of this program is to create a program and SQL database that allows the program to read the accompanying text file and present the desired results. 
# List Specific resources used to complete the assignment.


import sqlite3

#creating the database
conn = sqlite3.connect('Assignment5.db')
cur = conn.cursor()

#creating the table and fields
cur.execute("""
CREATE TABLE IF NOT EXISTS WEATHER (
    ID INTEGER PRIMARY KEY,
    Day_of_Week TEXT,
    Temperature_Value REAL
)
""")

#reading the text file and seperating the data
with open('Assignment5input.txt', 'r') as file:
   for line in file:
     Day, Temp = line.split()
     cur.execute("INSERT INTO WEATHER (Day_of_Week, Temperature_Value) VALUES (?, ?)", (Day, float(Temp)))
#commiting the changes     
conn.commit()

#finding the average for sunday
cur.execute("SELECT AVG (Temperature_Value) FROM WEATHER WHERE Day_of_Week = 'Sunday'")
Sunday_Avg = cur.fetchone()[0]

#finding the average for thursday
cur.execute("SELECT AVG (Temperature_Value) FROM WEATHER WHERE Day_of_Week = 'Thursday'")
Thursday_Avg = cur.fetchone()[0]


#printing the results
print("The average temperature on Sunday is: ", Sunday_Avg)
print("The average temperature on Thursday is: ", Thursday_Avg)


#closing 
conn.close()