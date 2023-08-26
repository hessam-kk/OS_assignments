# Importing python modules
import time
import sys
import threading as th

# Importing user-defined modules
import Semaphore 
import Chop_stick
import Philosopher


def main():
    # number of philosophers / chop sticks
    n = int(input('please enter the number of philosophers (odd numbers only allowed): '))
    while not (n % 2) and n != 1:
        n = int(input('ERROR: please enter the number of philosophers (odd numbers only allowed): '))

    # this is used for deadlock avoidance - only n-1 is available
    deadlock_avoidance = Semaphore.Semaphore(n-1)

    # this is set the list of chopsticks
    chopstick = [Chop_stick.Chop_stick(i) for i in range(n)]

    # here we set the list of philsophers
    philosophers = [Philosopher.Philosopher(i, chopstick[i], chopstick[(i+1)%n], deadlock_avoidance) for i in range(n)]

    # this is the most important part of programme
    for i in range(n):
        philosophers[i].start()


# Run the code
if __name__ == "__main__":
    main()
    sys.stdout.write('All Done...\nExiting...')