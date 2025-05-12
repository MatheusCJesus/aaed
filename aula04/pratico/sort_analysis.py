# Nesse arquivo vamos analisar o tempo de execução dos algoritmos de ordenação
# ShellSort, MergeSort, QuickSort e HeapSort.
# Vou utilizar uma biblioteca que possui a implementação desses algoritmos.
# Biblioteca Pysort: https://pypi.org/project/pysort/

from sorting_techniques.pysort import Sorting  # Import Sorting class diretamente
import time
import random

def generate_random_array(size):
    """Gera um array aleatório de inteiros."""
    return [random.randint(0, 10000) for _ in range(size)]

def generate_sorted_array(size):
    """Gera um array ordenado de inteiros."""
    return list(range(size))

def generate_reverse_sorted_array(size):
    """Gera um array ordenado de inteiros em ordem decrescente."""
    return list(range(size, 0, -1))

def measure_time(sort_function, array):
    """Mede o tempo de execução de uma função de ordenação."""
    start_time = time.time()
    sort_function(array)
    end_time = time.time()
    return end_time - start_time

def mean_time(sort_function, array, iterations=10):
    """Mede o tempo médio de execução de uma função de ordenação."""
    total_time = 0
    for _ in range(iterations):
        array_copy = array.copy()  # Copia o array para não modificar o original
        total_time += measure_time(sort_function, array_copy)
    return total_time / iterations

def quickSort(arr, left, right):

    if left < right:
        pivot = partition(arr, left, right)
        quickSort(arr, left, pivot-1)
        quickSort(arr, pivot+1, right)


def partition(arr, left, right):

    pivot = arr[right]

    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1

def main():
    size = 100000

    # Gera os arrays
    random_array = generate_random_array(size)
    sorted_array = generate_sorted_array(size)
    reverse_sorted_array = generate_reverse_sorted_array(size)

    # Instancia a classe Sorting
    sorting_instance = Sorting()

    # Lista de algoritmos a serem testados
    algorithms = {
        "ShellSort": sorting_instance.shellSort,
        "MergeSort": sorting_instance.mergeSort,
        "HeapSort": sorting_instance.heapSort,
        "QuickSort": lambda arr: quickSort(arr, 0, len(arr) - 1),
    }

    # Testa cada algoritmo com os diferentes tipos de array
    for name, sort_function in algorithms.items():
        print(f"Analisando {name}...")
        print(f"Tempo médio para array aleatório: {mean_time(sort_function, random_array)} segundos")
        print(f"Tempo médio para array ordenado: {mean_time(sort_function, sorted_array)} segundos")
        print(f"Tempo médio para array ordenado reversamente: {mean_time(sort_function, reverse_sorted_array)} segundos")
        print("-" * 50)

if __name__ == "__main__":
    main()