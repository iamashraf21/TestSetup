import serial
import time
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)  # open serial port
f1 = open('test-results.xml', 'w+')
f2 = open('test.log','w+')

while True:
	data = ser.readline().decode('ascii')
	if(data[0:1] == "<"):
		f1.write(data)
	print (data.rstrip("\r\n"))
	f2.write(data)
	if(data == '</test-run>'):
		break

f1.close()
f2.close()

ser.close()
exit()
