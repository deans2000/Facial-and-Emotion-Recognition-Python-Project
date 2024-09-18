import tkinter as tk
import subprocess

def run_code():
    subprocess.run(['python', 'facial_emotion_recog.py'])

def add_user():
    subprocess.run(['python', 'add_user_from_db.py'])

def delete_user():
    subprocess.run(['python', 'delete_user_from_db.py'])

# Creating the main window
root = tk.Tk()
root.title("Facial and Emotion Recognition")

#Setting windows size
root.geometry("400x200")

# Creating buttons
button1 = tk.Button(root, text="Add User", command=add_user)
button1.pack(side="top", expand=True)

button2 = tk.Button(root, text="Delete User", command=delete_user)
button2.pack(side="top", expand=True)

button3 = tk.Button(root, text="Run Code", command=run_code)
button3.pack(side="top", expand=True)

# Starting the GUI main loop
root.mainloop()
