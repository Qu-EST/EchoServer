# from socket import socket, AF_INET, SOCK_STREAM
import ServerData
from threading import Thread, Event
import socket
class ListenerThread(Thread):
    '''Thread to listen to the incoming clients'''
    def __init__(self):
        super.__init__(self)
        self.listener_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        PORT=5005
        self.listener_socket.bind(socket.gethostname(), PORT)
        self.listener_socket.listen(2)
        self.switch = Event()
        self.switch.clear()
        self.serverdata = ServerData.ServerData()

    def start(self):
        ''' listen to the incoming connections indefinitely'''
        while(not self.switch.is_set()):
            client_socket,addr = self.listener_socket.accept()
            print("connected to {}".format(addr))
            self.serverdata.socket_list.add(client_socket))
            
    def off(self):
        self.switch.set()
    
