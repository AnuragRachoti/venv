import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(100000)

##creating our function.

#function to compute factorias of a given number

def compute_fact(n):
    print(f'factorial of a specific number {n}')
    result = math.factorial(n)
    return result

if __name__ == '__main__':
    numbers = [5000,6000,7000]
    start_time = time.time()

    #creating a pool of worker processors

    with multiprocessing.Pool() as pool:
        results = pool.map(compute_fact, numbers)

    end_time = time.time()

    print(f'Results: {results}')
    print(f'Time taken : {end_time - start_time} seconds')