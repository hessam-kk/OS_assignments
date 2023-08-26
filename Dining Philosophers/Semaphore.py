import threading as th
class Semaphore(object):

    def __init__(self, initial):
        self.lock = th.Condition(th.Lock())
        self.value = initial

    def up(self):
        with self.lock:
            self.value += 1
            self.lock.notify()

    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1
