I'll create a reformatted version of the sorting algorithm analysis:

# CMPS 2200 - Recitation 5 Results

## Sorting Algorithm Performance Analysis

**Team Members:** Samuel Kelly and n/a


### Benchmark Results

#### Pre-sorted Arrays

| Input Size | Selection Sort (ms) | QuickSort Fixed Pivot (ms) | QuickSort Random Pivot (ms) | TimSort (ms) |
|------------|--------------------|-----------------------------|----------------------------|--------------|
| 1          | 0.001              | 0.002                       | 0.001                      | 0.001        |
| 20         | 0.029              | 0.073                       | 0.041                      | 0.002        |
| 50         | 2.341              | 0.624                       | 0.086                      | 0.002        |
| 100        | 0.283              | 0.647                       | 0.237                      | 0.003        |
| 200        | 0.840              | 2.560                       | 0.499                      | 0.004        |
| 500        | 9.496              | 21.990                      | 1.933                      | 0.010        |
| 1000       | 79.985             | 121.966                     | 3.567                      | 0.015        |
| 2000       | 197.476            | 393.238                     | 4.525                      | 0.015        |
| 5000       | 776.661            | 1963.769                    | 14.361                     | 0.050        |
| 10000      | 2202.947           | 5792.638                    | 26.976                     | 0.095        |

#### Random Arrays

| Input Size | Selection Sort (ms) | QuickSort Fixed Pivot (ms) | QuickSort Random Pivot (ms) | TimSort (ms) |
|------------|--------------------|-----------------------------|----------------------------|--------------|
| 1          | 0.001              | 0.002                       | 0.001                      | 0.001        |
| 20         | 0.020              | 0.019                       | 0.031                      | 0.002        |
| 50         | 0.060              | 0.041                       | 0.059                      | 0.003        |
| 100        | 0.246              | 0.109                       | 0.124                      | 0.007        |
| 200        | 0.688              | 0.207                       | 0.257                      | 0.015        |
| 500        | 9.395              | 0.897                       | 1.142                      | 0.054        |
| 1000       | 26.184             | 2.028                       | 2.206                      | 0.124        |
| 2000       | 162.481            | 3.887                       | 4.101                      | 0.224        |
| 5000       | 686.645            | 11.691                      | 13.994                     | 0.675        |
| 10000      | 2424.923           | 21.307                      | 25.488                     | 1.407        |

### Analysis

Our experimental results confirm the theoretical complexity of each algorithm:

1. **Selection Sort**: Demonstrates consistent O(n²) behavior for both sorted and random inputs. The execution time increases quadratically as input size grows, showing nearly identical performance regardless of initial array order.

2. **QuickSort with Fixed Pivot**: 
   - For sorted arrays: Shows poor O(n²) performance due to degenerate partitioning (always selecting the worst possible pivot)
   - For random arrays: Achieves closer to O(n log n) complexity as pivot selection becomes more balanced

3. **QuickSort with Random Pivot**: Maintains O(n log n) complexity for both input types by avoiding worst-case scenarios through randomization. The performance is significantly better than fixed-pivot QuickSort on sorted data.

4. **TimSort**: Outperforms all other algorithms across both test cases. Particularly efficient with pre-sorted data (approximately 10x faster than with random data), demonstrating its adaptive nature that recognizes and exploits existing order within the input.

TimSort's hybrid approach combining merge sort and insertion sort, along with its pattern recognition capabilities, makes it exceptionally well-suited for real-world data that often contains partially ordered sequences.
