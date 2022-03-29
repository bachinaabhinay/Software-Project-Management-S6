import tkinter as tk
from tkinter import ttk
import time

def startprocess():
    def increment(*args):
        for i in range(100):
            p1["value"] = i+1
            root.update()
            time.sleep(0.1)

    root = tk.Tk()
    root.title("loading files")
    root.geometry('700x200')
    label_1 = tk.Label(root, text="please wait, we are setting the required things for you")
    p1 = ttk.Progressbar(root, length=300, cursor='spider',
                         mode="determinate",
                         orient=tk.HORIZONTAL)
    mybutton = tk.Button(root,text="Quit",command = root.destroy)
    label_1.pack(pady=20)
    p1.pack(pady=20)
    mybutton.pack(pady=20)
    increment()
    root.destroy()
    root.mainloop()

startprocess()