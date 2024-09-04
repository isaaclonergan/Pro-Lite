import serial
import datetime

def checkSettings():
    try:
        open("settings.txt", "r")
        print("File Exists")
    except:
        file = open("settings.txt", "w")
        file.write("ID: 01\nport: COM1\nbaudrate: 9600\nbytesize: 8\nparity: N\nstopbits: 1")
        file.close()
        print("settings.txt created.")

def readSettings():
    with open("settings.txt","r") as file:
        id = file[0].split()[1]
        port = file[1].split()[1]
        baudrate = int(file[2].split()[1])
        bytesize = int(file[3].split()[1])
        parity = file[4].split()[1]
        stopbits = int(file[5].split()[1])
        file.close()
    array = [id,port, baudrate, bytesize, parity, stopbits]
    return array

def setupSerial():
    global s
    global id
    arr = readSettings()
    id = arr[0]
    s = serial.Serial(arr[1],arr[2],arr[3],arr[4],arr[5])

def crlf():
    s.write(13) #character return
    s.write(10) #line feed

def setClock():
    message = "T" + datetime.date.today()
    s.write("T")

def main():
    checkSettings()
    setupSerial()
    setClock()

if __name__ == '__main__':
    main()