import multiprocessing
import os

def print_cube(num):
    print(f'os.getpid(): {os.getpid()}')
    print(f'Cube: {num * num * num}')
    
def print_square(num):
    print(f'os.getpid(): {os.getpid()}')
    print(f'Square: {num * num}')
    
def main():
    my_cpu = multiprocessing.cpu_count()
    #print(f'my_cpu: {my_cpu}') # 12
    # Making 1 process p1
    # multiprocessing.Process(target=callbackName, args=(tuple))
    # print(f'Square: {4 * 4 * 4})
    p1 = multiprocessing.Process(target=print_cube, args=(3,))
    # print(f'Square: {4 * 4})
    p2 = multiprocessing.Process(target=print_square, args=(4,))
    # Start Process1 & Process2 at the same time :D
    p1.start()
    p2.start()
    # Wait for p1 & p2 to complete at the same time :D
    # Wait for p1 to complete & terminate => p1.join()
    p1.join()
    # Wait for p2 to complete
    p2.join()
    
    # To check whether p1 is still alive
    print(f'p1.is_alive(): {p1.is_alive()}')
    
    # To check whether p2 is still alive
    print(f'p2.is_alive(): {p2.is_alive()}')
# Fucking Windows needs to confirm this is the main script 
# and NOT a module...
if __name__ == '__main__':
    main()
