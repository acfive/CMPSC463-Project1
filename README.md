# CMPSC463-Project1

Project Goals:
The goals of this project were to find the most efficient sorting algorithms and the development of a hybrid sorting algorithm for achieving peak efficiency and avoiding the negative traits of its component algorithms. The hybrid sort consists of two component algorithms: insertion sort and merge sort. Insertion sort iterates through an array, shifting elements to their appropriate positions one at a time. It compares each element with the previous ones, moving elements to the right until it finds the correct position. The other hybrid component is merge sort. Merge sort divides the array into smaller segments, recursively sorts them, and then merges these sorted segments back together. This process continues until the entire array is sorted. With both of these components, the hybrid function achieves only the positives of both merge and insertions sorts. These positives are to harness the speed of merge sort when dealing with large datasets and insertion sort's efficiency for smaller datasets. To achieve this, a threshold value is defined, which dynamically determines when to switch between insertion and merge sort. Before the main testing phase, I inputted many different threshold values. In every case where the threshold was greater than 10, every sorting algorithm performed worse in execution time while maintaining the same memory usage. All testing done for this project was done with a threshold of 10 as any other input would lead to worse times and draw away from the actual input size which is what I focused my research on. 

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


- ***Theoretical Analysis For Each Algorithm***
 - **Insertion Sort:**
  - **Theoretical Analysis:** Insertion Sort is a simple and intuitive sorting algorithm that works well for small datasets. It has a time complexity of O(n^2) in the worst and average cases, making it less efficient for large arrays.
   - **Performance Explanation:** Insertion Sort's performance depends on the number of inversions in the dataset. It is efficient when the dataset is almost sorted because it makes fewer comparisons and shifts. However, as the dataset size increases, the number of comparisons and shifts grows quadratically, leading to longer execution times.
  
 - **Merge Sort:**
    - **Theoretical Analysis:** Merge Sort is a divide-and-conquer algorithm that divides the dataset into smaller segments, sorts them, and then merges them back together. It has a consistent time complexity of O(n log n) in all cases.
   - **Performance Explanation:** Merge Sort excels in terms of time complexity and is highly efficient for large datasets. It consistently divides the dataset into two halves, recursively sorts them, and then merges them. The key to its performance is the division and merging process, which ensures a balanced workload, and this makes it suitable for larger datasets
 
 - **Hybrid Sort:**
   - **Theoretical Analysis:** Hybrid Sort combines Insertion Sort and Merge Sort, aiming to harness the advantages of both. It uses Insertion Sort for smaller segments of data and Merge Sort for larger segments, switching between the two based on a defined threshold.
   - **Performance Explanation:** The Hybrid Sort's threshold value determines the size at which it switches from Insertion Sort to Merge Sort. For smaller datasets, Insertion Sort is more efficient due to its lower overhead. As the dataset size increases, Merge Sort's O(n log n) complexity becomes more favorable, and the switch occurs. The Hybrid Sort aims to minimize the quadratic time complexity of Insertion Sort for large datasets. The actual performance of Hybrid Sort depends on the specific threshold chosen and the characteristics of the input data.


- ***Conclusion***
-  After conducting the testing for the project, the performance evaluation of sorting algorithms for varying array sizes sheds light on their memory usage and execution speed characteristics. When working with arrays containing 1,000 elements, Insertion Sort consistently required an additional 4,096 bytes of memory, but it was notably slower than Merge Sort and Hybrid Sort, highlighting its efficiency with smaller datasets. Hybrid Sort, on average, was also fractions of a second faster than both Merge Sort and Insertion Sort. Merge Sort demonstrated both memory efficiency and quick execution times, making it a strong choice for larger datasets. Hybrid Sort, combining the strengths of both Insertion Sort and Merge Sort, showcased a memory usage pattern similar to Merge Sort but with execution times matching Merge Sort's speed. With arrays containing 10,000 elements, these trends continued, demonstrating that memory-efficient algorithms like Merge Sort and Hybrid Sort excel in handling larger datasets while Insertion Sort falls behind in time taken for execution, but excels in memory use. Finally, with arrays of 25,000 elements, the positive traits of Merge Sort and Hybrid Sort persisted, but the negative traits of excessive memory use also were shown with Merge and Hybrid Sort while Insertion Sort stayed consistently small. In summary, the findings in this project have illuminated the trade-offs between memory efficiency and execution speed in sorting algorithms, providing insights into their applicability for various dataset sizes.

