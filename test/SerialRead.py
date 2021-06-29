import serial
import time
import os
import xmlformatter
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
for i in range(0,3):
	os.system("printf '%s\n' '1m6' 'wq' | ed -s test-results.xml")

formatter = xmlformatter.Formatter(indent="1", indent_char="\t", encoding_output="UTF-8", preserve=["literal"])
xmldata = formatter.format_file("test-results.xml")
xmldata.decode() 
f3 = open('test-results.xml', 'wb+')
f3.write(xmldata)
f3.close()
ser.close()
exit()
