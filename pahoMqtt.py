import paho.mqtt.client as mqtt #import the client1


broker_address="maqiatto.com" 
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1") #create new instance
client.username_pw_set(username="worldomo@gmail.com",password="Worldomo@4321")
client.connect(broker_address) #connect to broker
client.publish("worldomo@gmail.com/test","OFF")#publish
