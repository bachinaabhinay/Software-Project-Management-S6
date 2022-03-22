import psycopg2


class admin:
    def __init__(self,cur, myuid, mypass):
        self.cur = cur
        self.myuid = myuid
        self.mypass = mypass

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
                        print("Error!", f"{er}")
            except Exception as er:
                print("Error!", f"{er}")

    def addusers(self):
        name = input("Input name: ")
        role = input("input role: ")
        userid = input("Input new Userid: ")
        password = input("Input password")
        seckey = input("Input secert Key: ")
        try:
            self.cur.execute("INSERT INTO EMPLOYEE (name, role, userid) VALUES(%s,%s,%s)", (name,role,userid))
            self.cur.execute("INSERT INTO login (userid, password, seckey) VALUES(%s,%s,%s)", (userid,password,seckey))
            print("Values Inserted")
        except Exception as er:
            print("Error!", f"{er}")


def main():
    connection = psycopg2.connect(host="localhost", user="postgres", password="root",
                                  database="inveMSys")
    cur = connection.cursor()
    userid = input("Input Userid: ")
    upass = input("Input Password: ")
    addcs = admin(cur,userid,upass)
    addcs.addusers()
    connection.commit()
    connection.close()

main()
