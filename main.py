import random
import time
import tabulate
import sys

# Increase recursion limit for handling larger arrays
sys.setrecursionlimit(100000)

def selection_sort(array):
    """Implementation of selection sort using recursion"""
    # Base case: single element array is already sorted
    if len(array) <= 1:
        return array
    
    # Find the minimum element position
    min_position = array.index(min(array))
    
    # Swap minimum element with first position
    array[0], array[min_position] = array[min_position], array[0]
    
    # Return sorted first element + recursively sorted remainder
    return [array[0]] + selection_sort(array[1:])

def quick_sort(array, pivot_selector):
    """Divide and conquer sorting algorithm with customizable pivot selection"""
    # Base case: arrays with 0 or 1 elements are already sorted
    if len(array) <= 1:
        return array
    
    # Select pivot based on provided function
    pivot_value = pivot_selector(array)
    
    # Partition the array into three sections
    smaller = [item for item in array if item < pivot_value]
    equal = [item for item in array if item == pivot_value]
    larger = [item for item in array if item > pivot_value]
    
    # Recursively sort and combine the partitions
    return quick_sort(smaller, pivot_selector) + equal + quick_sort(larger, pivot_selector)

def measure_sort_time(sorting_algorithm, data_list):
    """Measure execution time of a sorting algorithm in milliseconds"""
    # Record starting time
    start_time = time.time()
    
    # Execute sorting algorithm
    sorting_algorithm(data_list)
    
    # Calculate and return elapsed time in milliseconds
    return (time.time() - start_time) * 1000

def benchmark_sorting_algorithms(dataset_sizes=[1, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]):
    """Compare performance of different sorting algorithms across various input sizes"""
    # Define sorting algorithms to benchmark
    qs_first_element_pivot = lambda arr: quick_sort(arr, lambda x: x[0])
    qs_random_element_pivot = lambda arr: quick_sort(arr, lambda x: random.choice(x))
    python_builtin_sort = sorted
    
    # Store benchmark results
    performance_results = []
    
    # Test each dataset size
    for size in dataset_sizes:
        # Create sequential list and randomize it
        test_data = list(range(size))
        random.shuffle(test_data)
        
        # Record results for each algorithm
        performance_results.append([
            size,
            measure_sort_time(selection_sort, test_data.copy()),
            measure_sort_time(qs_first_element_pivot, test_data.copy()),
            measure_sort_time(qs_random_element_pivot, test_data.copy()),
            measure_sort_time(python_builtin_sort, test_data.copy()),
        ])
    
    return performance_results

def display_results(benchmark_data):
    """Format and display sorting benchmark results"""
    print(tabulate.tabulate(
        benchmark_data,
        headers=['Array Size', 'Selection Sort', 'QuickSort-Fixed', 'QuickSort-Random', 'Python Sort'],
        floatfmt=".3f",
        tablefmt="github"
    ))

def run_benchmark():
    """Execute sorting benchmark and print results"""
    display_results(benchmark_sorting_algorithms())

# Initialize random number generator
random.seed()

# Run the benchmark
run_benchmark()
