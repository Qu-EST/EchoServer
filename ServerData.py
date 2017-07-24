'''
Server data 
'''
from queue import Queue

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

class SocData(object):
    ''' data object to be passed to the sender thread'''
    def __init__(self, socket,data):
        self.send_socket=socket
        self.send_data=data
        
