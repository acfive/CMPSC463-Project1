# CMPSC463-Project1

Project Goals:
The goals of this project include finding the most efficient sorting algorithm as well as finding the perfect hybrid algorithm for sorting at peak efficiency. These goals were achieved by documenting the performance of the base merge sort and insertion sort function as well as a hybrid sort containing both insertion and merge sort. The purpose of the hybrid function is to take advantage of the merge sort's speed when dealing with large data sets as well as the insertion sort's speed when dealing with smaller data sets. This was done using a threshold which can be edited to insertion/merge sort when a specific number of elements is left in an array. 

***Testing***

 Code was tested using varying data sizes, including 1,000, 10,000, and 100,000
 The generated array contains random numbers between 1 and 10,000 with a random order every time it is generated
 
***Array with a size of 1000 elements***
-   Test 1
   - Insertion Sort
 -     Memory usage for Insertion Sort: 15527936 -> 15532032 bytes
-     Additional memory needed for insertion sort:  4096
-     Time taken for Insertion Sort: 0.10892677307128906 seconds
-   Merge Sort
-     Memory usage for Merge Sort: 15540224 -> 15552512 bytes
-     Additional memory needed for merge sort:  12288
-     Time taken for Merge Sort: 0.007531166076660156 seconds
-   Hybrid Sort
-     Memory usage for Hybrid Sort: 15552512 -> 15560704 bytes
-     Additional memory needed for hybrid sort:  8192
-     Time taken for Hybrid Sort: 0.007513761520385742 seconds
  
-   Test 2
-   **Insertion Sort**
-     Memory usage for Insertion Sort: 15495168 -> 15499264 bytes
-     Additional memory needed for insertion sort:  4096
-     Time taken for Insertion Sort: 0.09323501586914062 seconds
-   **Merge Sort**
-     Memory usage for Merge Sort: 15507456 -> 15515648 bytes
-     Additional memory needed for merge sort:  8192
-     Time taken for Merge Sort: 0.007512331008911133 seconds
-   **Hybrid Sort**
-     Memory usage for Hybrid Sort: 15519744 -> 15523840 bytes
-     Additional memory needed for hybrid sort:  4096
-     Time taken for Hybrid Sort: 0.007784843444824219 seconds

-   **Test 3**
-   **Insertion Sort**
-   Memory usage for Insertion Sort: 15560704 -> 15564800 bytes
-     Additional memory needed for insertion sort:  4096
-     Time taken for Insertion Sort: 0.09526753425598145 seconds
-   **Merge Sort**
-     Memory usage for Merge Sort: 15572992 -> 15581184 bytes
-     Additional memory needed for merge sort:  8192
-     Time taken for Merge Sort: 0.007374286651611328 seconds
-   **Hybrid Sort**
-     Memory usage for Hybrid Sort: 15581184 -> 15593472 bytes
-     Additional memory needed for hybrid sort:  12288
-     Time taken for Hybrid Sort: 0.007013797760009766 seconds

- Discussing performance: 
These tests on arrays with a size 1000 provided insights into their memory usage and execution times. For Insertion Sort, we observed a consistent pattern of requiring an additional 4096 bytes of memory. However, it was notably slower than both Merge Sort and Hybrid Sort, with execution times ranging from 0.0932 to 0.1089 seconds. Merge Sort consistently used an additional 8192 to 12288 bytes of memory. It outperformed Insertion Sort in terms of execution time, with times as low as 0.0070 to 0.0078 seconds. Hybrid Sort had an intermediate memory usage pattern, requiring 4096 to 12288 bytes of additional memory. Its execution times were on par with Merge Sort, ranging from 0.0070 to 0.0078 seconds. These results underline the trade-offs between memory efficiency and execution speed, highlighting Merge Sort and Hybrid Sort as suitable choices for larger datasets, while Insertion Sort's efficiency is more evident with smaller datasets.


***Array with size of 10,000 elements***
-   Test 1
-   **Insertion Sort**
-     Memory usage for Insertion Sort: 16056320 -> 16060416 bytes
-     Additional memory needed for insertion sort:  4096
-     Time taken for Insertion Sort: 5.347431182861328 seconds
- **Merge Sort**
-     Memory usage for Merge Sort: 16138240 -> 16203776 bytes
-     Additional memory needed for merge sort:  65536
-     Time taken for Merge Sort: 0.03681325912475586 seconds
-   **Hybrid Sort**
-     Memory usage for Hybrid Sort: 16224256 -> 16285696 bytes
-     Additional memory needed for hybrid sort:  61440
-     Time taken for Hybrid Sort: 0.03568220138549805 seconds
    
- Test 2
-   **Insertion Sort**
-     Memory usage for Insertion Sort: 16101376 -> 16105472 bytes
-     Additional memory needed for insertion sort:  4096
-     Time taken for Insertion Sort: 4.7373974323272705 seconds
-   **Merge Sort**
-     Memory usage for Merge Sort: 16187392 -> 16244736 bytes
-     Additional memory needed for merge sort:  57344
- Time taken for Merge Sort: 0.04981088638305664 seconds
-   **Hybrid Sort**
-     Memory usage for Hybrid Sort: 16265216 -> 16330752 bytes
-     Additional memory needed for hybrid sort:  65536
-     Time taken for Hybrid Sort: 0.036128997802734375 seconds

-   Test 3
-   **Insertion sort**
-     Memory usage for Insertion Sort: 15843328 -> 15847424 bytes
-     Additional memory needed for insertion sort:  4096
-     Time taken for Insertion Sort: 5.557173728942871 seconds
-   **Merge Sort**
-     Memory usage for Merge Sort: 15925248 -> 16084992 bytes
-     Additional memory needed for merge sort:  159744
-     Time taken for Merge Sort: 0.03658771514892578 seconds
-   **Hybrid Sort**
    Memory usage for Hybrid Sort: 16084992 -> 16166912 bytes
-     Additional memory needed for hybrid sort:  81920
-     Time taken for Hybrid Sort: 0.03599858283996582 seconds
