import psycopg2
import otherclass

class worker:
    def __init__(self, cur, myuid, mypass):
        self.cur = cur
        self.myuid = myuid
        self.mypass = mypass
        self.jcard = otherclass.jobcard(self.cur, self.myuid)
        self.repdam = otherclass.damage_Report(self.cur,self.myuid)

    def updateMyPassword(self,newpass):
        if self.myuid == "" or self.mypass == "":
            print("Error!", "All fields are required")
        else:
            try:
                self.cur.execute("select * from login where userid=%s and password=%s",
                            (self.myuid, self.mypass))
                row = self.cur.fetchone()
                if row == None:
                    print("Error!", "Invalid userid & PASSWORD")
                else:
                    try:
                        self.cur.execute("update login set password=%s where userid=%s and seckey=%s",
                                    (newpass, self.myuid, self.mypass))
                        print("password changed")
                    except Exception as er:
                        print("Erro", f"{er}")
            except Exception as er:
                print("Erro", f"{er}")

    def view_mywork(self):
        self.jcard.view_job_card(self.myuid)

    def report_damage(self):
        self.repdam.reportDamage()



def main():
    connection = psycopg2.connect(host="localhost", user="postgres", password="root",
                                  database="inveMSys")
    cur = connection.cursor()
    userid = input("input userid: ")
    upass = input("input password: ")
    addcs = worker(cur,userid,upass)
    addcs.report_damage()
    connection.commit()
    connection.close()

main()
