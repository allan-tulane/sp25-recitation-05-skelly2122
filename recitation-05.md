CMPS 2200 Recitation 5

In this recitation, we'll look at randomness in computation.

To make grading easier, please place all written solutions directly in answers.md, rather than scanning in handwritten work or editing this file.

All coding portions should go in main.py as usual.

Determinism versus Randomization in Quicksort

In lecture we saw that adding a random choice of pivot reduced the probability of worst-case behavior for any given input in selection. Let's look at how pivot choices affect Quicksort. For this question, refer to the code in main.py



**1a)**

Finish implementing the `qsort` and `compare_sort` functions. You may utilize lecture code for list partitioning assistance. Since the pivot selection function is provided to `qsort`, you'll need to curry `qsort` to evaluate different pivot selection strategies. Develop `qsort` variants that select either the first list element or a random element as the pivot.

**1b)**

Use `compare-sort` to analyze runtime differences between Quicksort variants and the provided selection sort (`ssort`). Conduct two comparisons: one using random sequences of specified sizes, and another using pre-sorted sequences. How do actual runtimes align with theoretical complexity bounds? How does input sequence type affect algorithm performance? Compare at least 10 different list sizes, adjusting based on your system's memory constraints. While `print_results` in `main.py` produces a results table, feel free to use Lab 1 code to visualize results graphically.

Sorted:
|     n |    ssort |   qsort-fixed-pivot |   qsort-random-pivot |   tim-sort |
|-------|----------|---------------------|----------------------|------------|
|     1 |    0.001 |               0.002 |                0.001 |      0.001 |
|    20 |    0.029 |               0.073 |                0.041 |      0.002 |
|    50 |    2.341 |               0.624 |                0.086 |      0.002 |
|   100 |    0.283 |               0.647 |                0.237 |      0.003 |
|   200 |    0.840 |               2.560 |                0.499 |      0.004 |
|   500 |    9.496 |              21.990 |                1.933 |      0.010 |
|  1000 |   79.985 |             121.966 |                3.567 |      0.015 |
|  2000 |  197.476 |             393.238 |                4.525 |      0.015 |
|  5000 |  776.661 |            1963.769 |               14.361 |      0.050 |
| 10000 | 2202.947 |            5792.638 |               26.976 |      0.095 |

Random:
|     n |    ssort |   qsort-fixed-pivot |   qsort-random-pivot |   tim-sort |
|-------|----------|---------------------|----------------------|------------|
|     1 |    0.001 |               0.002 |                0.001 |      0.001 |
|    20 |    0.020 |               0.019 |                0.031 |      0.002 |
|    50 |    0.060 |               0.041 |                0.059 |      0.003 |
|   100 |    0.246 |               0.109 |                0.124 |      0.007 |
|   200 |    0.688 |               0.207 |                0.257 |      0.015 |
|   500 |    9.395 |               0.897 |                1.142 |      0.054 |
|  1000 |   26.184 |               2.028 |                2.206 |      0.124 |
|  2000 |  162.481 |               3.887 |                4.101 |      0.224 |
|  5000 |  686.645 |              11.691 |               13.994 |      0.675 |
| 10000 | 2424.923 |              21.307 |               25.488 |      1.407 |

Selection Sort matches its theoretical O(n²) time complexity for both sorted and random lists, as evidenced by the exponential time increase with larger inputs.

Fixed Pivot Quicksort performs poorly at O(n²) on sorted lists because it consistently selects the worst possible pivot (causing degenerate partitioning), but achieves O(n log n) efficiency on random lists where it effectively selects random pivots, enabling many "good" pivot choices. Time increases exponentially for sorted arrays but follows O(n log n) for random inputs.

Random Pivot Quicksort achieves O(n log n) complexity on both sorted and random inputs because its random selection strategy statistically ensures many favorable pivots over time while avoiding problematic ones.

**1c)**

Python implements [*Timsort*](https://en.wikipedia.org/wiki/Timsort), designed by Tim Peters. Compare your fastest sorting implementation against Python's native `sorted` function using the same tests from 1b.

Timsort outperforms all other algorithms significantly, with exceptional performance on sorted data and modest advantages on unsorted data. It processes sorted arrays approximately 10 times faster than random ones.
