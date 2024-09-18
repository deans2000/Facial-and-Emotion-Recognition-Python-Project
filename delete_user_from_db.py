import tkinter as tk
from faunadb import query as q
from faunadb.client import FaunaClient

# Initializing FaunaDB client
client = FaunaClient(secret="your secret code")

# Declaring entry as a global variable
entry = None

def delete_user_by_name():
    global entry  # Declaring entry as a global variable
    user_name = entry.get()

    try:
        # Querying FaunaDB to find the user by name
        index_data = client.query(
            q.map_(
                lambda ref: q.get(ref),
                q.paginate(q.match(q.index('userii')))
            )
        )

        # Iterating through the data and deleting the user if the name matches
        for entry in index_data['data']:
            user_detail = entry['data']
            if user_detail.get("name", "").lower() == user_name.lower():
                # Extracting the Ref ID and delete the user
                user_ref_id = entry["ref"].id()
                client.query(q.delete(q.ref(q.collection('useri'), user_ref_id)))

                result_label.config(text=f"User '{user_name}' deleted successfully.")
                return  # Exiting the function if user is found and deleted

        result_label.config(text=f"User with name '{user_name}' not found.")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")


# Creating the GUI
root = tk.Tk()
root.title("Delete User from FaunaDB Collection by Name")

label = tk.Label(root, text="Enter User Name:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

delete_button = tk.Button(root, text="Delete User", command=delete_user_by_name)
delete_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
