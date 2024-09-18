from faunadb import query as q
from faunadb.client import FaunaClient
import tkinter as tk

def insert_data():
    # Getting values from the entry fields
    key1_value = entry_name.get()
    key2_value = entry_photo.get()

    # Inserting data into FaunaDB
    client.query(
        q.create(
            q.collection(collection_name),
            {'data': {'name': key1_value, 'image': key2_value}}
        )
    )

    # Closing the window
    root.quit()

# Initializing the FaunaDB client
client = FaunaClient(secret='your secret code')  # Replace with your FaunaDB secret

# Defining the collection name
collection_name = 'useri'

# Creating the main window
root = tk.Tk()
root.title("FaunaDB Data Insertion")

# Creating labels and entry fields
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_photo = tk.Label(root, text="Photo Name:")
label_photo.grid(row=1, column=0, padx=10, pady=5)

entry_photo = tk.Entry(root)
entry_photo.grid(row=1, column=1, padx=10, pady=5)

# Creating a button to insert data
insert_button = tk.Button(root, text="Insert Data", command=insert_data)
insert_button.grid(row=2, columnspan=2, pady=10)

# Starting the GUI main loop
root.mainloop()
