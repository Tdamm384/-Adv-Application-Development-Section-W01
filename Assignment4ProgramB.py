# Program Name: Assignment4.py/ProgramB.py
# Course: IT3883/Section W01
# Student Name: Teraya Damm
# Assignment Number: Lab#4
# Due Date: 10/26/2025
# Purpose: What does the program do (in a few sentences)? This program allows for a user to input a string and then the program will send it to another program and the second program prints the recieved string. 
# List Specific resources used to complete the assignment. Module reading/slides/lectures 


import socket 

#getting name/info of the host
host = socket.gethostname()
port = 9999

# Creating the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

#accepting, recieving, editing, and sending the message
Client_socket, addr = server_socket.accept()
message = Client_socket.recv(1024)
response = message.decode('ascii').upper()
Client_socket.send(response.encode('ascii'))

#closing everything
Client_socket.close()
server_socket.close()