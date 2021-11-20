#fichero que activa el enchufe TAPO P100 
#https://www.amazon.es/TP-Link-Tapo-P100-Inteligente-Concentrador/dp/B07Z5JD3T4


from PyP100 import PyP100
p100 = PyP100.P100("192.168.1.128", "tu_email@gmail.com", "tu_clave") #Creating a P100 plug object
p100.handshake() #Creates the cookies required for further methods 
p100.login() #Sends credentials to the plug and creates AES Key and IV for further methods
p100.turnOn() #Sends the turn on request
#p100.setBrightness(100) #Sends the set brightness request
#p100.turnOff() #Sends the turn off request
a=p100.getDeviceInfo() #Returns dict with all the device info
print(a)
