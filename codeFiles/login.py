from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

class login:

   def __init__(self,root):
      self.root=root
      self.root.title("login Page")
      self.root.geometry("1250x750")
      self.root.resizable(False,False)
      #background image
      file = Image.open("images/warner.png")
      self.resize_image = file.resize((1250, 750))
      self.bg = ImageTk.PhotoImage(self.resize_image)
      self.bg_image = Label(self.root, image = self.bg).place(x=0, y=0)
      #login frame
      Frame_login = Frame(self.root,bg="white")
      Frame_login.place(x=675,y=100,height=320,width=500)
      title = Label(Frame_login,text="Login",font=("Imapct",28),bg="white").place(x=40,y=20)
      
      lb_user = Label(Frame_login,text="Username", font=("Goudy old Style",15), bg="white").place(x=40,y=90)
      self.txt_user = Entry(Frame_login,font=("times new roman",12),bg="white").place(x=45,y=125)
      lb_user = Label(Frame_login, text="Password", font=("Goudy old Style", 15), bg="white").place(x=40, y=155)
      self.txt_pass = Entry(Frame_login, font=("times new roman", 12), bg="white").place(x=45, y=190)
      forget_button = Button(Frame_login,text="Forget Password?", bg = "white", fg="#0000CD",bd=0,font=("times new roman",12)).place(x=40,y=225)
      Login_button = Button(Frame_login,command=self.validate_login,text="Login", bg = "white",font=("times new roman",13))
      Login_button.place(x=40,y=260)

   def validate_login(self):
      usna = self.txt_user
      print(usna.get())


def main():
   root = Tk()
   obj = login(root)
   root.mainloop()

main()
