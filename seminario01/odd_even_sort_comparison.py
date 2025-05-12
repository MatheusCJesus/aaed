import random
import time
import numpy as np
from threading import Thread
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor

# Note: For NVIDIA CUDA implementation, we'll use CuPy if available
try:
    import cupy as cp
    CUDA_AVAILABLE = True
except ImportError:
    CUDA_AVAILABLE = False
    print("CuPy not found. NVIDIA CUDA implementation will be skipped.")

def generate_random_array(size):
    """Generate a random array of integers."""
    return [random.randint(0, size) for _ in range(size)]

# Sequential implementation of Odd-Even sort
def odd_even_sort_sequential(arr):
    n = len(arr)
    sorted = False
    
    while not sorted:
        sorted = True
        
        # Odd phase
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
        
        # Even phase
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
    
    return arr

# Parallel implementation with threads (fixed version)
def odd_even_sort_parallel(arr, num_threads=4):
    n = len(arr)
    result = arr.copy()
    
    def compare_and_swap(start_idx, step=2):
        """Compare and swap elements starting from start_idx with step 2."""
        swapped = False
        for i in range(start_idx, n-1, step):
            if result[i] > result[i+1]:
                result[i], result[i+1] = result[i+1], result[i]
                swapped = True
        return swapped
    
    # Divide work among threads more efficiently
    sorted_flag = False
    
    while not sorted_flag:
        sorted_flag = True
        
        # Odd phase - each thread handles a portion of the array
        odd_swapped = False
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            chunk_size = max(1, (n // num_threads) // 2)
            odd_indices = list(range(1, n-1, 2))
            odd_chunks = [odd_indices[i:i+chunk_size] for i in range(0, len(odd_indices), chunk_size)]
            
            def process_chunk(indices):
                chunk_swapped = False
                for idx in indices:
                    if result[idx] > result[idx+1]:
                        result[idx], result[idx+1] = result[idx+1], result[idx]
                        chunk_swapped = True
                return chunk_swapped
            
            futures = [executor.submit(process_chunk, chunk) for chunk in odd_chunks if chunk]
            for future in futures:
                if future.result():
                    odd_swapped = True
        
        # Even phase - each thread handles a portion of the array
        even_swapped = False
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            chunk_size = max(1, (n // num_threads) // 2)
            even_indices = list(range(0, n-1, 2))
            even_chunks = [even_indices[i:i+chunk_size] for i in range(0, len(even_indices), chunk_size)]
            
            futures = [executor.submit(process_chunk, chunk) for chunk in even_chunks if chunk]
            for future in futures:
                if future.result():
                    even_swapped = True
        
        # If either phase swapped elements, we're not sorted yet
        if odd_swapped or even_swapped:
            sorted_flag = False
    
    return result

# NVIDIA CUDA implementation using CuPy
def odd_even_sort_cuda(arr):
    if not CUDA_AVAILABLE:
        return None
    
    # Convert to CuPy array
    d_arr = cp.array(arr)
    n = len(arr)
    
    # Custom CUDA kernel for Odd-Even sort
    # This is a simplified version - NVIDIA's CUB implementation would be more optimized
    odd_even_sort_kernel = cp.RawKernel(r'''
    extern "C" __global__
    void odd_even_sort(float* data, int n, bool* swapped) {
        // Odd phase
        *swapped = false;
        for (int i = 1; i < n-1; i += 2) {
            if (data[i] > data[i+1]) {
                float temp = data[i];
                data[i] = data[i+1];
                data[i+1] = temp;
                *swapped = true;
            }
        }
        __syncthreads();
        
        // Even phase
        for (int i = 0; i < n-1; i += 2) {
            if (data[i] > data[i+1]) {
                float temp = data[i];
                data[i] = data[i+1];
                data[i+1] = temp;
                *swapped = true;
            }
        }
    }
    ''', 'odd_even_sort')
    
    # Run the sort
    d_swapped = cp.array([True])
    while d_swapped[0]:
        d_swapped[0] = False
        odd_even_sort_kernel((1,), (1,), (d_arr, n, d_swapped))
    
    # Return sorted array
    return cp.asnumpy(d_arr)

def benchmark(sizes):
    """Benchmark different odd-even sort implementations with various array sizes."""
    sequential_times = []
    parallel_times = []
    cuda_times = []
    
    for size in sizes:
        print(f"Testing with array size: {size}")
        test_array = generate_random_array(size)
        
        # Sequential implementation
        start_time = time.time()
        odd_even_sort_sequential(test_array.copy())
        seq_time = time.time() - start_time
        sequential_times.append(seq_time)
        print(f"  Sequential: {seq_time:.4f} seconds")
        
        # Parallel implementation
        start_time = time.time()
        odd_even_sort_parallel(test_array.copy())
        par_time = time.time() - start_time
        parallel_times.append(par_time)
        print(f"  Parallel: {par_time:.4f} seconds")
        
        # CUDA implementation
        if CUDA_AVAILABLE:
            start_time = time.time()
            odd_even_sort_cuda(test_array.copy())
            cuda_time = time.time() - start_time
            cuda_times.append(cuda_time)
            print(f"  CUDA: {cuda_time:.4f} seconds")
        
        print()
    
    return sequential_times, parallel_times, cuda_times

def plot_results(sizes, sequential_times, parallel_times, cuda_times):
    """Plot benchmark results."""
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, sequential_times, 'o-', label='Sequential')
    plt.plot(sizes, parallel_times, 's-', label='Parallel (Threads)')
    
    if CUDA_AVAILABLE:
        plt.plot(sizes, cuda_times, 'D-', label='CUDA (NVIDIA)')
    
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Odd-Even Sort Performance Comparison')
    plt.legend()
    plt.grid(True)
    plt.savefig('odd_even_sort_comparison.png')
    plt.show()

if __name__ == "__main__":
    # Test with different array sizes
    sizes = [100, 500, 1000, 5000, 10000]
    
    # Run benchmark
    sequential_times, parallel_times, cuda_times = benchmark(sizes)
    
    # Plot results
    plot_results(sizes, sequential_times, parallel_times, cuda_times)
    
    # Print summary
    print("Performance Summary:")
    print(f"{'Size':<10} {'Sequential':<15} {'Parallel':<15} {'CUDA':<15}")
    for i, size in enumerate(sizes):
        cuda_time = cuda_times[i] if CUDA_AVAILABLE else "N/A"
        print(f"{size:<10} {sequential_times[i]:<15.4f} {parallel_times[i]:<15.4f} {cuda_time}")