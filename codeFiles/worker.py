import psycopg2

class worker:
    def __init__(self,cur, myuid, mypass):
        self.cur = cur
        self.myuid = myuid
        self.mypass = mypass

    def updateMyPassword(self,newpass):

        if self.myuid == "" or self.mypass == "":
            print("Error!", "All fields are required")
        else:
            try:
                self.cur.execute("select * from login where username=%s and password=%s",
                            (self.myuid, self.mypass))
                row = self.cur.fetchone()
                if row == None:
                    print("Error!", "Invalid USERNAME & PASSWORD")
                else:
                    try:
                        self.cur.execute("update login set password=%s where username=%s and seckey=%s",
                                    (newpass, self.myuid, self.mypass))
                        print("password changed")
                    except Exception as er:
                        print("Error!", f"{er}")
            except Exception as er:
                print("Error!", f"{er}")

    def addwork(self):
        pass 


def main():
    connection = psycopg2.connect(host="localhost", user="postgres", password="root",
                                  database="inveMSys")
    cur = connection.cursor()
    uname = input("Input UserNeme: ")
    upass = input("Input Password: ")
    addcs = worker(cur,uname,upass)
    addcs.updateMyPassword(input("newpassword: "))
    connection.commit()
    connection.close()