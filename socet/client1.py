import socket
import sys

HOST, PORT = "10.0.10.200", 1234
data = " ".join(sys.argv[1:])
print(data)

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
   # sock.sendall(bytes(data + "\n", "utf-8"))
    sock.sendall(bytes("1", "utf-8")) #Данные тут(нешифрованно)

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))