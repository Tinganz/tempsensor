import serial
import time

file_name = "templates/serial.html" 

serial_port = '/dev/cu.usbmodem1301'
baudrate = 9600

page_title = "Temperature Sensor"

s = None

def write_page(data_list):
    fo = open(file_name,"w+",encoding='utf-8')
    fo.write("<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.01//EN' 'http://www.w3.org/TR/html4/strict.dtd'>")
    fo.write("<html><head><title>"+page_title+"</title>")
    fo.write("<meta http-equiv='refresh' content='1'>")
    fo.write("<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'>")
    # fo.write("<link rel='shortcut icon' href='/static/images/favicon.ico' />")
    # fo.write("<link rel='icon' type='image/x-icon' href='/static/images/favicon.ico' />")
    fo.write("<link rel='icon' type='image/png' href='/static/images/favicon.png' />")
    fo.write("</head><body><center><p>"+page_title+"</p>")
    fo.write("<table border='1' border-spacing='5' style='text-align:center;'>")
    fo.write("<tr><th>Sensor ID</th><th>Temperature</th></tr>")
    for i in range(0,len(data_list),2):
        fo.write("<tr>")
        fo.write("<td>"+data_list[i]+"</td>")
        fo.write("<td>")
        fo.write(data_list[i+1])
        fo.write("</font></td>")
        fo.write("</tr>")
    fo.write("</table>")
    fo.write("</body>")
    fo.write("</html>")
    fo.close()

def init():
    global s
    s = serial.Serial(serial_port,baudrate) 
    s.dtr = 0 
    s.dtr = 1
    print("Waiting for data...");
    time.sleep(2) 
    s.reset_input_buffer()


def refresh():
    global s
    data_str = s.readline().decode('utf-8')
    # data_str = "Sensor 1:25.87°C:"
    data_str = data_str.replace('\r','') 
    data_str = data_str.replace('\n','') 
    data_str += 'Sensor 9:25.00°C:'
    print(data_str)
    data_list = data_str.split(":")
    del data_list[len(data_list)-1]
    write_page(data_list)
    return data_list

def ReadyToRead():
    global s
    return s.in_waiting > 0