# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Teraya Damm
# Assignment Number: Lab#2
# Due Date: 09/19/2025
# Purpose: What does the program do (in a few sentences)? This program opens a file containing student data. The data is then split and organized into a list. Each student and their average is then displayed from the highest grade to lowest.
# Resources: module slides and lectures 

#preparing the list
Students = []

#reading the file
with open("Assignment2input.txt", 'r') as file_object:
  for line in file_object:
    #splitting the data into a list
    Part = line.strip().split()
    Name = Part[0]
    Scores = []
    for grade in Part[1:]:
      Scores.append(int(grade))
    #calculating the averages   
    Average = sum(Scores)/len(Scores)
    Students.append([Name, Average])

#sorting the students by average
def get_average(Student):
  return Student[1]
Students.sort(key=get_average, reverse=True)

#printing the students and their averages
for name, average in Students:
  print(f'{name}: {average:.2f}')





