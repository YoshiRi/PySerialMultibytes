import serial

try:
    ser = serial.Serial('/dev/ttyUSB0',115200,bytesize=8,stopbits=1,timeout=2,xonxoff=True, rtscts=True, write_timeout=2, dsrdtr=False, inter_byte_timeout=None)
    
except:
    print("Error!")
    

while True:
    line = ser.readline()
    print(line)
    
ser.close()



##
# ser = serial.Serial('/dev/ttyUSB0',115200,bytesize=8,stopbits=1,timeout=2,write_timeout =2)
# 
