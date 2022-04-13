from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
import psycopg2

class manager:
    def __init__(self,root,myuid,mypass):
        self.myuid = myuid
        self.mypass = mypass
        self.frame = root
        self.connection = psycopg2.connect(host="localhost",port=5433, user="postgres", password="sathwik@123", database="inveMSys")
        self.cur = self.connection.cursor()
        self.frame.title("Manager page")
        self.frame.geometry("1280x960")
        self.frame.resizable(True, True)
        self.frame1 = Frame(self.frame, bg="MediumSpringGreen")
        self.frame1.place(x=0,y=0,height=80,width=1280)
        title = Label(self.frame1,text = "INVENTORY MANAGEMENT SYSTEM", font=("Oblique",20), bg="MediumSpringGreen")
        title.place(x=5,y=0)
        #create logout button
        logbut = Button(self.frame1, command=self.logout, text = "Logout", font=("bold",20), bg="steel blue", fg="white")
        logbut.place(x=1150,y=28,height=45, width=100)
        title = Label(self.frame1,text = "Manager Dashboard", font=("Oblique",20), bg="MediumSpringGreen").place(x=550,y=40)
        self.frame2 = Frame(self.frame,bg="PaleGreen")
        self.frame2.place(x=0,y=80,height=880,width=200)
        update_user_button = Button(self.frame2, command=self.updateuserui, text="Update User", activebackground="cyan", font=(40))
        update_user_button.place(x=20, y=80, height=50, width=150)
        jobcard_button = Button(self.frame2, command=self.jobcardui, text="Jobcard", activebackground="cyan", font=(40))
        jobcard_button.place(x=20, y=150, height=50, width=150)
        inventory_button = Button(self.frame2, command=self.inventoryui, text="Inventory", activebackground="cyan", font=(40))
        inventory_button.place(x=20, y=220, height=50, width=150)
        change_password_button = Button(self.frame2, command=self.changemypasswordui, text="change my password",font=(25), bg="steel blue", fg="white")
        change_password_button.place(x=20, y=500, height=50, width=160)
        self.frame3 = Frame(self.frame, bg="Gray35")
        self.frame3.place(x=210, y=82, height=878, width=1070)
        title = Label(self.frame3, text="Welcome, Manager", font=("Oblique", 20), bg="Gray35", fg="white")
        title.place(x=10, y=2)

    def logout(self):
        self.connection.close()
        quit(manager)

    def clearwindow(self):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()

    def clearwindow1(self):
        for widgets in self.frame2.winfo_children():
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


    def updateuserui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Update User", font=("Oblique", 20),bg="Gray35", fg="white")
        title.place(x=10, y=2)
        title = Label(self.frame3, text="Enter user id to update info of user ", font=("times new roman", 14), bg="Gray35", fg="white")
        title.place(x=10, y=50)
        lb_user = Label(self.frame3, text="User ID", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=10, y=100)
        self.txt_userid1 = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.txt_userid1.place(x=130, y=105)
        proceed = Button(self.frame3, command=self.checkuserid, text="check", bg="white", font=("times new roman", 13))
        proceed.place(x=325,y=98)

    def jobcardui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Job card", font=("Oblique", 20), bg="Gray35", fg="white")
        title.place(x=10, y=2)
        jobcardview_button = Button(self.frame3, command=self.jobcardviewui, text="View", activebackground="orange", font=(40))
        jobcardview_button.place(x=130, y=85, height=45, width=150)
        jobcardupdate_button = Button(self.frame3, command=self.jobcardupdateui, text="Assign", activebackground="orange", font=(40))
        jobcardupdate_button.place(x=130, y=155, height=45, width=150)

    def jobcardviewui(self):
        messagebox.showinfo(title="Jobcard", message="No Data File Found.")

    def jobcardupdateui(self):
        messagebox.showinfo(title="Update", message="No Data File Found.")

    def inventoryui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Inventory", font=("Oblique", 20), bg="Gray35", fg="white")
        title.place(x=10, y=2)
        inventoryview_button = Button(self.frame3,command=self.inventoryviewui, text="View", activebackground="orange", font=(40))
        inventoryview_button.place(x=130, y=85, height=45, width=150)
        inventoryupdate_button = Button(self.frame3, command=self.inventoryupdateui, text="Update", activebackground="orange", font=(40))
        inventoryupdate_button.place(x=130, y=155, height=45, width=150)
        inventoryreport_button = Button(self.frame3, command=self.inventoryreportui, text="Report", activebackground="orange", font=(40))
        inventoryreport_button.place(x=130, y=225, height=45, width=150)

    def inventoryviewui(self):
        messagebox.showinfo(title="View", message="No Data File Found.")

    def inventoryupdateui(self):
        messagebox.showinfo(title="Update", message="No Data File Found.")

    def inventoryreportui(self):
        messagebox.showinfo(title="Report", message="No Data File Found.")

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
    obj = manager(root,uid,passd)
    root.mainloop()

main('wok001',123456)