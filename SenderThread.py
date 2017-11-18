'''class for sending the data'''

import ServerData
from queue import Queue, Empty
import socket
from threading import Thread, Event

class SenderThread(Thread):
    '''Thread class to send the data'''
    def __init__(self):
        self.switch = Event()
        self.switch.clear()
        Thread.__init__(self)
        self.serverdata = ServerData.ServerData()
        
    def run(self):
        '''send the data to the client indefinitly'''
        while(not self.switch.is_set()):
            try:
                data = self.serverdata.send_queue.get(timeout=1)
            except Empty as e: pass
            else:
                data.send_socket.send(data.send_data)
                
    def off(self):
        self.switch.set()
