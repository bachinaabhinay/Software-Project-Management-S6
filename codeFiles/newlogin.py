import psycopg2

class login:

    def __init__(self,uname,upass,secKey):
        self.uname = uname
        self.upass = upass
        self.secKey = secKey

    def loginV(self):
        if self.uname == "" or self.upass == "":
            print("Error!", "All fields are required")
        else:
            try:
                connection = psycopg2.connect(host="localhost", user="postgres", password="root",
                                              database="inveMSys")
                cur = connection.cursor()
                cur.execute("select * from login where username=%s and password=%s",
                            (self.uname, self.upass))
                row = cur.fetchone()
                if row == None:
                    print("Error!", "Invalid USERNAME & PASSWORD")
                else:
                    print("Success", "Welcome, login success")

                    connection.close()

            except Exception as e:
                print("Error!", f"Error due to {str(e)}")

    def updateDetails(self,newpass):
        global connection
        if self.uname == "" or self.secKey == "":
            print("Error!", "All fields are required")
        else:
            try:
                connection = psycopg2.connect(host="localhost", user="postgres", password="root",
                                              database="inveMSys")
                cur = connection.cursor()
                cur.execute("select * from login where username=%s and seckey=%s",
                            (self.uname, self.secKey))
                row = cur.fetchone()
                if row == None:
                    print("Error!", "Invalid USERNAME & PASSWORD")
                else:
                    try:
                        cur.execute("update login set password=%s where username=%s and seckey=%s",
                                    (newpass, self.uname, self.secKey))
                        print("password changed")
                        connection.commit()
                    except Exception as er:
                        print("Error!", f"{er}")
            except Exception as er:
                print("Error!", f"{er}")
                connection.close()


uname = input("Input UserNeme: ")
upass = input("Input Password: ")
secKey = input("Input Secert key: ")
loginc = login(uname,upass,secKey)
loginc.updateDetails(input("Input New password: "))
