from socket import *
import time 
import sys

def main():
    content = open(sys.argv[1], 'r')
    for line in content:
        if not(line == ""):
            d = 0.1
            serverName = '127.0.0.1'
            serverPort = 61234
            clientSocket = socket(AF_INET, SOCK_DGRAM)
            clientSocket.sendto(line.encode(),(serverName, serverPort))
            reply, serverAddress = clientSocket.recvfrom(2048)
            res, statusCode = reply.split()
            while(res.decode() == 'dropped'):
                time.sleep(d)
                d = 2 * d
                if (d > 2):
                    print("Error 300: Request timed out: the server is dead")
                    break
                else: 
                    print("Request timed out: resending")
                    clientSocket.sendto(line.encode(),(serverName, serverPort))
                    reply, serverAddress = clientSocket.recvfrom(2048)
                    res, statusCode = reply.split()
            sc = int(statusCode)
            if(sc == 200):
                print("Result is ", res.decode())
            elif(sc == 630):
                print("Error 630: Invalid operands")
            elif(sc == 620):
                print("Error 620: Invalid operation code")
        else:
            clientSocket.close()    
    clientSocket.close()
    content.close()

if __name__ == "__main__":
    main()