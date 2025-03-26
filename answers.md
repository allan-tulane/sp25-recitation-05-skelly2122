Team Members: Samuel Kelly and N/A

Benchmark Results
Pre-sorted Arrays
Input SizeSelection Sort (ms)QuickSort Fixed Pivot (ms)QuickSort Random Pivot (ms)TimSort (ms)10.0010.0020.0010.001200.0290.0730.0410.002502.3410.6240.0860.0021000.2830.6470.2370.0032000.8402.5600.4990.0045009.49621.9901.9330.010100079.985121.9663.5670.0152000197.476393.2384.5250.0155000776.6611963.76914.3610.050100002202.9475792.63826.9760.095
Random Arrays
Input SizeSelection Sort (ms)QuickSort Fixed Pivot (ms)QuickSort Random Pivot (ms)TimSort (ms)10.0010.0020.0010.001200.0200.0190.0310.002500.0600.0410.0590.0031000.2460.1090.1240.0072000.6880.2070.2570.0155009.3950.8971.1420.054100026.1842.0282.2060.1242000162.4813.8874.1010.2245000686.64511.69113.9940.675100002424.92321.30725.4881.407
Analysis
Our experimental results confirm the theoretical complexity of each algorithm:

Selection Sort: Demonstrates consistent O(n²) behavior for both sorted and random inputs. The execution time increases quadratically as input size grows, showing nearly identical performance regardless of initial array order.
QuickSort with Fixed Pivot:

For sorted arrays: Shows poor O(n²) performance due to degenerate partitioning (always selecting the worst possible pivot)
For random arrays: Achieves closer to O(n log n) complexity as pivot selection becomes more balanced


QuickSort with Random Pivot: Maintains O(n log n) complexity for both input types by avoiding worst-case scenarios through randomization. The performance is significantly better than fixed-pivot QuickSort on sorted data.
TimSort: Outperforms all other algorithms across both test cases. Particularly efficient with pre-sorted data (approximately 10x faster than with random data), demonstrating its adaptive nature that recognizes and exploits existing order within the input.

TimSort's hybrid approach combining merge sort and insertion sort, along with its pattern recognition capabilities, makes it exceptionally well-suited for real-world data that often contains partially ordered sequences.
