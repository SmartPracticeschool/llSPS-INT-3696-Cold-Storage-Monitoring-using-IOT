import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
#Provide your IBM Watson Device Credentials
organization = "nbpn1e"
deviceType = "arduino"
deviceId = "12345678"
authMethod = "token"
authToken = "87654321"

a=0
#optimum temperature
temp=12

def func1():
        listOfGlobals = globals()
        listOfGlobals['a'] = 1

def func2():
        listOfGlobals = globals()
        listOfGlobals['a'] = 0

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)#Commands
        print(type(cmd.data))
        i=cmd.data['command']
        if i=='motor on':
                func1()
        elif i=='motor off':
                func2()
                
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()


deviceCli.connect()




while True:

        if a==0 :
                ldr=random.randint(50,300)
                #print ldr sensor value
                hum=random.randint(75,90)
                #print(hum)
                temp=int(temp)
                temp =str(temp+1)
                temp=(temp.zfill(2))                
                #Send Temperature, Humidity & Ldr to IBM Watson
                data = { 'Temperature' : temp, 'Humidity': hum, 'LDR': ldr }
                #print (data)
                def myOnPublishCallback():
                        print ("Published Temperature = %s C" % temp, "Humidity = %s %%" % hum, "LDR = %s " % ldr, "to IBM Watson")

                success = deviceCli.publishEvent("Weather", "json", data, qos=0, on_publish=myOnPublishCallback)
                if not success:
                        print("Not connected to IoTF")
                time.sleep(10)

                deviceCli.commandCallback = myCommandCallback
        

        elif a==1 :
                ldr=random.randint(50, 300)
                #print ldr sensor value
                hum=random.randint(75, 90)
                #print(hum)
                temp=int(temp)
                temp =str(temp-1)
                temp=(temp.zfill(2))
                #Send Temperature, Humidity & Ldr to IBM Watson
                data = { 'Temperature' : temp, 'Humidity': hum, 'LDR': ldr }
                #print (data)
                def myOnPublishCallback():
                        print ("Published Temperature = %s C" % temp, "Humidity = %s %%" % hum, "LDR = %s " % ldr, "to IBM Watson")
                success = deviceCli.publishEvent("Weather", "json", data, qos=0, on_publish=myOnPublishCallback)
                if not success:
                        print("Not connected to IoTF")
                time.sleep(10)

                deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
