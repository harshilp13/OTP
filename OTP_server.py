import socket
import random


def sumOfDigits(num):
    sum = 0

    while num != 0:
        sum = sum + int(num % 10)
        num = int(num / 10)
    
    return sum

def equate(num):
    return (3 * (num * num)) - (9 * num) + 2 


s = socket.socket()

host = socket.gethostname()
port = 12345    

s.bind((host,port))

s.listen(5)
c,addr = s.accept()
print("Connection received from %s" % addr[0])

users = {}

while True:

    receive_command = c.recv(1024).decode().split()
    print(receive_command)

    if receive_command[0] == 'r':
        users[receive_command[1]] = int(receive_command[2])
        c.send(b"[+] User successfully registered")

    elif receive_command[0] == 'l':
        userid = receive_command[1]
        x = random.randint(10,99)
        print("Random value generated %s" % x)

        c.send((str(x)).encode())

        val = int(c.recv(1024).decode())

        if users[userid] == 1:
            print("Value Received %s and computed value %s" % (val,x+1))
            if val == x+1:
                c.send("[+] Login Successful".encode())
            else:
                c.send("[-] Login Unsuccessful".encode())
        elif users[userid] == 2:
            print("Value Received %s and computed value %s" % (val,sumOfDigits(x)))
            if val == sumOfDigits(x):
                c.send("[+] Login Successful".encode())
            else:
                c.send("[-] Login Unsuccessful".encode())
        else:
            print("Value Received %s and computed value %s" % (val,equate(x)))
            if val == equate(x):
                c.send("[+] Login Successful".encode())
            else:
                c.send("[-] Login Unsuccessful".encode())

c.close()