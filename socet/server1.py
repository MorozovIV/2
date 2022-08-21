import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        if self.data == b'1':
            print('+')
        elif self.data == b'2':
            print('++')
        else:
            print('-')

        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())
if __name__ == "__main__":
    HOST, PORT = "10.0.10.200", 1234

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()