import ServerData
from queue import Queue, Empty
from threading import Thread, Event
import socket

class ReceiverThread(Thread):
    '''Thread to receive data'''
    def __init__(self):
        super.__init__(self)
        self.serverdata = ServerData.ServerData()
        self.switch = Event()
        self.switch.clear()


    def start(self):
        ''' thread to receive the data from all the sockets'''
        while not self.switch.is_set():
            
            for sockets in self.serverdata.socket_list: # access the list with lock
                try:
                    data = sockets.receive() # make it non-blocking, exception for receiving from a closed socket
                except socket.timeout:
                    pass#print("socket timeout exception")
                except ConnectionResetError:
                    print("connection reset error, disconnecting")
                    self.disconnect(sockets)
                except OSError as e:
                    print("From received processor. got the error:{} hence disconnecting".format(e))
                    self.disconnect(sockets)
                else:
                    data = data.decode('utf-8')
                    if(data == 'online'):
                        self.serverdata.send_connecteds(sockets)
                    if(data == ' '):
                        self.disconnect(sockets)


    def disconnect(self, dis_soc):

        # remove the diconeccted socket fromt the list
        self.serverdata.sockets_lock.acquire()
        self.serverdata.socket_list.remove(dis_soc)
        self.serverdata.sockets_lock.release()

        # inform all the connected sockets about the disconnected socket
        send_data = "offline {}".format(dis_soc.getpeername()[0])
        send_data =send_data.encode('utf-8')
        for sockets in self.serverdata.socket_list:
            soc_data = ServerData.SocData(sockets, send_data)
            self.serverdata.send_queue.put(soc_data)
        

                
    def off(self):
        self.switch.set()
            
