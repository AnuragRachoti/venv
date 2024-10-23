## multiprocessing ?? -- >  it allows you to create processes 
## when to use ? -> cpu bound task.
### Parallel execution in such a way so that i can use all the cores of the CPu.

import multiprocessing
import time

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f'square {i*i}')

def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f'cube {i*i*i}')


if __name__ == '__main__':
        ##creating 2 processes
        t= time.time()
        p1 = multiprocessing.Process(target=square_number)
        p2 = multiprocessing.Process(target=cube_number)

        ##starting the process
        p1.start()
        p2.start()


        ##waiting to finish the process

        p1.join()
        p2.join()

        finished_time = time.time() - t
        print(finished_time)