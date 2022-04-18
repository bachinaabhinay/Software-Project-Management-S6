from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import showinfo
import psycopg2
import tkinter as tk
import datetime
from datetime import date

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
        order_button = Button(self.frame2, command=self.orderui, text="Orders", activebackground="cyan", font=(40))
        order_button.place(x=20, y=290, height=50, width=150)
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
        jobcardupdate_button = Button(self.frame3, command=self.assignworkui, text="Assign Work", activebackground="orange", font=(40))
        jobcardupdate_button.place(x=130, y=155, height=45, width=150)

    def jobcardviewui(self):
        row = []
        root1 = tk.Tk()
        root1.title("work")
        root1.geometry("1070x450")
        columns = ('jobid', 'workDesc', 'status', 'assignby', 'assigndate')
        viewtree = ttk.Treeview(root1, columns=columns, show='headings', height=30)
        viewtree.pack()
        viewtree.heading('jobid', text='Job Id')
        viewtree.heading('workDesc', text='work Description')
        viewtree.heading('status', text='work Status')
        viewtree.heading('assignby', text='Assign By')
        viewtree.heading('assigndate', text='Assign Date')
        viewtree.column("jobid", width=100, anchor=CENTER)
        viewtree.column("workDesc", width=550, anchor=CENTER)
        viewtree.column('status', width=120, anchor=CENTER)
        viewtree.column('assignby', width=120, anchor=CENTER)
        viewtree.column('assigndate', width=120, anchor=CENTER)
        viewtree.pack(pady=30)
        try:
            self.cur.execute(
                "select jobid, workdesc, status, assignby, assigndate from jobcard".format(
                    self.myuid))
            row = self.cur.fetchall()
            if row == None:
                messagebox.showinfo("No Work", "No assigned work")
        except Exception as er:
            print("Error!", f"{er}")
        for val in row:
            viewtree.insert(parent='', index='end', text='', values=(val[0], val[1], val[2], val[3], val[4]))

        # style
        style = ttk.Style()
        style.theme_use("default")
        style.map("Viewtree")

        root1.mainloop()

    def assignworkui(self):
        lb_user = Label(self.frame3, text="Enter job Id", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=8, y=230)
        self.jobid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.jobid.place(x=220, y=235)
        lb_user1 = Label(self.frame3, text="Work Description", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=8, y=280)
        self.workdesc = Text(self.frame3, font=("times new roman", 12), bg="white")
        self.workdesc.place(x=220, y=285,width=220,height=30)
        lb_user2 = Label(self.frame3, text="Worker Id", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=8, y=330)
        self.assigntoo = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.assigntoo.place(x=220, y=335)
        closework = Button(self.frame3,command=self.assignwork, text="Assign", font=("bold",17), bg="steel blue", fg="white")
        closework.place(x=100, y=413, height=35, width=130)

    def assignwork(self):
        x = str(datetime.datetime.now())
        date_time_obj = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
        x_date = date_time_obj.date()
        if self.workdesc.get(1.0, END) == "" or self.jobid.get() == "" or self.assigntoo.get() == "":
            messagebox.showerror("Error!", "All fields are required")
        else:
            try:
                self.cur.execute("select * from jobcard where jobid=%s", (self.jobid.get()))
                row = self.cur.fetchone()
                if row != None:
                    messagebox.showerror("Error!", "Id Already assigned\nGive new Job id")
                else:
                    self.cur.execute(
                        "INSERT INTO jobcard (jobid, workdesc, assignby, assignto, assigndate) VALUES(%s,%s,%s,%s,%s)",
                        (self.jobid.get(), self.workdesc.get(1.0, END), self.myuid, self.assigntoo.get(),
                         x_date))
                    messagebox.showinfo("Assigned Sucess", "Sucess, Job is Assigned")
                    self.connection.commit()
            except Exception as er:
                print("Error!", f"{er}")

    def inventoryui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Inventory", font=("Oblique", 20), bg="Gray35", fg="white")
        title.place(x=10, y=2)
        inventoryview_button = Button(self.frame3,command=self.inventoryviewui, text="View", activebackground="orange", font=(40))
        inventoryview_button.place(x=130, y=85, height=45, width=150)
        inventoryupdate_button = Button(self.frame3, command=self.inventoryupdateui, text="Update", activebackground="orange", font=(40))
        inventoryupdate_button.place(x=130, y=155, height=45, width=150)
        inventoryreport_button = Button(self.frame3, command=self.inventoryreportui, text="Report", activebackground="orange", font=(40))
        inventoryreport_button.place(x=530, y=85, height=45, width=150)
        inventoryaddnew_button = Button(self.frame3, command=self.inventoryaddnewui, text="Add new", activebackground="orange", font=(40))
        inventoryaddnew_button.place(x=530, y=155, height=45, width=150)

    def inventoryviewui(self):
        row = []
        root1 = tk.Tk()
        root1.title("Inventory")
        root1.geometry("1070x450")
        columns = ('inventoryid', 'inventoryitems', 'inventorydesc', 'inventoryprice', 'inventorynumber','inventoryexpiry','inventoryarriveddate')
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
            viewtree.insert(parent='', index='end', text='', values=(val[0], val[1], val[2], val[3], val[4], val[5], val[6]))

        # style
        style = ttk.Style()
        style.theme_use("default")
        style.map("Viewtree")

        root1.mainloop()

    def inventoryupdateui(self):
        self.clearwindow()
        lb_user = Label(self.frame3, text="Enter Inventory Id", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=8, y=230)
        self.inventoryid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventoryid.place(x=250, y=235)
        lb_user1 = Label(self.frame3, text="Enter Inventory Items", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=8, y=280)
        self.inventoryitems = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventoryitems.place(x=250, y=285)
        lb_user2 = Label(self.frame3, text="Enter Inventory Description", font=("Goudy old Style", 15), bg="Gray35",fg="white").place(x=8, y=330)
        self.inventorydesc = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventorydesc.place(x=250, y=335)
        lb_user3 = Label(self.frame3, text="Enter Inventory Price", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=8, y=380)
        self.inventoryprice = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventoryprice.place(x=250, y=385)
        lb_user4 = Label(self.frame3, text="Enter Inventory Number", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=8, y=430)
        self.inventorynumber = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventorynumber.place(x=250, y=435)
        lb_user5 = Label(self.frame3, text="Enter Inventory Expiry", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=8, y=480)
        self.inventoryexpiry = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventoryexpiry.place(x=250, y=485)
        closework = Button(self.frame3, command=self.inventoryupdate, text="Update", font=("bold", 17), bg="steel blue",fg="white")
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
                        (self.inventoryitems.get(), self.inventorydesc.get(), self.inventoryprice.get(), self.inventorynumber.get(), self.inventoryexpiry.get(), self.inventoryid.get()))
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
        columns = ('itemid', 'itemname', 'itemquantity')
        viewtree = ttk.Treeview(root1, columns=columns, show='headings', height=30)
        viewtree.pack()
        viewtree.heading('itemid', text='Item Id')
        viewtree.heading('itemname', text='Item Name')
        viewtree.heading('itemquantity', text='Remaining Quantity')
        viewtree.column("itemid", width=120, anchor=CENTER)
        viewtree.column("itemname", width=120, anchor=CENTER)
        viewtree.column('itemquantity', width=120, anchor=CENTER)
        viewtree.pack(pady=30)
        try:
            self.cur.execute(
                "select item_id, item_name, item_quantity from producttable".format(
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

    def inventoryaddnewui(self):
        self.clearwindow()
        lb_user = Label(self.frame3, text="Enter Inventory Id", font=("Goudy old Style", 15), bg="Gray35",
                        fg="white").place(x=8, y=230)
        self.inventoryid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventoryid.place(x=250, y=235)
        lb_user1 = Label(self.frame3, text="Enter Inventory Items", font=("Goudy old Style", 15), bg="Gray35",
                         fg="white").place(x=8, y=280)
        self.inventoryitems = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventoryitems.place(x=250, y=285)
        lb_user2 = Label(self.frame3, text="Enter Inventory Description", font=("Goudy old Style", 15), bg="Gray35",
                         fg="white").place(x=8, y=330)
        self.inventorydesc = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventorydesc.place(x=250, y=335)
        lb_user3 = Label(self.frame3, text="Enter Inventory Price", font=("Goudy old Style", 15), bg="Gray35",
                         fg="white").place(x=8, y=380)
        self.inventoryprice = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventoryprice.place(x=250, y=385)
        lb_user4 = Label(self.frame3, text="Enter Inventory Number", font=("Goudy old Style", 15), bg="Gray35",
                         fg="white").place(x=8, y=430)
        self.inventorynumber = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.inventorynumber.place(x=250, y=435)
        lb_user5 = Label(self.frame3, text="Enter Inventory Expiry", font=("Goudy old Style", 15), bg="Gray35",
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
                        (self.inventoryid.get(), self.inventoryitems.get(), self.inventorydesc.get(), self.inventoryprice.get(), self.inventorynumber.get(), self.inventoryexpiry.get(),x_date))
                    messagebox.showinfo("Added Sucess", "Sucess, Added to Inventory")
                    self.connection.commit()
            except Exception as er:
                print("Error!", f"{er}")

    def orderui(self):
        self.clearwindow()
        title = Label(self.frame3, text="Order", font=("Oblique", 20), bg="Gray35", fg="white")
        title.place(x=10, y=2)
        orderview_button = Button(self.frame3,command=self.orderviewui, text="View", activebackground="orange", font=(40))
        orderview_button.place(x=130, y=85, height=45, width=150)
        orderupdate_button = Button(self.frame3, command=self.orderupdateui, text="Update", activebackground="orange", font=(40))
        orderupdate_button.place(x=130, y=155, height=45, width=150)
        generateorder_button = Button(self.frame3, command=self.generateorderui, text="Generate Order", activebackground="orange", font=(40))
        generateorder_button.place(x=530, y=85, height=45, width=150)
        cancelorder_button = Button(self.frame3, command=self.cancelorderui, text="Cancel Order", activebackground="orange", font=(40))
        cancelorder_button.place(x=530, y=155, height=45, width=150)

    def orderviewui(self):
            row = []
            root1 = tk.Tk()
            root1.title("orders")
            root1.geometry("1070x450")
            columns = ('order_id', 'order_name', 'order_type', 'order_quantity', 'order_date','order_status')
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

    def orderupdateui(self):
        self.clearwindow()
        lb_user = Label(self.frame3, text="Enter Order Id", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=8, y=230)
        self.orderid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.orderid.place(x=250, y=235)
        lb_user1 = Label(self.frame3, text="Enter Order Name", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=8, y=280)
        self.ordername = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.ordername.place(x=250, y=285)
        lb_user2 = Label(self.frame3, text="Enter Payment Type", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=8, y=330)
        self.ordertype = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.ordertype.place(x=250, y=335)
        lb_user3 = Label(self.frame3, text="Enter Order Quantity", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=8, y=380)
        self.orderquantity = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.orderquantity.place(x=250, y=385)
        lb_user4 = Label(self.frame3, text="Enter Order Date", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=8, y=430)
        self.orderdate = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.orderdate.place(x=250, y=435)
        closework = Button(self.frame3, command=self.orderupdate, text="Update", font=("bold", 17), bg="steel blue", fg="white")
        closework.place(x=100, y=503, height=35, width=130)

    def orderupdate(self):
        try:
            self.cur.execute("select * from orders where order_id=%s", (self.orderid.get()))
            row = self.cur.fetchone()
            if row != None:
                self.cur.execute(
                    "update orders set order_name=%s, order_type=%s, order_quantity=%s, order_date=%s where order_id=%s",
                    (self.ordername.get(), self.ordertype.get(), self.orderquantity.get(), self.orderdate.get(), self.orderid.get()))
                messagebox.showinfo("updation Sucess", "Sucess, Order is Updated")
                self.connection.commit()
        except Exception as er:
            print("Error!", f"{er}")



    def generateorderui(self):
        self.clearwindow()
        lb_user = Label(self.frame3, text="Enter Order Id", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=8, y=230)
        self.orderid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.orderid.place(x=250, y=235)
        closework = Button(self.frame3, command=self.generateorder, text="Generate", font=("bold", 17), bg="steel blue", fg="white")
        closework.place(x=100, y=333, height=35, width=130)

    def generateorder(self):
        if self.orderid.get() == "":
            messagebox.showerror("Error!", "All fields are required")
        else:
            try:
                self.cur.execute("select * from orders where order_id=%s", (self.orderid.get()))
                row = self.cur.fetchone()
                if row != None:
                    self.cur.execute(
                        "SELECT CASE WHEN inventorynumber > 0 THEN inventorynumber ELSE 0 END AS inventorynumber FROM (SELECT (inventory.inventorynumber) - (SELECT (orders.order_quantity) FROM orders WHERE order_id = %s) as inventorynumber FROM inventory WHERE inventory .inventoryid = 1) alias;",
                        (self.orderid.get()))
                    messagebox.showinfo("Generated", "Sucess, Order Generated successfully")
                    row1 = self.cur.fetchone()
                    self.cur.execute(
                    "update producttable set item_quantity=%s where item_id=1",
                    (row1))
                    self.cur.execute(
                        "update orders set order_status='completed' WHERE order_id = %s",
                        (self.orderid.get()))
                    self.connection.commit()
            except Exception as er:
                print("Error!", f"{er}")



    def cancelorderui(self):
        self.clearwindow()
        lb_user = Label(self.frame3, text="Enter Order Id", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=8, y=230)
        self.cancelorderid = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.cancelorderid.place(x=250, y=235)
        closework = Button(self.frame3, command=self.cancelorder, text="Cancel", font=("bold", 17), bg="steel blue", fg="white")
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
        title = Label(self.frame3, text="change my password", font=("Oblique", 20), bg="Gray35", fg="white" )
        title.place(x=10, y=2)
        lb_user = Label(self.frame3, text="Current password", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=10, y=50)
        self.cpass = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.cpass.place(x=210, y=55)
        lb_user = Label(self.frame3, text="New password", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=10, y=80)
        self.newpass = Entry(self.frame3, font=("times new roman", 12), bg="white")
        self.newpass.place(x=210, y=85)
        lb_user = Label(self.frame3, text="Re-enter password ", font=("Goudy old Style", 15), bg="Gray35", fg="white").place(x=10, y=110)
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