'''interface all the modules in the tool
and communicate with the world using CLI'''
import ServerData
import SenderThread
import ReceiverThread
import ListenerThread
import threading

serverdata = ServerData.ServerData()
off = False
listener = None
sender = None
receiver = None

def start_server():
    print("starting the server")
    global listener, sender, receiver
    listener=ListenerThread.ListenerThread()
    listener.start()
    sender=SenderThread.SenderThread()
    sender.start()
    receiver=ReceiverThread.ReceiverThread()
    receiver.start()

def connected_devices():
    print("listing the connected devices")
    

def list_threads():
    print("listing the open threads")
    print(threading.enumerate())

def stop_server():
    print("stopting the server")
    global off
    off = True
    
while not off:
    option = input('1. start server 2. list connected devices 3. list threads 4. stop server')
    print("Yout option is {}".format(option))
    if option is "1":
        start_server()
    elif option is "2":
        connected_devices()
    elif option is "3":
        list_threads()
    elif option is "4":
        stop_server()
        
