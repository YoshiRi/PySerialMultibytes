import serial
import struct
import time

class Ser_mbyte():
    def __init__(self,PORT='/dev/ttyUSB0'):
        self.ser = serial.Serial(PORT,115200,bytesize=8,stopbits=1,timeout=2,write_timeout =2)
        
    def sendfloat(self,data):
        #print(data)
        sdata = struct.pack('>f', float(data))
        self.ser.write(sdata)
       
    def sendfloats(self,datalist):
        sdatalist = ''
        for data in datalist:
            sdatalist = sdatalist+struct.pack('>f',float(data))
        self.ser.write(sdatalist)
        
    
    def __del__(self):
        self.ser.close()


if __name__ == '__main__':
    ser = Ser_mbyte()
    start = time.time()
    
    while True:
        try:
            now = time.time() - start
            ser.sendfloat(now)
            time.sleep(0.001)# 1ms sleep
            print(now)
            
        except KeyboardInterrupt:
            break
