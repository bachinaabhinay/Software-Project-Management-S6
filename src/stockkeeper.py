import datetime

import psycopg2
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from datetime import date
import os


class stockkeeper:
    def __init__(self,root,myuid,mypass):
        self.frame =  root
        self.myuid = myuid
        self.mypass = mypass
        self.connection = psycopg2.connect(host="localhost", user="postgres", password="root", database="inveMSys")
        self.cur = self.connection.cursor()
        self.frame.title("Stock keeper page")
        self.frame.geometry("1280x960")
        self.frame.resizable(False, False)
        self.frame1 = Frame(self.frame, bg="white")
        self.frame1.place(x=0, y=0, height=80, width=1280)
        title = Label(self.frame1, text="INVENTORY MANAGEMENT SYSTEM", font=("Oblique", 20), bg="white")
        title.place(x=5, y=0)
        # create logout button
        logbut = Button(self.frame1, command=self.logout, text="Logout", font=("Oblique", 20), bg="white")
        logbut.place(x=1150, y=5)
        title = Label(self.frame1, text="<<Stock Keeper Dashboard>>", font=("Oblique", 18), bg="white").place(x=550, y=40)
        self.frame2 = Frame(self.frame, bg="white")
        assign_Work = Button(self.frame2,command=self.assignworkui,text="Assign Work")
        assign_Work.place(x=20,y=60,height=50,width=160)
        inventory_but = Button(self.frame2,command=self.inventoryui,text="Inventory")
        inventory_but.place(x=20, y=120, height=50, width=160)
        order_but = Button(self.frame2, command=self.orderui,text="Orders")
        order_but.place(x=20,y=180, height = 50, width=160)
        damagerep_but = Button(self.frame2, command=self.damagerepui,text="Reported Damage")
        damagerep_but.place(x=20,y=240, height = 50, width=160)
        change_password_button = Button(self.frame2, command=self.changemypasswordui, text="change my password")
        change_password_button.place(x=20, y=800, height=50, width=160)
        self.frame2.place(x=0, y=80, height=880, width=200)
        self.frame3 = Frame(self.frame, bg="white")
        self.frame3.place(x=210, y=82, height=878, width=1070)
        title = Label(self.frame3, text="Welcome", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)

#logout Function
    def logout(self):
        self.connection.close()
        quit(stockkeeper)

#assignwork ui
    def assignworkui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Assign work", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)
        view_assign_but = Button(self.frame3, command=self.viewassignworkui, text="View works (asg me)")
        view_assign_but.place(x=20, y=60, height=50, width=160)
        active_but = Button(self.frame3, command=self.viewactivework, text="View Active works")
        active_but.place(x=210, y=60, height=50, width=160)
        assignwork_but = Button(self.frame3, command=self.assignnewwork, text="Assign Work")
        assignwork_but.place(x=120, y=130, height=50, width=160)

    def viewassignworkui(self):
        pass

    def viewactivework(self):
        pass

    def assignnewwork(self):
        pass

#inventory ui
    def inventoryui(self):
        self.clearwindow()
        title = Label(self.frame3,text="INVENTORY",font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)
        view_inven_but = Button(self.frame3, command=self.viewinventoryui, text="View Inventory")
        view_inven_but.place(x=20, y=60, height=50, width=160)
        order_but = Button(self.frame3, command=self.addinventoryui, text="Add Inventory")
        order_but.place(x=210, y=60, height=50, width=160)
        order_but = Button(self.frame3, command=self.updateinventoryui, text="Update Inventory")
        order_but.place(x=120, y=130, height=50, width=160)

    def viewinventoryui(self):
        pass

    def addinventoryui(self):
        pass

    def updateinventoryui(self):
        pass

#order ui
    def orderui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Orders", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)
        neworder_but = Button(self.frame3, command=self.neworderui, text="New Order")
        neworder_but.place(x=20, y=60, height=50, width=160)
        updateorder_but = Button(self.frame3, command=self.updateorderui, text="Update Order")
        updateorder_but.place(x=210, y=60, height=50, width=160)
        vieworder_but = Button(self.frame3, command=self.vieworderui, text="View Orders")
        vieworder_but.place(x=20, y=130, height=50, width=160)
        vieworder_but = Button(self.frame3, command=self.deleteorderui, text="Delete Order")
        vieworder_but.place(x=210, y=130, height=50, width=160)

    def neworderui(self):
        pass

    def updateorderui(self):
        pass

    def vieworderui(self):
        pass

    def deleteorderui(self):
        pass

#damagereport ui
    def damagerepui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Damage Report", font=("Oblique", 20), bg="white")
        title.place(x=10, y=2)
        rep_damage_but = Button(self.frame3, command=self.reportDamui, text="Report Damage")
        rep_damage_but.place(x=20, y=60, height=50, width=160)
        Tak_act_but = Button(self.frame3, command=self.acttakrep, text="Take Action on Rep")
        Tak_act_but.place(x=20, y=120, height=50, width=160)
        pastdam_but = Button(self.frame3, command=self.pastDamrepui, text="Past Damage report ")
        pastdam_but.place(x=20, y=180, height=50, width=160)

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
        if self.drepid.get() == '':
            messagebox.showerror('No Value', "Report Id Field Not Empty")
        else:
            try:
                messagebox.showinfo('ID Present', "Given Id present click ok to update description")
                self.cur.execute("select report_id, rep_by from damagereport where report_id=%s and rep_by=%s",
                                 (self.drepid.get(), self.myuid))
                row = self.cur.fetchall()
                if row == None:
                    messagebox.showinfo("No Damage Reported", "No Damage reported for Given id")
                else:
                    l_repdesp = Label(self.frame3, text="Update Description", font=("Goudy old Style", 15),
                                      bg="white").place(x=10, y=115)
                    self.repdesp = Text(self.frame3, font=("times new roman", 12), bg="white")
                    self.repdesp.place(x=10, y=150, width=450, height=270)
                    upbutton = Button(self.frame3, text="Save", command=self.upd_rep).place(x=10, y=450)
                    clearbut = Button(self.frame3, text='Clear Field', command=self.repdesp.delete(1.0, END)).place(
                        x=70, y=450)
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

    def acttakrep(self):
        pass

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
        if self.drepid.get() == '':
            messagebox.showerror('No Value', "Report Id Field Not Empty")
        else:
            try:
                messagebox.showinfo('ID Present', "Given Id present click ok to delete description report")
                self.cur.execute("select report_id, rep_by from damagereport where report_id=%s and rep_by=%s",
                                 (self.drepid.get(), self.myuid))
                row = self.cur.fetchall()
                if row == None:
                    messagebox.showinfo("No Damage Reported", "No Damage reported for Given id")
                else:
                    try:
                        self.cur.execute("Delete from damagereport where report_id=%s and rep_by=%s",
                                         (self.drepid.get(), self.myuid))
                        self.connection.commit()
                        messagebox.showinfo('Deletion Sucess', 'Reported Deleted sucess')
                    except Exception as er:
                        print("Error!", f"{er}")
            except Exception as er:
                print("Error!", f"{er}")


#change my password ui
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
stockkeper = stockkeeper(root, "stoc001","0001")
root.mainloop()
