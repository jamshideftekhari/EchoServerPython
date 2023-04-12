import Pyro4
import socket

uri = input("What is the Pyro uri of the greeting object? ").strip()
name = input("What is your name? ").strip()

address = socket.gethostbyname(socket.gethostname())
print(address)

greeting_maker = Pyro4.Proxy(uri)    # get a Pyro proxy to the greeting object
print(greeting_maker.get_fortune(name, address))   # call method normally