
from addauthor import addauthor
from sshtunnel import SSHTunnelForwarder

# Example based on https://dev.mysql.com/doc/connector-python/en/connector-python-tutorial-cursorbuffered.html
# http://www.mysqltutorial.org/getting-started-mysql-python-connector/

with open("stuff.inc") as pwfile:
    mydata = pwfile.readline()
    mydata = mydata.rstrip('\n')
    dblist = mydata.split(" ")
    print(dblist)
with SSHTunnelForwarder(("nbtl.mesacc.edu",22),ssh_password = dblist[3],ssh_username = dblist[1],remote_bind_address =("localhost",3306)) as server:
    addauthor.addauthor(dblist[1],dblist[2].dblist[0],server.local_bind_port)


