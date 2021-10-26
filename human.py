import cv2
import paho.mqtt.client as mqtt #import the client1
import keyboard


def detect(frame):
    bounding_box_cordinates, weights =  HOGCV.detectMultiScale(frame, winStride = (4, 4), padding = (8, 8), scale = 1.03)
    
    person = 1
    for x,y,w,h in bounding_box_cordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, f'person {person}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        person += 1
        client.publish("worldomo@gmail.com/test","Total Persons="+str(person) )#publish
    
    cv2.putText(frame, 'Status : Detecting ', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.putText(frame, f'Total Persons : {person-1}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.imshow('output', frame)
    return frame
       
        
def Detect():   
    video = cv2.VideoCapture(0)
    print('Detecting people...')

    while True:
        check, frame = video.read()
        frame = detect(frame)
        key = cv2.waitKey(1)
        if keyboard.is_pressed("q"):
            print("ending loop")
            break

    video.release()
    cv2.destroyAllWindows()

    
if __name__ == "__main__":
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    broker_address="maqiatto.com" 
    #broker_address="iot.eclipse.org" #use external broker
    client = mqtt.Client("P1") #create new instance
    client.username_pw_set(username="worldomo@gmail.com",password="Worldomo@0000")
    client.connect(broker_address) #connect to broker
    Detect()
