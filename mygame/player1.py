import socket
from tkinter import messagebox, Tk, Entry, Button, Label

# Create a socket object
player1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = 'localhost'
port = 7777

# Connect to the server
player1_socket.connect((host, port))

# Create a Tkinter window
window = Tk()
window.title("Hangman - Player 1")
window.geometry("300x250")

# Create global variables
word_entry = None
hint_entry = None

# Function to handle the submission of word and hint
def submit_word_and_hint():
    word = word_entry.get().strip()
    hint = hint_entry.get().strip()

    if word == "" or hint == "":
        messagebox.showinfo("Error", "Please enter both word and hint!")
    else:
        # Send the word and hint to the server
        player1_socket.send(f"{word},{hint}".encode())
        messagebox.showinfo("Success", "Word and hint sent successfully!")

    word_entry.delete(0, 'end')
    hint_entry.delete(0, 'end')
    window.quit()  # Exit the GUI

# Create an Entry widget for entering the word
word_label = Label(window, text="Enter Word:", font=("Helvetica", 12))
word_label.pack(pady=10)

word_entry = Entry(window, font=("Helvetica", 12))
word_entry.pack(pady=5)

# Create an Entry widget for entering the hint
hint_label = Label(window, text="Enter Hint:", font=("Helvetica", 12))
hint_label.pack(pady=10)

hint_entry = Entry(window, font=("Helvetica", 12))
hint_entry.pack(pady=5)

# Create a Button widget to submit the word and hint
submit_button = Button(window, text="Submit", font=("Helvetica", 12), command=submit_word_and_hint)
submit_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()

# Close the socket
player1_socket.close()
