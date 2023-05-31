import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = 'localhost'
port = 7777

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(2)

print('Waiting for Player 1 to enter the word and hint...')

# Accept the connection from Player 1
player1_socket, player1_address = server_socket.accept()

# Receive the word and hint from Player 1
data = player1_socket.recv(1024).decode()
word, hint = data.split(',')

print('Player 1 has entered the word and hint.')

print('Waiting for Player 2 to connect...')
# Accept the connection from Player 2
player2_socket, player2_address = server_socket.accept()

print('Player 2 has connected.')

# Send the word length and hint to Player 2
player2_socket.send(f"{len(word)},{hint}".encode())

while True:
    # Receive the guess from Player 2
    guess = player2_socket.recv(1024).decode()
    if guess == word:
        player2_socket.send("correct".encode())
        break
    else:
        player2_socket.send("incorrect".encode())

# Close the sockets
player1_socket.close()
player2_socket.close()
server_socket.close()
