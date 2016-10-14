'''
Created on Oct 12, 2016

@author: amolsaurabh
'''

import sys
import socket
import thread

class clSocket:

    def __init__(self):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def clSocket_bind(self,port=34567):
        self.soc.bind((str(socket.INADDR_ANY),port))
        self.soc.listen(50)
        
    def clSocket_connect(self,host = "localhost",port=34567):
        self.soc.connect((host,port))

    def clSocket_recv(self,size=1024):
        x = self.soc.recv(size)
        print x

    def clSocket_send(self,Msg = None):
        self.soc.send(Msg)
    
    def clSocket_close(self):
        self.soc.close()
    

def handle_client(client, address):
    print address
    while True:
        print "receiving from port {0}".format(address)
        m = client.recv(1024)
        print m
        client.send(m)
        if ( m == "exit" or m == ""):
            print "Client {0} disconnected".format(address)
            break
            
if __name__ == '__main__':
    
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        raise AssertionError("Please pass port as argument")
    
    while True:
        print "1. Client"
        print "2. server (Can't exit)"
        print "3. Exit"
        choice = raw_input("Enter your choice")
        if choice == "1":
            mySocket = clSocket()
            host = raw_input("enter hostname or IP : ")
            mySocket.clSocket_connect(host,int(sys.argv[1]))
            while True:
                m = raw_input("Enter your msg ('exit' to exit) :")
                mySocket.clSocket_send(m)
                mySocket.clSocket_recv()
                if m == "exit":
                    print "exiting"
                    mySocket.clSocket_close()
                    break
        elif choice == "2":
            mySocket = clSocket()
            mySocket.clSocket_bind(int(sys.argv[1]))
            while True:
                client, address = mySocket.soc.accept()
                thread.start_new_thread(handle_client, (client,address))    
        elif choice=="3":
            sys.exit()
        else:
            print "wrong choice"

            
        
    
    
    
    