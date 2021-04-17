import instaloader
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import Label, StringVar, messagebox

root = tk.Tk()

def download():
    insta = instaloader.Instaloader()
    profile = user.get()
    try:
        insta.download_profile(profile, profile_pic_only=True)
        messagebox.showinfo("status", "Downloaded")
    except Exception as e:
  
        messagebox.showinfo("status", "Username not found")
#GUI
root.title("Insta Profile Pic downloader")
head = tk.Label(root, text="Instagram Profie Pic Downloader", font=("Poppins", 18, "bold")).grid(row=0, column=0, columnspan=5, padx=28, pady=8)

label = tk.Label(root, text="Enter Username: ", font=("Poppins", 14)).grid(row=2, column=0, pady=8)
user = StringVar()
username = tk.Entry(root, width=40, textvariable=user).grid(row=2, column=1, columnspan=2)

btn = tk.Button(root, text="Download", command=download).grid(row=4, column=0, columnspan=5, padx=2, pady=10)
root.mainloop()