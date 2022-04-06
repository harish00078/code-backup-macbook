from multiprocessing import process
import os
import time

def square_numbers():
    for x in range(100):
        x * x 
        time.sleep(0.1)



processes = []
num_processes = os.cpu_count()


# create processes 
for x in range(num_processes):
    p = process(target=square_numbers)
    processes.append(p)



# start
for p in processes:
    p.start()



#join
for p in processes:
    p.join()



print('end main')

    
    