from GSM import PDU

class SMS():

    csa = "00881665900005"
    dest = 0
    msg = ''


    def __init__(self, dest, msg ):

        self.dest = dest
        self.msg = msg

    def send(self):
        print( "Sending to ", self.dest )
        print( "Message: ", self.msg )
