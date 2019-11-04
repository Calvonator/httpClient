import http.client
import urllib.request
import socket
import time
#Establishes http connection to Ubuntu Apache server (192.168.56.101)[Running off host-only network Virtual Box] using three different modules (http.client, urllib and socket)

#Burp Suite Proxy
proxy = "127.0.0.1"
proxyPort = 8080


def myHttpProxy(address):                   #HTTP proxy connection using http.client module
    
    x = time.time()                                                                     #records time before connection for later calculation of connection duration
    connection = http.client.HTTPConnection(proxy, proxyPort)                           #Creates connection to the Burp Suite Proxy (localhost:8080)
    connection.set_tunnel(str(address))                                                 #Endpoint connection (Actual website visted) from after proxy connection
    print("Connection object: " + str(connection))                                      #Prints byte object of the connection object
    connection.request("GET", "/")                                                      #Request sent along the established connection (Requesting home page)
    response = connection.getresponse()                                                 #Stores response to the request using the getresponse() method
    print('Status: {} and reason {}'.format(response.status, response.reason))          #Prints the status/reason sent in the response using status() and reason() methods on the response object
    connection.close()                                                                  #Closes HTTP connection object
    z = time.time()                                                                     #Records time just after closing of the connection
    threadTime = z - x                                                                  #Calculates difference between x and y to find duration of the connection
    print("Thread took " + str(threadTime) + " seconds\n")


def myHttp(address):                        #Creates HTTP connection without proxy using http.client module
    
    x = time.time() 
    connection = http.client.HTTPConnection(str(address), 80, timeout=20)               #Creates connection object to the specified address (No proxy so the endpoint can be placed here instead of in .set_tunnel())
    print("Connection object: " + str(connection))  
    connection.request("GET", "/")
    response = connection.getresponse()
    print('Status: {} and reason {}'.format(response.status, response.reason))
    connection.close()
    z = time.time()
    threadTime = z - x
    print("Thread took " + str(threadTime) + " seconds\n")


def mySocket(address):                      #Creates a HTTP socket connection using socket module
    x = time.time()
    request = "GET / HTTP/1.1\r\nHost:" + str(address) + "\r\n\r\n"                     #Request string and header formulated with specified address
    sock = socket.socket()                                                              #Creates the socket object using the socket.socket() method
    sock.connect((str(address), 80))                                                    #Socket connection establised with specified address using port 80(HTTP)
    sock.send(request.encode('utf-8'))                                                  #The request is sent through the socket connection using the 'utf-8' encoding
    response = sock.recv(4096)                                                          #The first 4096 byte block of the response is received using the recv() method
    z = time.time()
    threadTime = z - x
    print("Thread took " + str(threadTime) + " seconds\n")
    while (len(response) > 0):                                                          #While loop used to see if there was a response
        print(response)                                                                 #Prints first block of the response
        response = sock.recv(4096)                                                      #Attempts to receive another 4096 byte block of the response
    z = time.time()
    threadTime = z - x
    print("Thread took " + str(threadTime) + " seconds\n")

def mySocketProxy(address):                 #Creats a HTTP socket connection to Proxy Server, from there a request is sent to the specified address
    x = time.time()
    request = "GET http://" + str(address) + "/ HTTP/1.1\r\nHost:" + str(address) + "\r\n\r\n" #Request string and header formulated with specified endpoint address
    sock = socket.socket()                                                              
    sock.connect((proxy, proxyPort))                                                      #Socket connection establised with proxy server using the proxy global variables
    sock.send(request.encode('utf-8'))                                                  
    response = sock.recv(4096)                                                          
    z = time.time()
    threadTime = z - x
    print("Thread took " + str(threadTime) + " seconds\n")
    while (len(response) > 0):                                                          
        print(response)                                                                 
        response = sock.recv(4096)                                                      
    z = time.time()
    threadTime = z - x
    print("Thread took " + str(threadTime) + " seconds\n")



def myUrllib(address):                      #Creates a HTTP connection using the urllib module
        x = time.time()     
        homePage = urllib.request.urlopen(str(address)).read()                          #Creates a connection and sends basic request to the specified address using urllib.request.urlopen() and receives response using read() 
        print("HTML: " + str(homePage))                                                 #Prints response of the request by printing the homePage object
        z = time.time()
        threadTime = z - x
        print("Thread took " + str(threadTime) + " seconds\n")


loopControl = 1
while(loopControl == 1):
    
    choice = input("HTTP[proxy], Socket[proxy] or URLLIB[proxy] connection?")
    
    if str.lower(choice) == 'http':
        addyChoice = input("Address please: ")
        if addyChoice == '1':
            addyChoice = '192.168.56.101'
        myHttp(addyChoice)
        choice = ' '
    elif str.lower(choice) == 'httpproxy':
        addyChoice = input("Address please: ")
        if addyChoice == '1':
            addyChoice = '192.168.56.101'
        myHttpProxy(addyChoice)
        choice = ' '
    
    elif str.lower(choice) == 'socket':
        addyChoice = input("Address please: ('http://') ")
        if addyChoice == '1':
            addyChoice = '192.168.56.101'
        mySocket(addyChoice)
        choice = ' '

    elif str.lower(choice) == 'socketproxy':
        addyChoice = input("Address please: ('http://') ")
        if addyChoice == '1':
            addyChoice = '192.168.56.101'
        mySocketProxy(addyChoice)
        choice = ' '
        
    elif str.lower(choice) == 'urllib':
        addyChoice = input("Address please: ")
        if addyChoice == '1':
            addyChoice = '192.168.56.101'
        myUrllib(addyChoice)
        choice = ' '
        
    elif str.lower(choice) == 'q':
        loopControl = 0
