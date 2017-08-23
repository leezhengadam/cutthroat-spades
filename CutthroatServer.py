import socket
import time
import json


def main():
    # create a socket object
    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostname()

    port = 9999

    # bind to the port
    print "binding to " + host + " at port " + str(port)
    server_socket.bind((host, port))

    # queue up to 20 requests
    server_socket.listen(20)
    # set a timeout on the socket
    server_socket.settimeout(.1)

    while True:
        try:
            # establish a connection
            client_socket, addr = server_socket.accept()

            # no timeout so we got a connection
            print("Got a connection from %s" % str(addr))
            data = json.dumps({'connected': 'true'})
            client_socket.send(data)
            client_socket.close()
        except socket.timeout:
            # got no connection, we don't care
            pass

        try:
            server_socket.recv(1024)
        except socket.timeout:
            # got no message, we don't care
            pass

if __name__ == '__main__':
    main()
