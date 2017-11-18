'''listener thread
'''
# from socket import socket, AF_INET, SOCK_STREAM
import ServerData
from threading import Thread, Event
import socket
import time, sys
class ListenerThread(Thread):
    '''Thread to listen to the incoming clients'''
    def __init__(self):
        Thread.__init__(self)
        self.listener_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        PORT=5005
        self.listener_socket.bind(("155.246.202.104", PORT))
        #print(socket.gethostname())
        print(self.listener_socket)
        self.listener_socket.listen(5)
        #self.listener_socket.settimeout(0.5)
        self.switch = Event()
        self.switch.clear()
        self.serverdata = ServerData.ServerData()
        print("listener thread initalizing")
    def run(self):
        ''' listen to the incoming connections indefinitely'''
        while(not self.switch.is_set()):
            print("in listener loop")
            #time.sleep(1)
            client_socket,addr = self.listener_socket.accept()
            #print(sys.exc_info()[0])
            print("connected to {}".format(addr))
            # set the timeout for the client socket
            client_socket.settimeout(0.5)
            # send the list of connected devices to the newly connected socket
            self.serverdata.send_connecteds(client_socket)
            # send the new connected devices to all the other connected devices
            send_data = "online {}".format(client_socket.getpeername()[0])
            send_data = send_data.encode('utf-8')
            for sockets in self.serverdata.socket_list:
                soc_data = ServerData.SocData(sockets, send_data)
                self.serverdata.send_queue.put(soc_data)

            # add the new socket to the socket ist with lock
            self.serverdata.sockets_lock.acquire()
            self.serverdata.socket_list.add(client_socket)
            self.serverdata.sockets_lock.release()
    def off(self):
        self.switch.set()
    
