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
        self.connection = psycopg2.connect(host="localhost",port=5433, user="postgres", password="sathwik@123", database="inveMSys")
        self.cur = self.connection.cursor()
        self.frame.title("Stock keeper page")
        self.frame.geometry("1280x960")
        self.frame.resizable(True, True)
        self.frame1 = Frame(self.frame, bg="light sky blue")
        self.frame1.place(x=0, y=0, height=80, width=1280)
        title = Label(self.frame1, text="INVENTORY MANAGEMENT SYSTEM", font=("Oblique", 20), bg="light sky blue")
        title.place(x=5, y=0)
        # create logout button
        logbut = Button(self.frame1, command=self.logout, text="Logout", font=("Oblique", 20), bg="white")
        logbut.place(x=1150, y=5)
        title = Label(self.frame1, text="<<Stock Keeper Dashboard>>", font=("Oblique", 18), bg="light sky blue").place(x=550, y=40)
        self.frame2 = Frame(self.frame, bg="powder blue")
        assign_Work = Button(self.frame2,command=self.assignworkui,text="Assign Work")
        assign_Work.place(x=20,y=60,height=50,width=160)
        inventory_but = Button(self.frame2,command=self.inventoryui,text="Inventory")
        inventory_but.place(x=20, y=120, height=50, width=160)
        order_but = Button(self.frame2, command=self.orderui,text="Orders")
        order_but.place(x=20,y=180, height = 50, width=160)
        damagerep_but = Button(self.frame2, command=self.damagerepui,text="Reported Damage")
        damagerep_but.place(x=20,y=240, height = 50, width=160)
        change_password_button = Button(self.frame2, command=self.changemypasswordui, text="change my password")
        change_password_button.place(x=20, y=500, height=50, width=160)
        self.frame2.place(x=0, y=80, height=880, width=200)
        self.frame3 = Frame(self.frame, bg="goldenrod")
        self.frame3.place(x=210, y=82, height=878, width=1070)
        title = Label(self.frame3, text="Welcome", font=("Oblique", 20), bg="goldenrod")
        title.place(x=100, y=70)

#logout Function
    def logout(self):
        self.connection.close()
        quit(stockkeeper)

#assignwork ui
    def assignworkui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Assign work", font=("Oblique", 20), bg="goldenrod")
        title.place(x=10, y=2)
        view_assign_but = Button(self.frame3, command=self.viewassignworkui, text="View works (asg me)")
        view_assign_but.place(x=20, y=60, height=50, width=160)
        active_but = Button(self.frame3, command=self.viewactivework, text="View Active works")
        active_but.place(x=210, y=60, height=50, width=160)
        assignwork_but = Button(self.frame3, command=self.assignnewworkui, text="Assign Work")
        assignwork_but.place(x=120, y=130, height=50, width=160)

    def viewassignworkui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Assigned Works (Past)", font=("Oblique", 20), bg="goldenrod")
        title.place(x=10, y=2)
        row = []
        columns = ('job_id', 'wok_desc', 'status', 'aasignto', 'assign_date')
        viewtree = ttk.Treeview(self.frame3, columns=columns, show='headings', height=10)
        viewtree.heading('job_id', text='Job Id')
        viewtree.heading('wok_desc', text='work Descrption')
        viewtree.heading('status', text='Status')
        viewtree.heading('aasignto', text='Assign To')
        viewtree.heading('assign_date', text='Date Assigned')

        viewtree.column("job_id", width=100, anchor=CENTER)
        viewtree.column("wok_desc", width=350, anchor=CENTER)
        viewtree.column('status', width=100, anchor=CENTER)
        viewtree.column('aasignto', width=100, anchor=CENTER)
        viewtree.column('assign_date', width=100, anchor=CENTER)
        viewtree.pack(pady=50, padx=10)
        try:
            self.cur.execute(
                "select jobid,workdesc,status,assignto,assigndate from jobcard where assignby='{}' order by jobid ASC".format(
                    self.myuid))
            row = self.cur.fetchall()
            if row == []:
                messagebox.showinfo("No Report", "No past assignned works")
        except Exception as er:
            print("Error!", f"{er}")
        for val in row:
            viewtree.insert(parent='', index='end', text='', values=(val[0], val[1], val[2], val[3], val[4]))
        # style
        style = ttk.Style()
        style.theme_use("default")
        style.map("viewtree")
        button_back = Button(self.frame3, command=self.assignworkui, text="Back")
        button_back.place(x=10, y=250, height=40, width=80)

    def viewactivework(self):
        self.clearwindow()
        title = Label(self.frame3, text="Active Works", font=("Oblique", 20), bg="goldenrod")
        title.place(x=10, y=2)
        row = []
        columns = ('job_id', 'wok_desc', 'assignby', 'aasignto', 'assign_date')
        viewtree = ttk.Treeview(self.frame3, columns=columns, show='headings', height=10)
        viewtree.heading('job_id', text='Job Id')
        viewtree.heading('wok_desc', text='work Descrption')
        viewtree.heading('assignby', text='Assign By')
        viewtree.heading('aasignto', text='Assign To')
        viewtree.heading('assign_date', text='Date Assigned')

        viewtree.column("job_id", width=100, anchor=CENTER)
        viewtree.column("wok_desc", width=350, anchor=CENTER)
        viewtree.column('assignby', width=100, anchor=CENTER)
        viewtree.column('aasignto', width=100, anchor=CENTER)
        viewtree.column('assign_date', width=100, anchor=CENTER)
        viewtree.pack(pady=50, padx=10)
        try:
            self.cur.execute(
                "select jobid,workdesc,assignby,assignto,assigndate from jobcard where status='{}' order by jobid ASC".format(
                    "processing"))
            row = self.cur.fetchall()
            if row == []:
                messagebox.showinfo("No Report", "No past assignned works")
        except Exception as er:
            print("Error!", f"{er}")
        for val in row:
            viewtree.insert(parent='', index='end', text='', values=(val[0], val[1], val[2], val[3], val[4]))
        # style
        style = ttk.Style()
        style.theme_use("default")
        style.map("viewtree")
        button_back = Button(self.frame3, command=self.assignworkui, text="Back")
        button_back.place(x=10, y=250, height=40, width=80)

    def assignnewworkui(self):
        self.clearwindow()
        self.clearwindow()
        title = Label(self.frame3, text="Assign Work", font=("Oblique", 20), bg="goldenrod")
        title.place(x=10, y=2)
        l_repid = Label(self.frame3, text="New Job Id", font=("Goudy old Style", 15), bg="goldenrod").place(x=10, y=50)
        self.jbid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.jbid.place(x=210, y=55)
        l_repid = Label(self.frame3, text="Worker Id", font=("Goudy old Style", 15), bg="goldenrod").place(x=10, y=80)
        self.wkid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.wkid.place(x=210, y=85)

        l_repdesp = Label(self.frame3, text="Work Description", font=("Goudy old Style", 15), bg="goldenrod").place(x=10, y=110)
        self.assdesp = Text(self.frame3, font=("times new roman", 12), bg="white")
        self.assdesp.place(x=10, y=145, width=450, height=270)

        save = Button(self.frame3, command=self.assignnework, text="Save", bg="white", font=("times new roman", 13))
        save.place(x=10, y=450)
        cancel = Button(self.frame3, command=self.assignworkui, text="Cancel", bg="white",
                        font=("times new roman", 13))
        cancel.place(x=80, y=450)

    def assignnework(self):
        x = str(datetime.datetime.now())
        date_time_obj = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
        x_date = date_time_obj.date()
        jid = self.jbid.get()
        wkid= self.wkid.get()
        descp = self.assdesp.get(1.0,END)
        myid = self.myuid
        status = "processing"
        if descp == "" or jid == "" or wkid == "":
            messagebox.showerror("Error!", "All fields are required")
        else:
            try:
                self.cur.execute("select * from jobcard where jobid=%s", (jid))
                row = self.cur.fetchone()
                if row != None:
                    messagebox.showerror("Error!", "Id Already assigned\nGive new job id")
                else:
                    self.cur.execute(
                        "insert into jobcard (jobid, workdesc, assignby, assignto, assigndate, status) values('{0}','{1}','{2}','{3}','{4}','{5}')".format(jid,descp,myid,wkid,x_date,status))
                    messagebox.showinfo("Inserstion Sucess", "Sucess, job is assigned")
                    self.connection.commit()
            except Exception as er:
                print("Error!", f"{er}")


#inventory ui
    def inventoryui(self):
        self.clearwindow()
        title = Label(self.frame3,text="INVENTORY",font=("Oblique", 20), bg="goldenrod")
        title.place(x=10, y=2)
        view_inven_but = Button(self.frame3, command=self.viewinventoryui, text="View Inventory")
        view_inven_but.place(x=20, y=60, height=50, width=160)
        order_but = Button(self.frame3, command=self.addinventoryui, text="Add Inventory")
        order_but.place(x=210, y=60, height=50, width=160)
        order_but = Button(self.frame3, command=self.updateinventoryui, text="Update Inventory")
        order_but.place(x=120, y=130, height=50, width=160)

    def viewinventoryui(self):
        row = []
        root1 = tk.Tk()
        root1.title("Inventory")
        root1.geometry("1070x450")
        columns = (
        'inventoryid', 'inventoryitems', 'inventorydesc', 'inventoryprice', 'inventorynumber', 'inventoryexpiry',
        'inventoryarriveddate')
        viewtree = ttk.Treeview(root1, columns=columns, show='headings', height=30)
        viewtree.pack()
        viewtree.heading('inventoryid', text='Inventory Id')
        viewtree.heading('inventoryitems', text='Inventory Item')
        viewtree.heading('inventorydesc', text='Inventory Description')
        viewtree.heading('inventoryprice', text='Price')
        viewtree.heading('inventorynumber', text='Remaining')
        viewtree.heading('inventoryexpiry', text='Expiry Date')
        viewtree.heading('inventoryarriveddate', text='Arrived Date')
        viewtree.column("inventoryid", width=100, anchor=CENTER)
        viewtree.column("inventoryitems", width=350, anchor=CENTER)
        viewtree.column('inventorydesc', width=120, anchor=CENTER)
        viewtree.column('inventoryprice', width=120, anchor=CENTER)
        viewtree.column('inventorynumber', width=120, anchor=CENTER)
        viewtree.column('inventoryexpiry', width=120, anchor=CENTER)
        viewtree.column('inventoryarriveddate', width=120, anchor=CENTER)
        viewtree.pack(pady=30)
        try:
            self.cur.execute(
                "select inventoryid, inventoryitems, inventorydesc, inventoryprice, inventorynumber, inventoryexpiry, inventoryarriveddate from inventory".format(
                    self.myuid))
            row = self.cur.fetchall()
            if row == None:
                messagebox.showinfo("No Inventory", "Inventory is empty")
        except Exception as er:
            print("Error!", f"{er}")
        for val in row:
            viewtree.insert(parent='', index='end', text='',
                            values=(val[0], val[1], val[2], val[3], val[4], val[5], val[6]))

        # style
        style = ttk.Style()
        style.theme_use("default")
        style.map("Viewtree")

        root1.mainloop()

    def addinventoryui(self):
        self.clearwindow()
        lb_user = Label(self.frame3, text="Enter Inventory Id", font=("Goudy old Style", 15), bg="goldenrod",
                        fg="white").place(x=8, y=230)
        self.inventoryid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventoryid.place(x=250, y=235)
        lb_user1 = Label(self.frame3, text="Enter Inventory Items", font=("Goudy old Style", 15), bg="goldenrod",
                         fg="white").place(x=8, y=280)
        self.inventoryitems = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventoryitems.place(x=250, y=285)
        lb_user2 = Label(self.frame3, text="Enter Inventory Description", font=("Goudy old Style", 15), bg="goldenrod",
                         fg="white").place(x=8, y=330)
        self.inventorydesc = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventorydesc.place(x=250, y=335)
        lb_user3 = Label(self.frame3, text="Enter Inventory Price", font=("Goudy old Style", 15), bg="goldenrod",
                         fg="white").place(x=8, y=380)
        self.inventoryprice = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventoryprice.place(x=250, y=385)
        lb_user4 = Label(self.frame3, text="Enter Inventory Number", font=("Goudy old Style", 15), bg="goldenrod",
                         fg="white").place(x=8, y=430)
        self.inventorynumber = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventorynumber.place(x=250, y=435)
        lb_user5 = Label(self.frame3, text="Enter Inventory Expiry", font=("Goudy old Style", 15), bg="goldenrod",
                         fg="white").place(x=8, y=480)
        self.inventoryexpiry = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventoryexpiry.place(x=250, y=485)
        closework = Button(self.frame3, command=self.inventoryaddnew, text="Update", font=("bold", 17), bg="steel blue",
                           fg="white")
        closework.place(x=100, y=553, height=35, width=130)

    def inventoryaddnew(self):
        x = str(datetime.datetime.now())
        date_time_obj = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
        x_date = date_time_obj.date()
        if self.inventoryid.get() == "" or self.inventoryitems.get() == "" or self.inventorydesc.get() == "" or self.inventoryprice.get() == "" or self.inventorynumber.get() == "" or self.inventoryexpiry.get() == "":
            messagebox.showerror("Error!", "All fields are required")
        else:
            try:
                self.cur.execute("select * from inventory where inventoryid=%s", (self.inventoryid.get()))
                row = self.cur.fetchone()
                if row != None:
                    messagebox.showerror("Error!", "Id Already assigned\nGive new Job id")
                else:
                    self.cur.execute(
                        "INSERT INTO inventory (inventoryid, inventoryitems, inventorydesc, inventoryprice, inventorynumber, inventoryexpiry, inventoryarriveddate) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                        (self.inventoryid.get(), self.inventoryitems.get(), self.inventorydesc.get(),
                         self.inventoryprice.get(), self.inventorynumber.get(), self.inventoryexpiry.get(), x_date))
                    messagebox.showinfo("Added Sucess", "Sucess, Added to Inventory")
                    self.connection.commit()
            except Exception as er:
                print("Error!", f"{er}")

    def updateinventoryui(self):
        self.clearwindow()
        lb_user = Label(self.frame3, text="Enter Inventory Id", font=("Goudy old Style", 15), bg="goldenrod",
                        fg="white").place(x=8, y=230)
        self.inventoryid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventoryid.place(x=250, y=235)
        lb_user1 = Label(self.frame3, text="Enter Inventory Items", font=("Goudy old Style", 15), bg="goldenrod",
                         fg="white").place(x=8, y=280)
        self.inventoryitems = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventoryitems.place(x=250, y=285)
        lb_user2 = Label(self.frame3, text="Enter Inventory Description", font=("Goudy old Style", 15), bg="goldenrod",
                         fg="white").place(x=8, y=330)
        self.inventorydesc = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventorydesc.place(x=250, y=335)
        lb_user3 = Label(self.frame3, text="Enter Inventory Price", font=("Goudy old Style", 15), bg="goldenrod",
                         fg="white").place(x=8, y=380)
        self.inventoryprice = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventoryprice.place(x=250, y=385)
        lb_user4 = Label(self.frame3, text="Enter Inventory Number", font=("Goudy old Style", 15), bg="goldenrod",
                         fg="white").place(x=8, y=430)
        self.inventorynumber = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventorynumber.place(x=250, y=435)
        lb_user5 = Label(self.frame3, text="Enter Inventory Expiry", font=("Goudy old Style", 15), bg="goldenrod",
                         fg="white").place(x=8, y=480)
        self.inventoryexpiry = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventoryexpiry.place(x=250, y=485)
        closework = Button(self.frame3, command=self.inventoryupdate, text="Update", font=("bold", 17), bg="steel blue",
                           fg="white")
        closework.place(x=100, y=553, height=35, width=130)

    def inventoryupdate(self):
        if self.inventoryid.get() == "" or self.inventoryitems.get() == "" or self.inventorydesc.get() == "" or self.inventoryprice.get() == "" or self.inventorynumber.get() == "" or self.inventoryexpiry.get() == "":
            messagebox.showerror("Error!", "All fields are required")
        else:
            try:
                self.cur.execute("select * from inventory where inventoryid=%s", (self.inventoryid.get()))
                row = self.cur.fetchone()
                if row != None:
                    self.cur.execute(
                        "update inventory set inventoryitems=%s, inventorydesc=%s, inventoryprice=%s, inventorynumber=%s, inventoryexpiry=%s where inventoryid=%s",
                        (self.inventoryitems.get(), self.inventorydesc.get(), self.inventoryprice.get(),
                         self.inventorynumber.get(), self.inventoryexpiry.get(), self.inventoryid.get()))
                    self.cur.execute(
                        "update producttable set item_quantity=%s where item_id=%s",
                        (self.inventorynumber.get(), self.inventoryid.get()))

                    messagebox.showinfo("updation Sucess", "Sucess, Inventory is Updated")
                    self.connection.commit()
            except Exception as er:
                print("Error!", f"{er}")

    def inventoryreportui(self):
        row = []
        root1 = tk.Tk()
        root1.title("Inventory Report")
        root1.geometry("890x450")
        columns = ('inventoryitems', 'inventorynumber', 'inventoryarriveddate')
        viewtree = ttk.Treeview(root1, columns=columns, show='headings', height=30)
        viewtree.pack()
        viewtree.heading('inventoryitems', text='Item name')
        viewtree.heading('inventorynumber', text='Remaining')
        viewtree.heading('inventoryarriveddate', text='Arrived Date')
        viewtree.column("inventoryitems", width=120, anchor=CENTER)
        viewtree.column("inventorynumber", width=120, anchor=CENTER)
        viewtree.column('inventoryarriveddate', width=120, anchor=CENTER)
        viewtree.pack(pady=30)
        try:
            self.cur.execute(
                "select inventoryitems, inventorynumber, inventoryarriveddate from inventory".format(
                    self.myuid))
            row = self.cur.fetchall()
            if row == None:
                messagebox.showinfo("No Inventory", "Inventory is empty")
        except Exception as er:
            print("Error!", f"{er}")
        for val in row:
            viewtree.insert(parent='', index='end', text='', values=(val[0], val[1], val[2]))

        # style
        style = ttk.Style()
        style.theme_use("default")
        style.map("Viewtree")

        root1.mainloop()

#order ui
    def orderui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Orders", font=("Oblique", 20), bg="goldenrod")
        title.place(x=10, y=2)
        updateorder_but = Button(self.frame3, command=self.updateorderui, text="Update Order")
        updateorder_but.place(x=115, y=60, height=50, width=160)
        vieworder_but = Button(self.frame3, command=self.vieworderui, text="View Orders")
        vieworder_but.place(x=20, y=130, height=50, width=160)
        vieworder_but = Button(self.frame3, command=self.deleteorderui, text="Delete Order")
        vieworder_but.place(x=210, y=130, height=50, width=160)

    def updateorderui(self):
        self.clearwindow()
        lb_user = Label(self.frame3, text="Enter Order Id", font=("Goudy old Style", 15), bg="goldenrod",
                        fg="white").place(x=8, y=230)
        self.orderid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.orderid.place(x=250, y=235)
        lb_user1 = Label(self.frame3, text="Enter Order Name", font=("Goudy old Style", 15), bg="goldenrod",
                         fg="white").place(x=8, y=280)
        self.ordername = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.ordername.place(x=250, y=285)
        lb_user2 = Label(self.frame3, text="Enter Payment Type", font=("Goudy old Style", 15), bg="goldenrod",
                         fg="white").place(x=8, y=330)
        self.ordertype = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.ordertype.place(x=250, y=335)
        lb_user3 = Label(self.frame3, text="Enter Order Quantity", font=("Goudy old Style", 15), bg="goldenrod",
                         fg="white").place(x=8, y=380)
        self.orderquantity = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.orderquantity.place(x=250, y=385)
        lb_user4 = Label(self.frame3, text="Enter Order Date", font=("Goudy old Style", 15), bg="goldenrod",
                         fg="white").place(x=8, y=430)
        self.orderdate = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.orderdate.place(x=250, y=435)
        closework = Button(self.frame3, command=self.orderupdate, text="Update", font=("bold", 17), bg="steel blue",
                           fg="white")
        closework.place(x=100, y=503, height=35, width=130)

    def orderupdate(self):
        try:
            self.cur.execute("select * from orders where order_id=%s", (self.orderid.get()))
            row = self.cur.fetchone()
            if row != None:
                self.cur.execute(
                    "update orders set order_name=%s, order_type=%s, order_quantity=%s, order_date=%s where order_id=%s",
                    (self.ordername.get(), self.ordertype.get(), self.orderquantity.get(), self.orderdate.get(),
                     self.orderid.get()))
                messagebox.showinfo("updation Sucess", "Sucess, Order is Updated")
                self.connection.commit()
        except Exception as er:
            print("Error!", f"{er}")

    def vieworderui(self):
        row = []
        root1 = tk.Tk()
        root1.title("orders")
        root1.geometry("1070x450")
        columns = ('order_id', 'order_name', 'order_type', 'order_quantity', 'order_date', 'order_status')
        viewtree = ttk.Treeview(root1, columns=columns, show='headings', height=30)
        viewtree.pack()
        viewtree.heading('order_id', text='Order Id')
        viewtree.heading('order_name', text='Order Name')
        viewtree.heading('order_type', text='Order Payment Type')
        viewtree.heading('order_quantity', text='Order Quantity')
        viewtree.heading('order_date', text='Order Date')
        viewtree.heading('order_status', text='Order Status')
        viewtree.column("order_id", width=100, anchor=CENTER)
        viewtree.column("order_name", width=120, anchor=CENTER)
        viewtree.column('order_type', width=120, anchor=CENTER)
        viewtree.column('order_quantity', width=120, anchor=CENTER)
        viewtree.column('order_date', width=120, anchor=CENTER)
        viewtree.column('order_status', width=120, anchor=CENTER)
        viewtree.pack(pady=30)
        try:
            self.cur.execute(
                "select order_id, order_name, order_type, order_quantity, order_date, order_status from orders".format(
                    self.myuid))
            row = self.cur.fetchall()
            if row == None:
                messagebox.showinfo("No Orders", "orders is empty")
        except Exception as er:
            print("Error!", f"{er}")
        for val in row:
            viewtree.insert(parent='', index='end', text='', values=(val[0], val[1], val[2], val[3], val[4], val[5]))

        # style
        style = ttk.Style()
        style.theme_use("default")
        style.map("Viewtree")

        root1.mainloop()

    def deleteorderui(self):
        self.clearwindow()
        lb_user = Label(self.frame3, text="Enter Order Id", font=("Goudy old Style", 15), bg="goldenrod",
                        fg="white").place(x=8, y=230)
        self.cancelorderid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.cancelorderid.place(x=250, y=235)
        closework = Button(self.frame3, command=self.cancelorder, text="Cancel", font=("bold", 17), bg="steel blue",
                           fg="white")
        closework.place(x=100, y=333, height=35, width=130)

    def cancelorder(self):
        if self.cancelorderid.get() == "":
            messagebox.showerror("Error!", "All fields are required")
        else:
            try:
                self.cur.execute("select * from orders where order_id=%s", (self.cancelorderid.get()))
                row = self.cur.fetchone()
                if row != None:
                    self.cur.execute(
                        "update orders set order_status='canceled' where order_id=%s",
                        (self.cancelorderid.get()))
                    messagebox.showinfo("Canceled", "Sucess, Order cancel is successful")
                    self.connection.commit()
            except Exception as er:
                print("Error!", f"{er}")

    #damagereport ui
    def damagerepui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Damage Report", font=("Oblique", 20), bg="goldenrod")
        title.place(x=10, y=2)
        rep_damage_but = Button(self.frame3, command=self.reportDamui, text="Report Damage")
        rep_damage_but.place(x=20, y=60, height=50, width=160)
        Tak_act_but = Button(self.frame3, command=self.acttakrep, text="Take Action on Rep")
        Tak_act_but.place(x=20, y=120, height=50, width=160)
        pastdam_but = Button(self.frame3, command=self.pastDamrepui, text="Past Damage report ")
        pastdam_but.place(x=20, y=180, height=50, width=160)

    def reportDamui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Report Damage", font=("Oblique", 20), bg="goldenrod")
        title.place(x=10, y=2)
        l_repid = Label(self.frame3, text="New Report Id", font=("Goudy old Style", 15), bg="goldenrod").place(x=10,y=50)
        self.repid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.repid.place(x=210, y=55)

        l_repdesp = Label(self.frame3, text="Description", font=("Goudy old Style", 15), bg="goldenrod").place(x=10, y=80)
        self.repdesp = Text(self.frame3, font=("times new roman", 12), bg="white")
        self.repdesp.place(x=10, y=115, width=450,height=270)

        save = Button(self.frame3, command=self.reportDam, text="Save", bg="white", font=("times new roman", 13))
        save.place(x=10, y=410)
        cancel = Button(self.frame3, command=self.clearwindow, text="Cancel", bg="white",
                        font=("times new roman", 13))
        cancel.place(x=80, y=410)

    def reportDam(self):
        x = str(datetime.datetime.now())
        date_time_obj = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
        x_date = date_time_obj.date()
        self.repdesp.get(1.0, END)
        if self.repdesp.get(1.0, END) == "" or self.repid.get() == "":
            messagebox.showerror("Error!", "All fields are required")
        else:
            try:
                self.cur.execute("select * from damagereport where report_id=%s", (self.repid.get()))
                row = self.cur.fetchone()
                if row != None:
                    messagebox.showerror("Error!", "Id Already assigned\nGive new Report id")
                else:
                    self.cur.execute(
                        "INSERT INTO DAMAGEREPORT (REPORT_ID, REP_BY, REP_DESC,REP_DATE) VALUES(%s,%s,%s,%s)",
                        (self.repid.get(), self.myuid, self.repdesp.get(1.0, END), x_date))
                    messagebox.showinfo("Inserstion Sucess", "Sucess, Damage is reported")
                    self.connection.commit()
            except Exception as er:
                print("Error!", f"{er}")

    def pastDamrepui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Past Reported Damages", font=("Oblique", 20), bg="goldenrod")
        title.place(x=10, y=2)
        view_past_report = Button(self.frame3, command=self.pastrepui, text="View Past Reported",
                                  font=("times new roman", 14))
        view_past_report.place(x=20, y=80)
        edit_past_report = Button(self.frame3, command=self.updatepastrepui, text="Edit past Report",
                                  font=("times new roman", 14))
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
        viewtree.pack(pady=70)
        try:
            self.cur.execute(
                "select report_id, rep_desc, rep_date from damagereport where rep_by='{}' order by rep_date ASC".format(
                    self.myuid))
            row = self.cur.fetchall()
            if row == []:
                messagebox.showinfo("No Report", "No Damages Reported")
        except Exception as er:
            print("Error!", f"{er}")
        for val in row:
            viewtree.insert(parent='', index='end', text='', values=(val[0], val[1], val[2]))
        # style
        style = ttk.Style()
        style.theme_use("default")
        style.map("viewtree")


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
        self.clearwindow()
        title = Label(self.frame3, text="Take action", font=("Oblique", 20), bg="goldenrod")
        title.place(x=10, y=2)
        title2 = Label(self.frame3,text="Add action taken for incomplete damages",font=("Oblique", 12), bg="goldenrod")
        title2.place(x=10,y=40)
        title3 = Label(self.frame3,text="Reports, needed Add action taken",font=("Oblique", 12), bg="goldenrod")
        title3.place(x=10,y=70)
        row = []
        columns = ('report_id', 'rep_desc', 'rep_by', 'rep_date')
        viewtree = ttk.Treeview(self.frame3, columns=columns, show='headings', height=10)
        viewtree.heading('report_id', text='Report Id')
        viewtree.heading('rep_desc', text='Report Descrption')
        viewtree.heading('rep_by', text='Reported By')
        viewtree.heading('rep_date', text='Reported Date')

        viewtree.column("report_id", width=100, anchor=CENTER)
        viewtree.column("rep_desc", width=450, anchor=CENTER)
        viewtree.column('rep_date', width=120, anchor=CENTER)
        viewtree.column('rep_by', width=100, anchor=CENTER)
        viewtree.pack(pady=30)
        try:
            self.cur.execute(
                "select * from damagereport where act_taken_by is null Order by report_id ASC".format(
                    self.myuid))
            row = self.cur.fetchall()
            if row == []:
                messagebox.showinfo("No Report", "No Damages Reported")
        except Exception as er:
            print("Error!", f"{er}")
        for val in row:
            viewtree.insert(parent='', index='end', text='', values=(val[0], val[2], val[1],val[3]))
        # style
        style = ttk.Style()
        style.theme_use("default")
        style.map("viewtree")
        viewtree.grid(padx=10,pady=110)
        but_ref = Button(self.frame3,command=self.acttakrep,text='Refresh',font=('New times roman',14))
        but_ref.place(x=10,y=340)

        title = Label(self.frame3, text="Add Report Damage", font=("Oblique", 15), bg="goldenrod")
        title.place(x=10, y=380)
        l_repdesp = Label(self.frame3, text="Add Action", font=("Goudy old Style", 15), bg="goldenrod")
        l_repdesp.place(x=10, y=420)

        l_repid = Label(self.frame3, text="Enter Report Id", font=("Goudy old Style", 15), bg="goldenrod")
        l_repid.place(x=10, y=420)
        self.repid1 = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.repid1.place(x=230, y=425)
        l_label = Label(self.frame3, text="Enter Action taken", font=("Goudy old Style", 15), bg="goldenrod")
        l_label.place(x=10, y=450)
        self.actdesp = Text(self.frame3, font=("times new roman", 12), bg="white")
        self.actdesp.place(x=10, y=490, width=400, height=200)

        save = Button(self.frame3, command=self.addact, text="Save", bg="white", font=("times new roman", 13))
        save.place(x=700, y=650)
        cancel = Button(self.frame3, command=self.damagerepui, text="Cancel", bg="white",
                        font=("times new roman", 13))
        cancel.place(x=700, y=650)

    def addact(self):
        x = str(datetime.datetime.now())
        date_time_obj = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
        x_date = date_time_obj.date()
        repid = self.repid1.get()
        acttake = self.actdesp.get(1.0,END)
        myid = self.myuid
        if repid == "":
            messagebox.showerror('No Value', "Descrption, Report Id Fields Not to be Empty")
        else:
            try:
                self.cur.execute("update damagereport set action=%s, act_taken_by=%s, act_date=%s where report_id=%s",(acttake, myid, x_date,repid))
                self.connection.commit()
                messagebox.showinfo('Sucess', "Report updation sucess")
            except Exception as er:
                print("Error!", f"{er}")




    def deletepastreport(self):
        self.clearwindow()
        title = Label(self.frame3, text="delete damage Reported", font=("Oblique", 20), bg="goldenrod")
        title.place(x=10, y=2)
        lb_user = Label(self.frame3, text="Enter report Id", font=("Goudy old Style", 15), bg="goldenrod").place(x=10, y=70)
        self.drepid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.drepid.place(x=170, y=75)
        drepidbu = Button(self.frame3, command=self.delcheckdam, text="Check")
        drepidbu.place(x=370, y=70)

    def delcheckdam(self):
        if self.drepid.get() == '':
            messagebox.showerror('No Value', "Report Id Field Not Empty")
        else:
            try:
                self.cur.execute("select report_id, rep_by from damagereport where report_id=%s and rep_by=%s",
                                 (self.drepid.get(), self.myuid))
                row = self.cur.fetchall()

                if row == []:
                    messagebox.showinfo("No Damage Reported", "No Damage reported for Given id")
                else:
                    messagebox.showinfo('ID Present', "Given Id present click ok to delete description report")
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
        title = Label(self.frame3, text="change my password", font=("Oblique", 20), bg="goldenrod")
        title.place(x=10, y=2)
        lb_user = Label(self.frame3, text="Current password", font=("Goudy old Style", 15), bg="goldenrod").place(x=10, y=50)
        self.cpass = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.cpass.place(x=210, y=55)
        lb_user = Label(self.frame3, text="New password", font=("Goudy old Style", 15), bg="goldenrod").place(x=10, y=80)
        self.newpass = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.newpass.place(x=210, y=85)
        lb_user = Label(self.frame3, text="Re-enter password ", font=("Goudy old Style", 15), bg="goldenrod").place(x=10, y=110)
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



def main(uid,passd):
    root = Tk()
    obj = stockkeeper(root,uid,passd)
    root.mainloop()

main('stoc001','0001')