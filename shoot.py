import tkinter as tk
import customtkinter
import random
import os

# Generate a random number between 1 an 6.
def shoot():
    rn = random.randint(1, 6)


    if rn == 6:
        print("Bye Felicia!")
        return os.system("shutdown -1")
    else:
        print("Whew, dodged that bullet!")

#root = tk.Tk()
root = customtkinter.CTk()

root.configure(bg='black')
root.geometry('400x200')

button = customtkinter.CTkButton(master=root, text="Do You Feel Lucky Punk?", command=shoot)

button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()