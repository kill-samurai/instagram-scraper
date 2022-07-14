import tkinter as tk
from bot import InstagramFollowers

root = tk.Tk()
root.title("Instagram Scrapper By KillSamurai")
user_name = tk.StringVar()
pass_word = tk.StringVar()
profile_entry = tk.StringVar()

def get_entry():
    profile = profile_entry.get()
    username = user_name.get()
    password = pass_word.get()
    InstagramFollowers(profile=profile, username=username, password=password)


user_name_label = tk.Label(root, text="Your User Name: ")
user_name_entry = tk.Entry(root, textvariable=user_name)
user_name_label.grid(column=0, row=0, padx=5)
user_name_entry.grid(column=1, row=0, padx=5)

password_label = tk.Label(root, text="Your password: ")
password_entry = tk.Entry(root, textvariable=pass_word, show="#")
password_label.grid(column=0, row=1, padx=5, pady=10)
password_entry.grid(column=1, row=1, padx=5, pady=10)

user_label = tk.Label(root, text="Instagram Profile to get followrs: ")
entry = tk.Entry(root, textvariable=profile_entry)
user_label.grid(column=0, row=2, padx=5, pady=10)
entry.grid(column=1, row=2, padx=5, pady=10)


add_button = tk.Button(root, text="GO!!", command=lambda: get_entry())
add_button.grid(column=0, row=3, columnspan=3, pady=10, ipadx=10)

root.mainloop()