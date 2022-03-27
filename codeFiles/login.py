from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import psycopg2


class login:
    def __init__(self, root):
        self.root = root
        self.root.title("login Page")
        self.root.geometry("1250x750")
        self.root.resizable(False, False)
        # background image
        file = Image.open("images/warner.png")
        self.resize_image = file.resize((1250, 750))
        self.bg = ImageTk.PhotoImage(self.resize_image)
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0)
        # login frame
        self.frame_login = Frame(self.root, bg="white")
        self.frame_login.place(x=675, y=100, height=320, width=500)
        title = Label(self.frame_login, text="Login", font=("Imapct", 28), bg="white").place(x=40, y=20)

        lb_user = Label(self.frame_login, text="Username", font=("Goudy old Style", 15), bg="white").place(x=40, y=90)
        self.txt_user = Entry(self.frame_login, font=("times new roman", 12), bg="white")
        self.txt_user.place(x=45, y=125)
        lb_user = Label(self.frame_login, text="Password", font=("Goudy old Style", 15), bg="white").place(x=40, y=155)
        self.txt_pass = Entry(self.frame_login, font=("times new roman", 12), bg="white")
        self.txt_pass.place(x=45, y=190)
        forget_button = Button(self.frame_login, command=self.resetpass, text="Forget Password?", bg="white",
                               fg="#0000CD", bd=0,
                               font=("times new roman", 12))
        forget_button.place(x=40, y=225)
        Login_button = Button(self.frame_login, command=self.validate_login, text="Login", bg="white",
                              font=("times new roman", 13))
        Login_button.place(x=40, y=260)

    def validate_login(self):
        if self.txt_user.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error!", "All fields are required", parent=self.root)
        else:
            try:
                connection = psycopg2.connect(host="localhost", user="postgres", password="root",
                                              database="inveMSys")
                cur = connection.cursor()
                cur.execute("select * from login where userid=%s and password=%s",
                            (self.txt_user.get(), self.txt_pass.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!", "Invalid USERNAME & PASSWORD", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Login sucess", parent=self.root)
                    # Clear all the entries
                    self.reset_fields(2)
                    connection.close()

            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.root)

    def resetpass(self):
        for widgets in self.frame_login.winfo_children():
            widgets.destroy()
        title = Label(self.frame_login, text="Reset Password", font=("Imapct", 28), bg="white").place(x=40, y=20)
        
        lb_user = Label(self.frame_login, text="Username", font=("Goudy old Style", 15), bg="white").place(x=40, y=90)
        self.username = Entry(self.frame_login, font=("times new roman", 12), bg="white")
        self.username.place(x=45, y=120)

        lb_user = Label(self.frame_login, text="Secert Key", font=("Goudy old Style", 15), bg="white").place(x=40, y=150)
        self.seckey = Entry(self.frame_login, font=("times new roman", 12), bg="white")
        self.seckey.place(x=45, y=180)

        lb_user = Label(self.frame_login, text="New Password", font=("Goudy old Style", 15), bg="white").place(x=40, y=210)
        self.nepass = Entry(self.frame_login, font=("times new roman", 12), bg="white")
        self.nepass.place(x=45, y=240)

        clear = Button(self.frame_login, command=self.reset_fields, text="Clear", bg="white",font=("times new roman", 13))
        clear.place(x=45, y=270)
        save = Button(self.frame_login, command=self.savepassd, text="Save", bg="white",font=("times new roman", 13))
        save.place(x=115, y=270)

    def savepassd(self):
        uname = self.username.get()
        skey = self.seckey.get()
        newpass = self.nepass.get()
        if uname == "" or skey == "" or newpass == "":
            messagebox.showerror("Error!", "All fields are required", parent=self.root)
        else:
            try:
                connection = psycopg2.connect(host="localhost", user="postgres", password="root",
                                              database="inveMSys")
                cur = connection.cursor()
                cur.execute("select * from login where userid=%s and seckey=%s",
                            (uname, skey))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!", "Invalid USERNAME & SECRET key", parent=self.root)
                    self.reset_fields(2)
                else:
                    try:
                        cur.execute("update login set password=%s where userid=%s and seckey=%s",
                                    (newpass, uname, skey))
                        messagebox.showinfo("Password Change", "password changes saved", parent=self.root)
                        connection.commit()
                    except Exception as er:
                        print("Error!", f"{er}")
                connection.close()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.root)

    def reset_fields(self, n=1):  # n detremines login or forger password
        if n == 2:
            self.txt_pass.delete(0, END)
            self.txt_user.delete(0, END)
        else:
            self.username.delete(0, END)
            self.seckey.delete(0, END)
            self.nepass.delete(0, END)

def main():
    root = Tk()
    obj = login(root)
    root.mainloop()


main()
