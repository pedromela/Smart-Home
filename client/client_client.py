import socket
import ssl
import sys
import getpass

TCP_IP = '192.168.2.1'
TCP_PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_addr = (TCP_IP,TCP_PORT)

ssl_sock = ssl.wrap_socket(sock,
                           ca_certs="server.crt",
                           cert_reqs=ssl.CERT_REQUIRED)

print >>sys.stderr, '[C] connecting to: %s; port: %s' % client_addr
ssl_sock.connect(client_addr)
logged = False
r = ssl_sock.recv(1024)
print "[C] received:", r
if r == "Please Log In":
    user = raw_input('username:')
    pas = getpass.getpass('password:')
    s = "login "+ user + " " + pas
    ssl_sock.sendall(s)
else:
    s = "Something went wrong... Exiting"
    print s
    ssl_sock.sendall(s)
    ssl_cock.close()
    exit()
r = ssl_sock.recv(1024)
print "[C] received:", r
if r == "Login Failed":
    s = "Login Failed. Exiting..."
    print "[C] sending:", s
    ssl_sock.sendall(s)
    ssl_sock.close()
    exit()
elif r == "Login ERROR":
    s = "Login format was wrong"
    print "[C] sending:", s
    ssl_sock.sendall(s)
    ssl_sock.close()
    exit()
elif r == "Login True":
    logged = True
    s = "Logged In"
    ssl_sock.sendall(s)
else:
    s = "Something went wrong. Exiting"
    print "[C] sending:", s
    ssl_sock.sendall(s)
    ssl_sock.close()
    exit()
if not logged:
    print "Max attempts reached..."
    ssl_sock.close()
    exit()
 
try:
  while True:
    r = ssl_sock.recv(1024)
    print "[C] received:", r

    s = raw_input()
    print "[C] sending:", s
    ssl_sock.sendall(s)

    r = ssl_sock.recv(1024)
    print "[C] received answer:", r
    
    if s == "q" or s == "exit":
      break
  
finally:
  print >>sys.stderr, '[C] closing socket'
  ssl_sock.close()
