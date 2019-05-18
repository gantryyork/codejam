import binascii

class PDU():
    csa = '00881665900005'
    mode = 0
    dest_type = '91'
    dest = 0
    user_data = ''
    validity = ''

    size = 0

    def encode(self):

        SMSC_info_len = '00'
        first_octet = '11'
        tp_msgref = '00'
        dest_len = self.len_in_oct(self.dest)
        dest_num = self.semi_oct_encode(self.dest)
        tp_pid = '00'
        tp_dcs = '00'  #00 7 bit, 02 8 bit
        tp_validity = 'AA'
        tp_userdate_len = 'ww'
        tp_userdata = self.gsm_encode( self.user_data)


        pdu_str = SMSC_info_len \
            + first_octet \
            + tp_msgref + ' '\
            + dest_len + ' '\
            + self.dest_type + ' '\
            + dest_num + ' ' \
            + tp_pid \
            + tp_dcs \
            + tp_validity \
            + tp_userdate_len \
            + tp_userdata \

        return pdu_str


    def is_odd(self, num):
        if num/2 == int(num/2):
            return False
        else:
            return True

    def len_in_oct(self, num_str):

        len_str = str(hex(len(num_str)))
        len_str = len_str[2:5]

        if self.is_odd( len(len_str) ):
            len_str = '0' + len_str.upper()

        return len_str


    def semi_oct_encode(self, num_str):

        enc_str = ''

        if self.is_odd(len(num_str)):
            num_str = num_str + 'F'

        characters = list(num_str)
        while len(characters) > 0:

            second = characters.pop()
            first = characters.pop()

            enc_str = second + first + enc_str

        return enc_str


    gsm = ("@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ\x1bÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?"
           "¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ`¿abcdefghijklmnopqrstuvwxyzäöñüà")
    ext = ("````````````````````^```````````````````{}`````\\````````````[~]`"
           "|````````````````````````````````````€``````````````````````````")

    def gsm_encode(self, plaintext):
        res = bytearray()
        for c in plaintext:
            idx = gsm.find(c);
            if idx != -1:
                res.append(idx)
                continue
            idx = ext.find(c)
            if idx != -1:
                res.append(27)
                res.append(idx)
        print( res )
        return binascii.hexlify(res)
