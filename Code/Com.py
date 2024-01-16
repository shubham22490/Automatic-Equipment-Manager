import serial


# Class to setup communication between raspberry pi and code.
class Com:
    def __init__(self, port):
        self.serial = serial.Serial(port, 115200)

    def getData(self):
        self.serial.write(b"send\n")
        while True:
            reply = self.serial.readline()
            if(len(reply) > 2):
                data =  reply.decode('utf-8').strip()
                return ([int(data[1]), int(data[3]), int(data[5])])
            
    def sendData(self, data):
        data = f"t{data[0]}s{data[1]}c{data[2]}\n"
        self.serial.write(data.encode('utf-8'))
