# Program Name: Assignment4.py/ProgramA.py
# Course: IT3883/Section W01
# Student Name: Teraya Damm
# Assignment Number: Lab#4
# Due Date: 10/26/2025
# Purpose: What does the program do (in a few sentences)? This program allows for a user to input a string and then the program will send it to another program and the second program prints the recieved string. 
# List Specific resources used to complete the assignment. Module reading/slides/lectures



import socket

# Getting name/info of the host
host = socket.gethostname()
port = 9999

# Creating the client socket & connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect((host, port))

#allows for user to input a string and then sends it to the server
text = input("Enter a string: ")
client_socket.send(text.encode('ascii')) 

# receiving response from server
message = client_socket.recv(1024)
print('Received from server: ' + message.decode('ascii'))

#closing the socket
client_socket. close()