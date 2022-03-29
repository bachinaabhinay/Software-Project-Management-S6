class jobcard:
    def __init__(self,cur,userid):
        self.userid  = userid
        self.cur = cur

    def view_job_card(self, assignby, x=0):
        if x==0:
            try:
                self.cur.execute("select assigndate, jobid, workdesc, status, assignby from jobcard where assignto=%s",
                                 (self.userid))
                row = self.cur.fetchall()
                print(row)
            except Exception as er:
                print("Error!", f"{er}")
        else:
            try:
                self.cur.execute("select assigndate, jobid, workdesc, status from jobcard where assignto=%s and assignby=%s",
                                 (self.userid,assignby))
                row = self.cur.fetchall()
                print(row)
            except Exception as er:
                print("Error!", f"{er}")

    def add_job_card(self):
        pass

    def update_job_card(self):
        pass

class damage_Report:
    def __init__(self, cur, userid):
        self.userid = userid
        self.cur = cur

    def reportDamage(self):
        repid = input("Input report Id")
        rep_by = self.userid
        rep_desc = input("input descrption: ")
        rep_date = input("date")
        try:
            self.cur.execute("INSERT INTO damagereport (reportid, rep_by, rep_descrp, rep_date) VALUES(%s,%s,%s,%s)", (repid,rep_by,rep_desc,rep_date))
            print("Values Inserted")
        except Exception as er:
            print("Error!", f"{er}")

    def updateReport(self):
        repid = input("Input report Id")
        status = input("Input status")
        try:
            self.cur.execute("UPDATE damagereport set status=%s where reportid=%s", (status, repid))
            print("Values Inserted")
        except Exception as er:
            print("Error!", f"{er}")

    def viewReport(self):
        repid = input("Input report Id")
        try:
            self.cur.execute("SELECT * FROM DAMAGEREPORT WHERE repid = %s", (repid))
            print("Values Inserted")
        except Exception as er:
            print("Error!", f"{er}")

class order:
    def __init__(self):
        pass

class inventory:
    def __init__(self):
        pass
