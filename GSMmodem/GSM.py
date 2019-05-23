import binascii
import Numerical

class PDU():
    csa = '881665900006' # Default to Iridium GMDSS CSA
    mode = 0             # Default to PDU
    dest_type = '91'     # Default to "International"
    dest = 0
    user_data = ''
    validity = ''

    size = 0

    def encode(self):

        SMSC_info_len = '00' # 00 = SMSC info in phone to be used
        first_octet = '11'   #
        tp_msgref = '00'     # Constatn, fixed
        dest_len = self.len_in_hex(self.dest)
        dest_num = self.semi_oct_encode(self.dest)
        tp_pid = '00'
        tp_dcs = '00'  #00 7 bit, 02 8 bit
        tp_validity = 'AA'
        tp_userdata =  self.gsm_encode( self.user_data).decode("utf-8").upper()


        pdu_str = '{:s}{:s}{:s}{:s}{:s}{:s}{:s}{:s}{:s}{:s}{:s}'.format(
            SMSC_info_len,
            first_octet,
            tp_msgref,
            dest_len,
            self.dest_type,
            dest_num,
            tp_pid,
            tp_dcs,
            tp_validity,
            '{:x}'.format( len(tp_userdata) ).upper(),
            tp_userdata
        )

        return pdu_str


    def len_in_hex(self, num_str):

        len_str = str(hex(len(num_str)))
        len_str = len_str[2:5]

        if Numerical.is_odd( len(len_str) ):
            len_str = '0' + len_str.upper()

        return len_str



    def semi_oct_encode(self, num_str):

        enc_str = ''

        if Numerical.is_odd(len(num_str)):
            num_str = num_str + 'F'

        characters = list(num_str)
        while len(characters) > 0:

            second = characters.pop()
            first = characters.pop()

            enc_str = second + first + enc_str

        return enc_str



    def gsm_encode(self, plaintext):

        gsm = ("@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ\x1bÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?"
               "¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ`¿abcdefghijklmnopqrstuvwxyzäöñüà")
        ext = ("````````````````````^```````````````````{}`````\\````````````[~]`"
               "|````````````````````````````````````€``````````````````````````")

        res = bytearray()
        for c in plaintext:
            idx= gsm.find(c);
            if idx != -1:
                res.append(idx)
                continue
            idx = ext.find(c)
            if idx != -1:
                res.append(27)
                res.append(idx)

        return binascii.hexlify(res)
