from multiprocessing import Pool
import numpy as np
import time

size = 600

def caleigen(x):     # define work for each worker
    a = np.random.randint(1, 100, size=(size, size))
    S, U = np.linalg.eigh(a)
    return S, U


if __name__ == "__main__":
    start_time = time.time()
    with Pool(processes=16) as pool:      # start a pool of 4 workers
        # distribute work to workers
        result = pool.map_async(caleigen, range(100))
        result = result.get()        # collect result from MapResult object
    end_time = time.time()
    print("Mutltiprocessing took:", end_time - start_time, "seconds")

    # Run the single process version for comparison. This has to be within the if block as well.
    result = []
    start_time = time.time()
    for i in range(100):
        a = np.random.randint(1, 100, size=(size, size))  # generate random matrix
        # calculate eigen values and append to result list
        result.append(np.linalg.eigh(a))
    end_time = time.time()
    print("Single process took :", end_time - start_time, "seconds")
