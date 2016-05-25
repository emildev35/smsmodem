import serial


modem = serial.Serial('/dev/ttyUSB2', 9600)
buffer = ''
while True:
    modem.write('AT+CMGF=1')
    # if '\n' in buffer:
    #     pass
    # else:
    buffer += modem.read(1)
    buffer += modem.read(modem.inWaiting())
    print buffer