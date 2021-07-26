import serial
import time

Scom= serial.Serial('COM4',9600)
Scom.timeout=1

def run():
    while True:
        i=input("command --> ").lower().strip()
        if (i=="go"):
            print("byeeee")
            break
        Scom.write(i.encode())
        time.sleep(0.7)
        print(Scom.readline().decode("ascii"))
    Scom.close()

run()