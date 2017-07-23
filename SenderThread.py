'''class for sending the data'''

import Serverdata
from queue import Queue
import socket
from threading import Thread, Event

class SenderThread(Thread):
    '''Thread class to send the data'''
    def init(self):
        super.__init__(self)
        self.serverdata=ServerData.ServerData()
        self.switch=Event()
        self.switch.clear()
    def start(self):
        '''send the data to the client indefinitly'''
        pass
    def off(self):
        self.swtich.set()
