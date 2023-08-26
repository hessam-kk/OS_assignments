import threading
import random
import time
from os import system


def fill_array(lst: list):
    for i in range(0, 1000000):
        lst.append(random.randint(2, 20))


def get_fact(lst: list):
    for i in lst:
        x = 0
        for t in range(1, i):
            x *= t


system('cls')
lst = []
fill_array(lst)

# serial factorial
print('--------------SERIAL--------------')
start = time.time()
serial_res = 1
for i in lst:
    x = 0
    for t in range(1, i+1):
        x *= t
serial_time = time.time() - start
print('time in serial: ', serial_time)
# end serial factorual

print()
print('--------------PARARELL------------')
# pararell sum
start = time.time()
x1 = threading.Thread(target=get_fact, args=(lst[0:250000],))
x2 = threading.Thread(target=get_fact, args=(lst[250000:500000],))
x3 = threading.Thread(target=get_fact, args=(lst[500000:750000],))
x4 = threading.Thread(target=get_fact, args=(lst[750000:1000000],))

# start threads
x1.start()
x2.start()
x3.start()
x4.start()

# make them wait 
x1.join()
x2.join()
x3.join()
x4.join()

pararell_time = time.time() - start
print('time in pararell: ', pararell_time)
# end pararell

print()
print('--------------CONCLUSION----------')
print(
    f'pararell calculation is {serial_time - pararell_time} faster than serial calculation!!')
print()
