from socket import *
import sys 
import random

def main():
    p = float(sys.argv[1])
    random.seed(sys.argv[2])
    try:
        serverPort = 61234
        serverSocket = socket(AF_INET, SOCK_DGRAM)
        serverSocket.bind(('', serverPort))
        print ("The server is ready to receive")
        while True:
            message, clientAddress = serverSocket.recvfrom(2048)
            if random.random() <= p: 
                print(message.decode().strip(), "-> dropped")
                msg = 'dropped'
                sc1 = 301
                tempRes = str(msg) + " " + str(sc1)
                serverSocket.sendto(tempRes.encode(), clientAddress)
            else:
                modifiedMsg = message.decode()
                op, int1, int2 = modifiedMsg.split()
                if ('.' in int1) or ('.' in int2):
                    statusCode = 630
                    res = -1
                    print(modifiedMsg.strip(),"->",statusCode,res)
                    finalRes = str(res) + " " + str(statusCode)
                    serverSocket.sendto(finalRes.encode(), clientAddress)
                else:
                    num1 = int(int1)
                    num2 = int(int2)
                    if isValid(op) and isValidNums(num1) and isValidNums(num2):
                        res = preformOperations(op, num1, num2)
                        statusCode = 200
                    elif not (isValid(op)):
                        statusCode = 620
                        res = -1
                    elif op == '/' and int2 == 0:
                        statusCode = 630
                        res = -1
                    print(modifiedMsg.strip(),"->",statusCode,res)
                    finalRes = str(res) + " " + str(statusCode)
                    serverSocket.sendto(finalRes.encode(), clientAddress)
    except KeyboardInterrupt:
        print("connection closed")
        return


def isValid(operationCode): 
    if(not(operationCode == '+' or operationCode == '-' or operationCode == '/' or operationCode == '*')):
        return False
    else:
        return True


def preformOperations(op, int1, int2):
    if op == '+':
        return int1 + int2
    elif op == '-':
        return int1 - int2
    elif op == '*':
        return int1 * int2
    elif op == '/':
        return int1 / int2

def isValidNums(num): 
    if(isinstance(num, int)):
        return True
    else: 
        return False

if __name__ == "__main__":
    main()