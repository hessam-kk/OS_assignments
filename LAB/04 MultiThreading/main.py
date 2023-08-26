import threading
from collections import deque
import psutil as ps
from os import system
from time import sleep, time, ctime

# while True:
#     sleep(0.5)
#     system('cls')
#     print('cpu:', ps.cpu_percent(0))
#     print('Memory:', ps.virtual_memory()[2])
#     print('Net:', st.download() + st.upload())
    


def calc_ul_dl(rate, dt=1, interface='Wi-Fi'):
    t0 = time()
    counter = ps.net_io_counters(pernic=True)[interface]
    tot = (counter.bytes_sent, counter.bytes_recv)

    while True:
        last_tot = tot
        sleep(dt)
        counter = ps.net_io_counters(pernic=True)[interface]
        t1 = time()
        tot = (counter.bytes_sent, counter.bytes_recv)
        ul, dl = [
            (now - last) / (t1 - t0) / 1000.0
            for now, last in zip(tot, last_tot)
        ]
        rate.append((ul, dl))
        t0 = time()


def print_rate(rate):
    try:
        # sleep(0.5)
        print("UL: {0:.0f} kB/s / DL: {1:.0f} kB/s".format(*rate[-1]))
    except IndexError:
        print("UL: - kB/s/ DL: - kB/s")

def save_to_file():
    with open('data.txt', 'a+') as f:
        f.write('-'*10 + ctime() + '-'*10 + '\n')
        f.write('CPU:' + str(ps.cpu_percent(0)) + '\n')
        f.write('Memory:' + str(ps.virtual_memory()[2]) + '\n')


# Create the ul/dl thread and a deque of length 1 to hold the ul/dl- values
transfer_rate = deque(maxlen=1)
t = threading.Thread(target=calc_ul_dl, args=(transfer_rate,))

# The program will exit if there are only daemonic threads left.
t.daemon = True
t.start()

from os import system
# The rest of your program, emulated by me using a while True loop
while True:
    print_rate(transfer_rate)
    print(transfer_rate)
    print('CPU:', ps.cpu_percent(0))
    print('Memory:', ps.virtual_memory()[2])
    save_to_file()
    sleep(5)
    system('cls')