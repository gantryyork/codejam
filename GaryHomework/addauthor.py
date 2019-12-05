
import mysql.connector


def addauthor(username,dbname,dbpasswd,port):

    db1 = mysql.connector.connect(user=username,database=dbname,password=passwd,host="localhost",port=server.local_bind_port)

    cursor1 = db1.cursor(prepared=True)

    fname = input("Please type the authors first name")

    lname = input("Please type the authors last name")

    checkAuthor = """SELECT author_id,firstname,lastname from grauthors
    WHERE firstname = (%s) and lastname = (%s)"""

    cursor1.execute(checkAuthor,(fname,lname))
    rows = cursor1.fetchall()

    if cursor1.rowcount == 0:
    #print "We should do the insert here"
        cursor2 = db1.cursor(prepared=True)
        insertauthor = """INSERT INTO grauthors (firstname,lastname) values (%s,%s)"""
        cursor2.execute(insertauthor,(fname,lname))
        db1.commit()
    else:
        print("That user already exists")
        db1.close()
