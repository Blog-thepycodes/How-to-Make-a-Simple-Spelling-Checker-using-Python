from tkinter import *
from textblob import Word
 
 
def check_spelling():
    user_input = entry.get()
    word = Word(user_input)
    corrected_word = word.correct()
 
 
    result_label.config(text=f"Corrected Text: {corrected_word}")
 
 
# Create a main window
root = Tk()
root.title("Simple Spell Checker - The Pycodes")
root.geometry("500x200")
root.configure(bg="#f0e68c")
 
 
# Create and configure a label
label = Label(root, text="Enter a word or phrase:" ,font=18, bg="#f0e68c")
label.pack(pady=10)
 
 
# Create an entry widget for user input
entry = Entry(root, width=40,font=14)
entry.pack()
 
 
# Create a button to check spelling
check_button = Button(root, text="Check Spelling",bg="#8b4513",font=18, command=check_spelling)
check_button.pack(pady=10)
 
 
# Create a label to display the result
result_label = Label(root, text="", wraplength=300,font=14,bg="#f0e68c")
result_label.pack()
 
 
# Start the Tkinter main loop
root.mainloop()
