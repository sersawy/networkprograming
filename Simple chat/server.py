from socket import *

s = socket (AF_INET, SOCK_STREAM)

host = "127.0.0.1"
port = 7000

s.bind((host, port))
s.listen(5)
c,ad = s.accept()
print("Connection From ",ad[0])

while True:
    x = c.recv(2048)
    print("client :", x.decode('utf=8'))
    if (x == 'Q'):
        break
    
s.close()
