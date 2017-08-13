'''
Server data 
'''
from queue import Queue
from threading import RLock
class Singelton(type):
    '''Metaclsss for the singleton'''
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singelton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class ServerData(metaclass = Singelton):
    '''class contains the data needed for the server
    '''
    def __init__(self, *args, **kwargs):
        self.socket_list = set()
        self.send_queue = Queue(0)
        self.received_queue = Queue(0)
        self.sockets_lock = RLock()

    def send_connecteds(self, send_socket):
        for sockets in self.socket_list:
            send_data = "online {}".format(sockets.getpeername()[0])
            send_data = send_data.encode('utf-8')
            soc_data = SocData(send_socket, send_data)
            self.send_queue.put(soc_data)
            
class SocData(object):
    ''' data object to be passed to the sender thread'''
    def __init__(self, socket,data):
        self.send_socket = socket
        self.send_data = data
        
