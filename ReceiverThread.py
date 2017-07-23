import ServerData
from queue import Queue, Empty
from threading import Thread, Event

class ReceicerThread(Thread):
    '''Thread to receive data'''
    def __init__(self):
        super.__init__(self)
        self.serverdata = ServerData.ServerData()
        self.switch = Event()
        self.switch.clear()


    def start(self):
        ''' thread to receive the data from all the sockets'''
        while not self.switch.is_set():
            for sockets in self.serverdata.socket_list:
                data = sockets.receive()
                socdata=ServerData.SocData(sockets,data)
                self.serverdata.received_queue.put(socdata)

                
    def off(self):
        self.switch.set()
            
