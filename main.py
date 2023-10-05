import socket
import signal
import sys
import threading
from time import sleep
import json
import webbrowser
from flask import Flask

# Define the server's IP address and port
HOST = '127.0.0.1' # IP address to bind to (localhost)
PORT = 8080 # Port to listen on
# Create a socket that uses IPv4 and TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the address and port
server_socket.bind((HOST, PORT))
# Listen for incoming connections
server_socket.listen(5) # Increased backlog for multiple simultaneous connections
print(f"Server is listening on {HOST}:{PORT}")
# Function to handle client requests
def handle_request(client_socket):
     # Receive and print the client's request data
     request_data = client_socket.recv(1024).decode('utf-8')
     print(f"Received Request:\n{request_data}")
     # Parse the request to get the HTTP method and path
     request_lines = request_data.split('\n')
     request_line = request_lines[0].strip().split()
     method = request_line[0]
     path = request_line[1]
     # Initialize the response content and status code
     response_content = ''
     status_code = 200
     # Define a simple routing mechanism
     producuts = [
  {
    "name" : "Fluent Python: Clear, Concise, and Effective Programming",
    "author" : "Luciano Ramalho",
    "price" : 39.95,
    "description" : "Don't waste time bending Python to fit patterns you've learned in other languages. Python's simplicity lets you become productive quickly, but often this means you aren't using everything the language has to offer. With the updated edition of this hands-on guide, you'll learn how to write effective, modern Python 3 code by leveraging its best ideas. "
  },
  {
    "name" : "Introducing Python: Modern Computing in Simple Packages",
    "author" : "Bill Lubanovic",
    "price" : 27.49,
    "description" : "Easy to understand and fun to read, this updated edition of Introducing Python is ideal for beginning programmers as well as those new to the language. Author Bill Lubanovic takes you from the basics to more involved and varied topics, mixing tutorials with cookbook-style code recipes to explain concepts in Python 3. End-of-chapter exercises help you practice what you’ve learned."
  }
]

     if path == '/':
          response_content = 'this is home page'
     elif path == '/about':
          response_content = 'This is the About page.'
     elif path == '/contacts':
          response_content = 'this is the contacts page'
     elif path == '/products':
          response_content = 'this is the products page'
     else:
          response_content = '404 Not Found'
          status_code = 404
          # Prepare the HTTP response
     response = f'HTTP/1.1 {status_code} OK\nContent-Type: text/html\n\n{response_content}'
     client_socket.send(response.encode('utf-8'))
     # Close the client socket
     client_socket.close()

# Function to handle Ctrl+C and other signals
def signal_handler(sig, frame):
     print("\nShutting down the server...")
     server_socket.close()
     sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)
while True:
     # Accept incoming client connections
     client_socket, client_address = server_socket.accept()
     print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
     # Create a thread to handle the client's request
     client_handler = threading.Thread(target=handle_request, args=(client_socket,))
     client_handler.start()

