import threading as th
import sys
import time


class Philosopher (th.Thread):

    def __init__(self, number, left, right, deadlock_avoidance):
        th.Thread.__init__(self)
        self.number = number    # set the philosopher number
        self.left = left
        self.right = right
        self.deadlock_avoidance = deadlock_avoidance

    def run(self):
        for i in range(25):
            self.deadlock_avoidance.down()  # start service by deadlock_avoidance
            time.sleep(0.08)                 # start to think
            self.left.take(self.number)     # pickup left chopstick
            time.sleep(0.08)
            self.right.take(self.number)    # pickup right chopstick
            time.sleep(0.08)                 # eat
            self.right.drop(self.number)    # release the right chopstick for others
            self.left.drop(self.number)     # release the left chopstick for others
            self.deadlock_avoidance.up()    # end service by deadlock_avoidance
        sys.stdout.write("---------------------------------------------------------------------\n")
        sys.stdout.write("philosopher number %s ->> finished his/her thinking and starts eating\n" % self.number)
        sys.stdout.write("---------------------------------------------------------------------\n")
