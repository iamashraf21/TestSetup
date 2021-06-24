import serial
import time
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)  # open serial port

while True:
	data = ser.readline().decode('ascii')
	if(data[0:1] == "<"):
		f = open('test-results.xml', 'a')
		f.write(data)
	print (data.rstrip("\r\n"))
	f = open('test.log','a')
	f.write(data)
	if(data == '</test-run>'):
		break
ser.close()
exit()
