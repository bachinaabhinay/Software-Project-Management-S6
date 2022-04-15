import datetime

import psycopg2
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from datetime import date
import os


class worker:
    def __init__(self,root,myuid,mypass):
        self.frame =  root
        self.myuid = myuid
        self.mypass = mypass
        self.connection = psycopg2.connect(host="localhost", user="postgres", password="root", database="inveMSys")
        self.cur = self.connection.cursor()
        self.frame.title("Worker page")
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
        view_Work = Button(self.frame2,command=self.viewworkui,text="View Work")
        view_Work.place(x=20,y=60,height=50,width=160)
        rep_damage = Button(self.frame2,command=self.reportDamui,text="Report Damage")
        rep_damage.place(x=20, y=120, height=50, width=160)
        past_damrep = Button(self.frame2, command=self.pastDamrepui,text="Past Reported Damage")
        past_damrep.place(x=20,y=180, height = 50, width=160)
        change_password_button = Button(self.frame2, command=self.changemypasswordui, text="change my password")
        change_password_button.place(x=20, y=800, height=50, width=160)
        self.frame2.place(x=0, y=80, height=880, width=200)
        self.frame3 = Frame(self.frame, bg="white")
        self.frame3.place(x=210, y=82, height=878, width=1070)
        title = Label(self.frame3, text="Welcome", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)


    def viewworkui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Active Work", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)
        clicktext = Label(self.frame3 ,text="Click Below to view active work ", font=("Oblique",12),bg="White").place(x=8,y=40)
        viewwok = Button(self.frame3, command=self.viewwork, text="View Work")
        viewwok.place(x=8,y=70)
        clicktext = Label(self.frame3, text="Click Below to add completed work", font=("Oblique", 12), bg="White").place(x=8, y=110)
        closework = Button(self.frame3, command=self.closework, text="Update work")
        closework.place(x=8,y=140)

    def viewwork(self):
        row=[]
        root1 = tk.Tk()
        root1.title("My work")
        root1.geometry("1070x450")
        columns = ('jobid','workDesc', 'status', 'assignby', 'assigndate')
        viewtree = ttk.Treeview(root1, columns=columns, show='headings',height=30)
        viewtree.pack()
        viewtree.heading('jobid', text='Job Id')
        viewtree.heading('workDesc', text='work Description')
        viewtree.heading('status', text='work Status')
        viewtree.heading('assignby', text='Assign By')
        viewtree.heading('assigndate', text='Assign Date')
        viewtree.column("jobid", width=100,anchor=CENTER)
        viewtree.column("workDesc", width=550,anchor=CENTER)
        viewtree.column('status', width=120,anchor=CENTER)
        viewtree.column('assignby', width=120,anchor=CENTER)
        viewtree.column('assigndate', width=120,anchor=CENTER)
        viewtree.pack(pady = 30)
        try:
            self.cur.execute(
                "select jobid, workdesc, status, assignby, assigndate from jobcard where assignto='{}'".format(self.myuid))
            row = self.cur.fetchall()
            if row == None:
                messagebox.showinfo("No Work", "No assigned work")
        except Exception as er:
            print("Error!", f"{er}")
        for val in row:
            viewtree.insert(parent='', index='end', text='', values=(val[0], val[1], val[2], val[3], val[4]))

        #style
        style = ttk.Style()
        style.theme_use("default")
        style.map("Viewtree")

        root1.mainloop()


    def closework(self):
        lb_user = Label(self.frame3, text="Enter job Id", font=("Goudy old Style", 15), bg="white").place(x=8, y=190)
        self.jobid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.jobid.place(x=150, y=195)
        closework = Button(self.frame3, command=self.onclickCloseW, text="Check")
        closework.place(x=350, y=190)

    def onclickCloseW(self):
        frame4 = Frame(self.frame, bg="white")
        frame4.place(x=220, y=310, height=450, width=600)
        title = Label(frame4, text="update work", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)
        for widgets in frame4.winfo_children():
            widgets.destroy()
        title = Label(frame4, text="update work", font=("Oblique", 20), bg="white")
        title.place(x=0, y=2)
        if self.jobid.get() == "" :
            messagebox.showerror("Error!", "Incomplete Field Job Id")
        else:
            try:
                self.cur.execute("select * from jobcard where assignto=%s and jobid=%s",(self.myuid, self.jobid.get()))
                row = self.cur.fetchone()
                if row == None:
                    messagebox.showinfo("No Work", "Invalid id")
                    frame4.destroy()
                elif 'completed' in row:
                    messagebox.showinfo("No Work", "For given Id work is completed")
                    frame4.destroy()
                else:
                    l_jobid = Label(frame4,text="Job Id: \t" + f"{row[0]}",font=("times new roman", 14),bg="white")
                    l_jobid.place(x=10, y=50)
                    l_assignby =Label(frame4,text="Assign By: " + f"{row[3]}",font=("times new roman", 14),bg="white")
                    l_assignby.place(x=10, y=80)
                    l_assigndate = Label(frame4,text="Assign Date : " + f"{row[-1]}",font=("times new roman", 14),bg="white")
                    l_assigndate.place(x=10, y=110)
                    l_decsp = Label(frame4,text="Description of job: " + f"{row[1]}",font=("times new roman", 14),bg="white")
                    l_decsp.place(x=10, y=140)
                    complete_button = Button(frame4, command=self.updateProg, text="Update work",font=(12))
                    complete_button.place(x=10,y=250)
                    clear = Button(frame4, command=frame4.destroy, text="clear", font=(12))
                    clear.place(x=150, y=250)
            except Exception as er:
                print("Error!", f"{er}")



    def updateProg(self):
        try:
            self.cur.execute("update jobcard set status=%s where assignto=%s and jobid=%s", ('completed',self.myuid,self.jobid.get()))
            self.connection.commit()
            messagebox.showinfo("success", "Congratulation, Work Done Status is updated")
        except Exception as er:
            print("Error!", f"{er}")

    def reportDamui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Report Damage", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)
        l_repid = Label(self.frame3, text="New Report Id", font=("Goudy old Style", 15), bg="white").place(x=10,y=50)
        self.repid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.repid.place(x=210, y=55)

        l_repdesp = Label(self.frame3, text="Description", font=("Goudy old Style", 15), bg="white").place(x=10, y=80)
        self.repdesp = Text(self.frame3, font=("times new roman", 12), bg="white")
        self.repdesp.place(x=10, y=115, width=450,height=270)

        save = Button(self.frame3, command=self.reportDam, text="Save", bg="white", font=("times new roman", 13))
        save.place(x=10, y=410)
        cancel = Button(self.frame3, command=self.clearwindow, text="Cancel", bg="white",
                        font=("times new roman", 13))
        cancel.place(x=80, y=410)

    def reportDam(self):
        x=datetime.datetime.now()
        self.repdesp.get(1.0,END)
        if self.repdesp.get(1.0,END)=="" or self.repid.get()=="":
            messagebox.showerror("Error!", "All fields are required")
        else:
            try:
                self.cur.execute("select * from damagereport where report_id=%s", (self.repid.get()))
                row = self.cur.fetchone()
                if row != None:
                    messagebox.showerror("Error!", "Id Already assigned\nGive new Report id")
                else:
                    self.cur.execute("INSERT INTO DAMAGEREPORT (REPORT_ID, REP_BY, REP_DESC,REP_DATE) VALUES(%s,%s,%s,%s)",
                                     (self.repid.get(), self.myuid, self.repdesp.get(1.0,END),x.strftime("%x")))
                    messagebox.showinfo("Inserstion Sucess", "Sucess, Damage is reported")
                    self.connection.commit()
            except Exception as er:
                print("Error!", f"{er}")


    def pastDamrepui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Past Reported Damages", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)
        view_past_report = Button(self.frame3, command=self.pastrepui, text="View Past Reported", font=("times new roman", 14))
        view_past_report.place(x=20, y=80)
        edit_past_report = Button(self.frame3,command=self.updatepastrepui,text="Edit past Report",font=("times new roman", 14))
        edit_past_report.place(x=20, y=130)
        delete_past_report = Button(self.frame3, command=self.deletepastreport, text="delete Report",
                                  font=("times new roman", 14))
        delete_past_report.place(x=20, y=180)

    def pastrepui(self):
        self.clearwindow()
        row = []
        columns = ('report_id', 'rep_desc', 'rep_date')
        viewtree = ttk.Treeview(self.frame3, columns=columns, show='headings', height=10)
        viewtree.heading('report_id', text='Report Id')
        viewtree.heading('rep_desc', text='Report Descrption')
        viewtree.heading('rep_date', text='Reported Date')

        viewtree.column("report_id", width=100, anchor=CENTER)
        viewtree.column("rep_desc", width=550, anchor=CENTER)
        viewtree.column('rep_date', width=120, anchor=CENTER)
        viewtree.pack(pady=30)
        try:
            self.cur.execute(
                "select report_id, rep_desc, rep_date from damagereport where rep_by='{}' order by rep_date ASC".format(self.myuid))
            row = self.cur.fetchall()
            if row == None:
                messagebox.showinfo("No Report", "No Damages Reported")
        except Exception as er:
            print("Error!", f"{er}")
        for val in row:
            viewtree.insert(parent='', index='end', text='', values=(val[0], val[1], val[2]))
        # style
        style = ttk.Style()
        style.theme_use("default")
        style.map("viewtree")
        viewtree.pack(padx=10,pady=10)


    def updatepastrepui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Edit Past damage Reported", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)
        lb_user = Label(self.frame3, text="Enter report Id", font=("Goudy old Style", 15), bg="white").place(x=10, y=70)
        self.drepid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.drepid.place(x=170, y=75)
        drepidbu = Button(self.frame3, command=self.checkDamid, text="Check")
        drepidbu.place(x=370, y=70)

    def checkDamid(self):
        if self.drepid.get()=='':
            messagebox.showerror('No Value', "Report Id Field Not Empty")
        else:
            try:
                messagebox.showinfo('ID Present',"Given Id present click ok to update description")
                self.cur.execute("select report_id, rep_by from damagereport where report_id=%s and rep_by=%s", (self.drepid.get(), self.myuid))
                row = self.cur.fetchall()
                if row == None:
                    messagebox.showinfo("No Damage Reported", "No Damage reported for Given id")
                else:
                    l_repdesp = Label(self.frame3, text="Update Description", font=("Goudy old Style", 15), bg="white").place(x=10,y=115)
                    self.repdesp = Text(self.frame3, font=("times new roman", 12), bg="white")
                    self.repdesp.place(x=10, y=150, width=450, height=270)
                    upbutton = Button(self.frame3,text="Save",command=self.upd_rep).place(x=10,y=450)
                    clearbut = Button(self.frame3,text='Clear Field', command=self.repdesp.delete(1.0,END)).place(x=70,y=450)
            except Exception as er:
                print("Error!", f"{er}")

    def upd_rep(self):
        x = str(datetime.datetime.now())
        date_time_obj = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
        x_date = date_time_obj.date()

        textval = self.repdesp.get(1.0,END)
        drepid = self.drepid.get()
        myid = self.myuid
        if textval==None:
            messagebox.showerror('No Value', "Descrption Field Not to be Empty")
        else:
            try:
                self.cur.execute("update damagereport set rep_desc=%s, rep_date=%s where report_id=%s and rep_by=%s", (textval,x_date,drepid,myid))
                self.connection.commit()
                messagebox.showinfo('Sucess', "Report updation sucess")
            except Exception as er:
                print("Error!", f"{er}")



    def deletepastreport(self):
        self.clearwindow()
        title = Label(self.frame3, text="Edit Past damage Reported", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)
        lb_user = Label(self.frame3, text="Enter report Id", font=("Goudy old Style", 15), bg="white").place(x=10, y=70)
        self.drepid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.drepid.place(x=170, y=75)
        drepidbu = Button(self.frame3, command=self.delcheckdam, text="Check")
        drepidbu.place(x=370, y=70)

    def delcheckdam(self):
        if self.drepid.get()=='':
            messagebox.showerror('No Value', "Report Id Field Not Empty")
        else:
            try:
                messagebox.showinfo('ID Present',"Given Id present click ok to delete description report")
                self.cur.execute("select report_id, rep_by from damagereport where report_id=%s and rep_by=%s", (self.drepid.get(), self.myuid))
                row = self.cur.fetchall()
                if row == None:
                    messagebox.showinfo("No Damage Reported", "No Damage reported for Given id")
                else:
                    try:
                        self.cur.execute("Delete from damagereport where report_id=%s and rep_by=%s",(self.drepid.get(), self.myuid))
                        self.connection.commit()
                        messagebox.showinfo('Deletion Sucess', 'Reported Deleted sucess')
                    except Exception as er:
                        print("Error!", f"{er}")
            except Exception as er:
                print("Error!", f"{er}")


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
