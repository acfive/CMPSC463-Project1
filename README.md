# CMPSC463-Project1

Project Goals:
The goals of this project include finding the most efficient sorting algorithm as well as finding the perfect hybrid algorithm for sorting at peak efficiency. These goals were achieved by documenting the performance of the base merge sort and insertion sort function as well as a hybrid sort containing both insertion and merge sort. The purpose of the hybrid function is to take advantage of the merge sort's speed when dealing with large data sets as well as the insertion sort's speed when dealing with smaller data sets. This was done using a threshold which can be edited to insertion/merge sort when a specific number of elements is left in an array. 

***Testing***

 Code was tested using varying data sizes, including 1,000, 10,000, and 25,000. NOTE: Anything significantly greater than 25,000 elements would not work on my laptop.
The generated array contains random numbers between 1 and 10,000 with a random order every time it is generated
 
***Array with a size of 1000 elements***
-   *Test 1*
   - **Insertion Sort**
 -     Memory usage for Insertion Sort: 15527936 -> 15532032 bytes
-     Additional memory needed for insertion sort:  4096
-     Time taken for Insertion Sort: 0.10892677307128906 seconds
-   **Merge Sort**
-     Memory usage for Merge Sort: 15540224 -> 15552512 bytes
-     Additional memory needed for merge sort:  12288
-     Time taken for Merge Sort: 0.007531166076660156 seconds
-   **Hybrid Sort**
-     Memory usage for Hybrid Sort: 15552512 -> 15560704 bytes
-     Additional memory needed for hybrid sort:  8192
-     Time taken for Hybrid Sort: 0.007513761520385742 seconds
  
-   *Test 2*
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

-   *Test 3*
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

- **Discussing performance:**
These tests on arrays with a size 1000 provided insights into their memory usage and execution times. For Insertion Sort, we observed a consistent pattern of requiring an additional 4096 bytes of memory. However, it was notably slower than both Merge Sort and Hybrid Sort, with execution times ranging from 0.0932 to 0.1089 seconds. Merge Sort consistently used an additional 8192 to 12288 bytes of memory. It outperformed Insertion Sort in terms of execution time, with times as low as 0.0070 to 0.0078 seconds. Hybrid Sort had an intermediate memory usage pattern, requiring 4096 to 12288 bytes of additional memory. Its execution times were on par with Merge Sort, ranging from 0.0070 to 0.0078 seconds. These results underline the trade-offs between memory efficiency and execution speed, highlighting Merge Sort and Hybrid Sort as suitable choices for larger datasets, while Insertion Sort's efficiency is more evident with smaller datasets.


***Array with size of 10,000 elements***
-   *Test 1*
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
    
- *Test 2*
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

-   *Test 3*
-   **Insertion sort**
-     Memory usage for Insertion Sort: 15843328 -> 15847424 bytes
-     Additional memory needed for insertion sort:  4096
-     Time taken for Insertion Sort: 5.557173728942871 seconds
-   **Merge Sort**
-     Memory usage for Merge Sort: 15925248 -> 16084992 bytes
-     Additional memory needed for merge sort:  159744
-     Time taken for Merge Sort: 0.03658771514892578 seconds
-   **Hybrid Sort**
-     Memory usage for Hybrid Sort: 16084992 -> 16166912 bytes
-     Additional memory needed for hybrid sort:  81920
-     Time taken for Hybrid Sort: 0.03599858283996582 seconds
-   **Discussing Performance:**
With an input size of 10,000, Insertion Sort needed a consistent additional memory usage of 4096 bytes, but it came at the cost of relatively slow execution times, ranging from 4.7374 to 5.5572 seconds. In contrast, Merge Sort consistently required more memory, ranging from 57344 to 65536 bytes of additional memory, but offered significantly faster execution times, ranging from 0.0361 to 0.0498 seconds. Hybrid Sort demonstrated an intermediate memory usage pattern, necessitating 4096 to 81920 bytes of additional memory. Its execution times were on par with Merge Sort, ranging from 0.0360 to 0.0366 seconds. These results highlight the trade-offs between memory efficiency and execution speed. Merge Sort and Hybrid Sort showed to much, much faster than insertion sort on larger sets of data. On the other hand, insertion sort proved faster with smaller amounts of data. This is shown in the hybrid sort with the average times being slightly lower than merge sort since insertion sort wraps up the small amount of data faster.

***Array size of 25,000***
- *Test 1*
- **Insertion Sort**
  - Memory usage for Insertion Sort: 16941056 -> 16945152 bytes
  - Additional memory needed for insertion sort:  4096
  - Time taken for Insertion Sort: 29.90860915184021 seconds
- **Merge Sort**
  - Memory usage for Merge Sort: 17141760 -> 17272832 bytes
  - Additional memory needed for merge sort:  131072
  - Time taken for Merge Sort: 0.0765082836151123 seconds
- **Hybrid Sort**
  - Memory usage for Hybrid Sort: 17371136 -> 17469440 bytes
  - Additional memory needed for hybrid sort:  98304
  - Time taken for Hybrid Sort: 0.07050275802612305 seconds
   
- *Test 2*
- **Insertion Sort**
  - Memory usage for Insertion Sort: 16924672 -> 16973824 bytes
  - Additional memory needed for insertion sort:  49152
  - Time taken for Insertion Sort: 36.94051265716553 seconds
- **Merge Sort**
  - Memory usage for Merge Sort: 17174528 -> 17235968 bytes
  - Additional memory needed for merge sort:  61440
  - Time taken for Merge Sort: 0.24836492538452148 seconds
- **Hybrid Sort**
  - Memory usage for Hybrid Sort: 17330176 -> 17432576 bytes
  - Additional memory needed for hybrid sort:  102400
  - Time taken for Hybrid Sort: 0.1635575294494629 seconds
   
 - *Test 3*
 - **Insertion Sort**
  - Memory usage for Insertion Sort: 16957440 -> 17006592 bytes
  - Additional memory needed for insertion sort:  49152
  - Time taken for Insertion Sort: 43.77454209327698 seconds
- **Merge Sort**
  - Memory usage for Merge Sort: 17207296 -> 17285120 bytes
  - Additional memory needed for merge sort:  77824
  - Time taken for Merge Sort: 0.1606743335723877 seconds
- **Hybrid Sort**
  - Memory usage for Hybrid Sort: 17379328 -> 17481728 bytes
  - Additional memory needed for hybrid sort:  102400
  - Time taken for Hybrid Sort: 0.1717231273651123 seconds
- **Discussing Performance:**
When analyzing arrays with 25,000 elements, the performance of the sorting algorithms varied greatly. For Insertion Sort, we observed a consistent memory usage pattern, requiring an additional 4,096 bytes, but the execution time increased significantly, reaching around 30 seconds in the first test. In contrast, Merge Sort consistently outperformed Insertion Sort in terms of execution time, completing the sorting task in just a fraction of a second. When testing Merge Sort specifically, some cases gave a negative memory value. It was about 50/50 when the value would be negative or positive and would only happen with very large data sets. I could not determine the cause of this and more investigation is needed for it. Hybrid Sort showcased a similar memory usage pattern to Merge Sort, but its execution time was slightly longer. With such a large dataset, I expected Merge Sort and Hybrid Sort's times to be very similar in execution times, but the different memory sizes needed surprised me. These results underscore the advantages of memory-efficient algorithms like Merge Sort and Hybrid Sort for sorting large datasets, but they also highlight the need for closer examination of memory-related issues in Merge Sort with large arrays.

