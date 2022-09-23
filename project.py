from playsound import playsound
import random

while True:

    temp=random.randint(0,100)
    humidity=random.randint(0,100)
    if(temp > 40)  and (humidity > 50) :
        if(temp > 40):
            print("Temperature is high", temp)
            playsound("sound.mp3")
        elif(humidity>50):
            print("Humidity is high",humidity)
            playsound("sound.mp3")

    else:
        print("Temprature and humidity is normal",temp, humidity)
        