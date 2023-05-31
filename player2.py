import socket
from tkinter import messagebox, Tk, Entry, Button, Label

# Create a socket object
player2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = 'localhost'
port = 7777

# Connect to the server
player2_socket.connect((host, port))

# Create a Tkinter window
window = Tk()
window.title("Hangman - Player 2")
window.geometry("300x250")

# Create global variables
word = ""
hint = ""

# Function to handle the guess submission
def submit_guess():
    global word
    global hint
    guess = entry.get().strip()
    if guess == "":
        messagebox.showinfo("Error", "Please enter a word!")
    else:
        player2_socket.send(guess.encode())
        result = player2_socket.recv(1024).decode()
        if result == "correct":
            messagebox.showinfo("Congratulations", "You guessed the word correctly!")
            window.quit()
        elif result == "incorrect":
            messagebox.showinfo("Wrong", "Incorrect guess. Try again!")
            entry.delete(0, 'end')

# Receive the hint from the server
hint = player2_socket.recv(1024).decode()

x=hint.split(',',1)
length=x[0]

# Create a Label widget to display the hint

hint_label = Label(window, text=f"Word Length: {x[0]}", font=("Helvetica", 12))
hint_label.pack(pady=10)

hint_label1 = Label(window, text=f"Hint: {x[1]}", font=("Helvetica", 12))
hint_label1.pack(pady=10)


# Create an Entry widget for guessing the word
entry = Entry(window, font=("Helvetica", 20), justify='center')
entry.pack(pady=10)

# Create a Button widget to submit the guess
submit_button = Button(window, text="Submit", font=("Helvetica", 12), command=submit_guess)
submit_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()

# Close the socket
player2_socket.close()
