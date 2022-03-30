import psycopg2
from tkinter import *
from tkinter import messagebox

class worker:
    def __init__(self,root,myuid,mypass):
        self.frame =  root
        self.myuid = myuid
        self.mypass = mypass
        self.connection = psycopg2.connect(host="localhost", user="postgres", password="root", database="inveMSys")
        self.cur = self.connection.cursor()
        self.frame.title("Admin page")
        self.frame.geometry("1280x960")
        self.frame.resizable(False, False)
        self.frame1 = Frame(self.frame, bg="white")
        self.frame1.place(x=0, y=0, height=80, width=1280)
        title = Label(self.frame1, text="INVENTORY MANAGEMENT SYSTEM", font=("Oblique", 20), bg="white")
        title.place(x=5, y=0)
        # create logout button
        logbut = Button(self.frame1, command=self.logout, text="Logout", font=("Oblique", 20), bg="white")
        logbut.place(x=1150, y=5)
        title = Label(self.frame1, text="<<Worker Dashboard>>", font=("Oblique", 18), bg="white").place(x=550, y=40)
        self.frame2 = Frame(self.frame, bg="white")
        view_Work = Button(self.frame2,command=self.viewwork,text="View Work")
        view_Work.place(x=20,y=60,height=50,width=160)
        rep_damage = Button(self.frame2,command=self.reportDam,text="Report Damage")
        rep_damage.place(x=20, y=120, height=50, width=160)
        past_damrep = Button(self.frame2, command=self.pastDamrep,text="Past Reported Damage")
        past_damrep.place(x=20,y=180, height = 50, width=160)
        change_password_button = Button(self.frame2, command=self.changemypasswordui, text="change my password")
        change_password_button.place(x=20, y=800, height=50, width=160)
        self.frame2.place(x=0, y=80, height=880, width=200)
        self.frame3 = Frame(self.frame, bg="white")
        self.frame3.place(x=210, y=82, height=878, width=1070)
        title = Label(self.frame3, text="Welcome", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)


    def viewwork(self):
        self.clearwindow()
        title = Label(self.frame3, text="Active Work", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)



    def reportDam(self):
        self.clearwindow()
        title = Label(self.frame3, text="Report Damage", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)


    def pastDamrep(self):
        self.clearwindow()

    def logout(self):
        self.connection.close()
        quit(worker)

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

    def clearwindow(self):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()

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
                messagebox.showinfo("sucess","Password, Changes sucess")
            except Exception as er:
                print("Error!", f"{er}")

root=Tk()
worker = worker(root, "wok001","123456")
root.mainloop()
