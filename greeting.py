# server program
import Pyro4

@Pyro4.expose

class greetingMaker():
    def get_fortune(self, name):
        return "Hello, {0}!".format(name)
    
if __name__ == "__main__":
    daemon = Pyro4.Daemon()
    uri = daemon.register(greetingMaker)
    print(uri)
    daemon.requestLoop()    
