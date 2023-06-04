#Importing Necessary Modules
import pyautogui
import subprocess 
import time
import serial 
import serial.tools.list_ports


#Running Edge And Shorts Page 
subprocess.run(["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",f"www.youtube.com/shorts"])

#Moving Mouse To Scroll Button
'''pyautogui.moveTo(1800, 1010, duration = 1)'''

#Debugging
'''print (pyautogui.size())
print(pyautogui.position())
pyautogui.moveTo(1800, 1000, duration = 1)'''

#Rate Limiter
time.sleep(2)

#Get Port Data

com_port = None

ports = serial.tools.list_ports.comports()

'''for port in ports:
    if "GyroScroll" in port.description:
        com_port = port.device
        break

if com_port is None:
    print("Port Finding Failed...Please Configure Manually.")
    exit()'''

port= serial.Serial(com_port,baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,timeout=1)

#Loop Forever
while True:
    
    #Read Port Data And Parse To A String
    data = port.readline().decode().strip()
    
    #Get Data In Integer Form
    
    print(data)
    #a = (data)
    
    try:
        a = int(data)
    except:
        a = 0
    
    #Click When Condition Satisfied
    if(a == 1):
        pyautogui.scroll(-200)
        print("Success")

        