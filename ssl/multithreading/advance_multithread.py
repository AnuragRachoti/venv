from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

# def print_number(number):
#     time.sleep(1)
#     return f'Number {number}'


# numbers = [1,2,3,4,5,6,7,8,9,0]

# with ThreadPoolExecutor(max_workers=3) as executor:
#     result = executor.map(print_number, numbers)

# for results in result:
#     print(results)



###multiprocessing with process pool executor.
if __name__ == '__main__':
    def print_number(number):
        time.sleep(1)
        return f'Number {number}'


    numbers = [1,2,3,4,5,6,7,8,9,0]

    with ProcessPoolExecutor(max_workers=3) as executor:
        result = executor.map(print_number, numbers)

    for results in result:
        print(results)