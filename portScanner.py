import socket 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "137.74.187.100" #https://www.hackthissite.org/
port = int(input("Which port do you wish to check?: "))
def portScanner(port):
    if s.connect_ex((host,port)):
        print("Port is closed")
    else:
        print("Port open")
portScanner(port)