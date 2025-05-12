# Python3 Program for Odd-Even Transposition sort
# using pthreads
# Link https://www.geeksforgeeks.org/odd-even-transposition-sort-brick-sort-using-pthreads/
from threading import Thread
import random
 
def generate_random_array(size):
    """Gera um array aleatório de inteiros."""
    return [random.randint(0, size) for _ in range(size)]

# Size of array
N = 10000
# maximum number of threads
MAX_THREAD = int(16)
# Generate a random array instead of using the hardcoded one
arr = generate_random_array(N)  # Numbers between 0 and 100
tmp = 0
 
# Function to compare and exchange
# the consecutive elements of the array
def compare():
    global tmp
    # Each thread compares
    # two consecutive elements of the array
    index = tmp
    tmp = tmp + 2
    if index+1 < N and arr[index] > arr[index+1]:
        arr[index], arr[index+1] = arr[index+1], arr[index]
 
 
def createThreads():
    # creating list of size MAX_THREAD
    threads = list(range(MAX_THREAD))
     
    # creating MAX_THEAD number of threads
    for index in range(MAX_THREAD):
        threads[index] = Thread(target=compare)
        threads[index].start()
         
    # Waiting for all threads to finish
    for index in range(MAX_THREAD):
        threads[index].join()
 
 
def oddEven():
    global tmp
    for i in range(1, N+1):
        # Odd Step
        if i % 2:
            tmp = 0
            createThreads()
        # Even Step
        else:
            tmp = 1
            createThreads()
 
# Driver Code
if __name__ == "__main__":
    # print("Given array is : %s" % arr)
    oddEven()
    # print("Sorted array is : %s" % arr)


