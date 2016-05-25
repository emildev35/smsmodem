from gsmmodem.modem import GsmModem


def print_sms(sms):
    print dir(sms)

def handleSms(sms):
    print dir(sms)

PORT = '/dev/ttyUSB2'
modem = GsmModem(PORT, 9600, smsReceivedCallbackFunc=handleSms)
# modem = GsmModem(PORT, 9600)
modem.smsTextMode = True
modem.connect(5910)

modem.sendSms('+59172038768', 'sadfadfsfd')

print modem.imei
print modem.networkName

# def lineStartingWith(string, lines):
#     """ Searches through the specified list of strings and returns the 
#     first line starting with the specified search string, or None if not found
#     """
#     for line in lines:
#         if line.startswith(string):
#             return line
#     else:
#         return None

# modem.write('AT+CMGS="{0}"'.format('+59172038768'), timeout=3, expectedResponseTermSeq='> ')
# result = lineStartingWith('+CMGS:', modem.write('sdfdsfsdfds', timeout=15, writeTerm=chr(26)))
# print result