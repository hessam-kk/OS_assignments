import threading as th
import sys


class Chop_stick(object):
    def __init__(self, number):
        self.number = number           # chop stick ID
        self.user = -1                 # keep track of philosopher using it
        self.lock = th.Condition(th.Lock())
        self.taken = False

    def take(self, user):           # used for synchronization
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user = user
            self.taken = True
            sys.stdout.write("philosopher number ->> %s took chopstick number -> %s\n" % (user+1, self.number+1))
            self.lock.notifyAll()

    def drop(self, user):         # used for synchronization
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user = -1
            self.taken = False
            sys.stdout.write("philosopher number ->> %s dropped chopstick number -> %s\n" % (user+1, self.number+1))
            self.lock.notifyAll()
