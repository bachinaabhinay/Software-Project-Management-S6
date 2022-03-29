from tkinter import *
from tkinter import messagebox
import psycopg2

class admin:
    def __init__(self,root,myuid,mypass):
        self.myuid = myuid
        self.mypass = mypass
        self.frame = root
        self.connection = psycopg2.connect(host="localhost",port=5433, user="postgres", password="sathwik@123", database="inveMSys")
        self.cur = self.connection.cursor()
        self.frame.title("Manager page")
        self.frame.geometry("1280x960")
        self.frame.resizable(True, True)
        self.frame1 = Frame(self.frame, bg="white")
        self.frame1.place(x=0,y=0,height=80,width=1280)
        title = Label(self.frame1,text = "INVENTORY MANAGEMENT SYSTEM", font=("Oblique",20), bg="white")
        title.place(x=5,y=0)
        #create logout button
        logbut = Button(self.frame1, command=self.logout, text = "Logout", font=("Oblique",20), bg="white")
        logbut.place(x=1150,y=5)
        title = Label(self.frame1,text = "<<Manager Dashboard>>", font=("Oblique",18), bg="white").place(x=550,y=40)
        self.frame2 = Frame(self.frame,bg="white")
        self.frame2.place(x=0,y=80,height=880,width=200)
        add_user_button = Button(self.frame2,command= self.addusersui ,text = "Add User",bg="white",font=(40))
        add_user_button.place(x=20,y=60,height=50,width=160)
        update_user_button = Button(self.frame2, command=self.updateuserui, text="Update User", bg="white", font=(40))
        update_user_button.place(x=20, y=120, height=50, width=160)
        change_password_button = Button(self.frame2, command=self.changemypasswordui, text="change my password", bg="white")
        change_password_button.place(x=20, y=800, height=50, width=160)
        self.frame3 = Frame(self.frame, bg="white")
        self.frame3.place(x=210, y=82, height=878, width=1070)
        title = Label(self.frame3, text="Welcome, Manager", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)

    def logout(self):
        self.connection.close()
        quit(admin)

    def clearwindow(self):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()

    def reset_fields(self):
        self.txt_name.delete(0, END)
        self.txt_role.delete(0, END)
        self.txt_userid.delete(0, END)
        self.txt_pass.delete(0, END)
        self.txt_seckey.delete(0, END)

    def reset_fields1(self):
        self.txt_role.delete(0, END)
        self.txt_pass.delete(0, END)
        self.txt_seckey.delete(0, END)

    def addusersui(self): # to make GUI
        self.clearwindow()
        title = Label(self.frame3, text="Add User", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)
        lb_user = Label(self.frame3, text="Name", font=("Goudy old Style", 15), bg="white").place(x=10, y=50)
        self.txt_name = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.txt_name.place(x=180, y=50)
        lb_user = Label(self.frame3, text="Role", font=("Goudy old Style", 15), bg="white").place(x=10, y=80)
        self.txt_role = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.txt_role.place(x=180, y=80)
        lb_user = Label(self.frame3, text="User ID", font=("Goudy old Style", 15), bg="white").place(x=10, y=110)
        self.txt_userid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.txt_userid.place(x=180, y=120)
        lb_user = Label(self.frame3, text="Password", font=("Goudy old Style", 15), bg="white").place(x=10, y=140)
        self.txt_pass = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.txt_pass.place(x=180, y=150)
        lb_user = Label(self.frame3, text="Secert Key", font=("Goudy old Style", 15), bg="white").place(x=10, y=180)
        self.txt_seckey = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.txt_seckey.place(x=180, y=180)
        clear = Button(self.frame3, command=self.reset_fields, text="Clear", bg="white",
                       font=("times new roman", 13))
        clear.place(x=10, y=230)
        save = Button(self.frame3, command=self.adduser, text="Save", bg="white", font=("times new roman", 13))
        save.place(x=80, y=230)
        cancel = Button(self.frame3, command=self.clearwindow, text="Cancel", bg="white", font=("times new roman", 13))
        cancel.place(x=145,y=230)

    def adduser(self):
        name = self.txt_name.get()
        role = self.txt_role.get()
        userid = self.txt_userid.get()
        password = self.txt_pass.get()
        seckey = self.txt_seckey.get()
        if name=="" or role=="" or userid=="" or password=="" or seckey=="":
            messagebox.showerror("Error!", "All fields are required", parent=self.frame)
        else:
            try:
                self.cur.execute("INSERT INTO EMPLOYEE (name, role, userid) VALUES(%s,%s,%s)", (name, role, userid))
                self.cur.execute("INSERT INTO login (userid, password, seckey) VALUES(%s,%s,%s)",
                                 (userid, password, seckey))
                self.connection.commit()
                messagebox.showinfo("Sucess", "Insertion sucess", parent=self.frame)
            except Exception as er:
                messagebox.showerror("Error!", f"{er}", parent=self.frame)

    def updateuserui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Update User", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)
        title = Label(self.frame3, text="Enter user id to update info of user ", font=("times new roman", 12), bg="white")
        title.place(x=10, y=40)
        lb_user = Label(self.frame3, text="User ID", font=("Goudy old Style", 15), bg="white").place(x=10, y=80)
        self.txt_userid1 = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.txt_userid1.place(x=130, y=85)
        proceed = Button(self.frame3, command=self.checkuserid, text="check", bg="white", font=("times new roman", 13))
        proceed.place(x=325,y=78)

    def checkuserid(self):
        uid=StringVar()
        connection1 = psycopg2.connect(host="localhost",port=5433, user="postgres", password="sathwik@123", database="inveMSys")
        cur1 = connection1.cursor()
        if uid == None:
            messagebox.showerror("Empty Fields","All Fields are Required")
        else:
            try:
                cur1.execute("select name from employee where userid = '{0}'".format(self.txt_userid1.get()))
                nameofuid = cur1.fetchone()
                title = Label(self.frame3, text="Name: \t\t"+f"{nameofuid[0]}", font=("times new roman", 16),bg="white")
                title.place(x=10, y=130)
                lb_user = Label(self.frame3, text="Role", font=("Goudy old Style", 15), bg="white").place(x=10, y=170)
                self.txt_role = Entry(self.frame3, font=("times new roman", 12), bg="white")
                self.txt_role.place(x=180, y=170)
                lb_user = Label(self.frame3, text="Password", font=("Goudy old Style", 15), bg="white").place(x=10,y=200)
                self.txt_pass = Entry(self.frame3, font=("times new roman", 12), bg="white")
                self.txt_pass.place(x=180, y=200)
                lb_user = Label(self.frame3, text="Secert Key", font=("Goudy old Style", 15), bg="white").place(x=10,y=230)
                self.txt_seckey = Entry(self.frame3, font=("times new roman", 12), bg="white")
                self.txt_seckey.place(x=180, y=230)
                clear = Button(self.frame3, command=self.reset_fields1, text="Clear", bg="white",
                               font=("times new roman", 13))
                clear.place(x=10, y=260)
                save = Button(self.frame3, command=self.updateuser, text="Save", bg="white", font=("times new roman", 13))
                save.place(x=80, y=260)
                cancel = Button(self.frame3, command=self.clearwindow, text="Cancel", bg="white",
                                font=("times new roman", 13))
                cancel.place(x=145, y=260)

            except Exception as er:
                messagebox.showerror("Error!", f"{er}")

    def updateuser(self):
        userid=self.txt_userid1.get()
        role = self.txt_role.get()
        password = self.txt_pass.get()
        seckey = self.txt_seckey.get()
        if  role == "" or password == "" or seckey == "":
            messagebox.showerror("Error!", "All fields are required", parent=self.frame)
        else:
            try:
                self.cur.execute("UPDATE EMPLOYEE SET ROLE=%s WHERE USERID=%s", (role, userid))
                self.cur.execute("UPDATE login SET password=%s ,seckey=%s WHERE USERID=%s",(password, seckey, userid))
                self.connection.commit()
                messagebox.showinfo("Sucess", "Insertion sucess", parent=self.frame)
            except Exception as er:
                messagebox.showerror("Error!", f"{er}")

    def changemypasswordui(self):
        self.clearwindow()
        title = Label(self.frame3, text="change my password", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)
        lb_user = Label(self.frame3, text="Current password", font=("Goudy old Style", 15), bg="white").place(x=10, y=50)
        self.cpass = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.cpass.place(x=210, y=55)
        lb_user = Label(self.frame3, text="New password", font=("Goudy old Style", 15), bg="white").place(x=10, y=80)
        self.newpass = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.newpass.place(x=210, y=85)
        lb_user = Label(self.frame3, text="Re-enter password ", font=("Goudy old Style", 15), bg="white").place(x=10, y=110)
        self.renpass = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.renpass.place(x=210, y=115)
        clear = Button(self.frame3, command=self.reset_fields3, text="Clear", bg="white",
                       font=("times new roman", 13))
        clear.place(x=10, y=260)
        save = Button(self.frame3, command=self.changemypassword, text="Save", bg="white", font=("times new roman", 13))
        save.place(x=80, y=260)
        cancel = Button(self.frame3, command=self.clearwindow, text="Cancel", bg="white",
                        font=("times new roman", 13))
        cancel.place(x=145, y=260)

    def reset_fields3(self):
        self.cpass.delete(0, END)
        self.newpass.delete(0, END)
        self.renpass.delete(0, END)

    def changemypassword(self):
        cpass=StringVar()
        cpass = self.cpass.get()
        if self.renpass.get() == "" or self.cpass.get()=="" or self.newpass.get()=="":
            messagebox.showerror("Error!", "All fields are required")
        elif self.mypass!=cpass:
            messagebox.showerror("Error!","Entered password is not matched")
        elif self.newpass.get()!=self.renpass.get():
            messagebox.showerror("Error!", "Entered & Re - entered new password is not matched")
        else:
            try:
                self.cur.execute("update login set password=%s where userid=%s", (self.newpass.get(), self.myuid))
                self.connection.commit()
                messagebox.showinfo("password changed sucessfully")
            except Exception as er:
                print("Error!", f"{er}")

def main(uid,passd):
    root = Tk()
    obj = admin(root,uid,passd)
    root.mainloop()

main('wok001',123456)