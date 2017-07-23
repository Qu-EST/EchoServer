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
    
class ServerData(Metaclsss = Singelton):
    '''class contains the data needed for the server
    '''
    def __init__(self):
        socket_list = {,}
        send_queue = Queue(0)
        received_queue = Queue(0)

class SendData(object):
    ''' data object to be passed to the sender thread'''
    def __init__(self):
        self.send_socket=None
        self.send_data=None
        
