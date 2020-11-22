import socket

s = socket.socket()

host = socket.gethostname()
port = 12345



def sumOfDigits(num):
    sum = 0

    while num != 0:
        sum = sum + int(num % 10)
        num = int(num / 10)
    
    return sum

def equate(num):
    return (3 * (num * num)) - (9 * num) + 2 

users = {}
s.connect((host,port))

while True:
    inp = input("Register or login? r/l: ")
    if inp == 'r':
        print("Following Functions available:")
        print("1: f(x) + 1)")
        print("2: Sum of digits")
        print("3: Equation")

        inp_li = input("Enter User ID and function choice seperated by space: ").split()
        users[inp_li[0]] = int(inp_li[1])

        # sending details to the server
        data = "r %s %s" % (inp_li[0],inp_li[1])
        print("Trying to send %s" % data)
        s.send(data.encode())
        print(s.recv(1024).decode())
        

    elif inp == 'l':

        userid = input("Enter username: ")
        data = "l %s" % userid

        #connection
        s.send(data.encode())

        num = int(s.recv(1024).decode())
        print("Number Recieved %s" % num)

        print("1: f(x) + 1)")
        print("2: Sum of digits")
        print("3: Equation")
        choice2 = int(input("Function to use?: "))

        if choice2 == 1:
            print("1: Sending %s "% str(num+1))
            s.send(str(num+1).encode())
            
        elif choice2 == 2:
            print("2: Sending %s "% str(sumOfDigits(num)))
            s.send(str(sumOfDigits(num)).encode())
        else:
            print("3: Sending %s "% str(equate(num)))
            s.send(str(equate(num)).encode())

        print(s.recv(1024).decode())
    else:
        s.close()
        break

print('[x] Terminating program')
s.connect((host,port))
print(s.recv(1024))
s.close()
