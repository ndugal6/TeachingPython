import threading
class NicksMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x = NicksMessenger(name='Send out messages')
y = NicksMessenger(name='Receive messages')

#Calling start on a thread causes the run function of a class to  be called
x.start()
y.start()