# Hessam Koucheki
# 9812358032 

import sys
import time

processes = int(input('Please enter count of processes: '))
resources = int(input('Please enter count of resources: '))

resource_list = []
for i in range(resources):
    resource_list.append(int(input('Please now Enter resource numbers: ')))
    
alloc_list = []
for i in range(processes):
    tmp = []
    for j in range(resources):
        tmp.append(int(input('please enter alloc [' + str(i) + '-' + str(j) + '] :')))
    alloc_list.append(tmp)

maximum_list = []
for i in range(processes):
    tmp = []
    for j in range(resources):
        tmp.append(int(input('please enter maximum [' + str(i) + '-' + str(j) + '] :')))
    maximum_list.append(tmp)

neccessary_list = []
for i in range(processes):
    tmp = []
    for j in range(resources):
        tmp.append(int(input('please enter neccessary [' + str(i) +'-' + str(j) + '] :')))
    neccessary_list.append(tmp)

require_list = []
for i in range(processes):
    tmp = []
    for j in range(resources):
        tmp.append(int(input('please enter requiremnet [' + str(i) +'-' + str(j) + '] :')))
    require_list.append(tmp)

free_list = []
for i in range(resources):
    result = 0
    for j in range(processes):
        result += alloc_list[i][j]
    free_list.append(resource_list[i] - result)
    

secure = []
done = []
for i in range(processes):
    done.append(False)
count = 0

while count < processes:
    flag = False
    for i in range(processes):
        if not done[i]:
            for j in range(resources):
                if require_list[i][j] > free_list[j]:
                    break
            if i == resources:
                for t in range(resources):
                    free_list[t] += alloc_list[i][t]
                secure[count] = i
                count += 1
                flag = True
    if not flag:
        sys.stdout.write('-----------------------------------------')
        sys.stdout.write('Warning!! System is not secure/safe...!\n')
        exit(0)

sys.stdout.write('-----------------------------------------')
sys.stdout.write('Nice..! System is secure/safe... :)\n')
time.sleep(1)
sys.stdout.write('-----------------------------------------')
sys.stdout.write('These are the queue for the safe system:\n')
for i in range(processes):
    sys.stdout.write('processes:', secure[i], '\n')
    
    

    
