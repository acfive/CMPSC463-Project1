import time
import random
import psutil

# Function to perform insertion sort on an array
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Function to perform merge sort on an array
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively apply merge sort to the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the two sorted halves back into the original array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Handle remaining elements in left and right halves
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Function to perform hybrid sort, choosing between insertion sort and merge sort based on a threshold
def hybrid_sort(arr, threshold):
    if len(arr) <= threshold:
        insertion_sort(arr)
    else:
        merge_sort(arr)

# Function to generate an array of random integers
def generateArray(num_of_elements):
    tempArr = []
    for i in range(num_of_elements):
        tempArr.append(random.randint(1, 10000))
    return tempArr

process = psutil.Process()

# Generate a single randomized array
random_array = generateArray(10000)

# Measure memory and time usage for Insertion Sort
arr_insertion = random_array.copy()
memory_before_insertion = process.memory_info().rss
start_time_insertion = time.time()
insertion_sort(arr_insertion)
end_time_insertion = time.time()
memory_after_insertion = process.memory_info().rss
time_taken_insertion = end_time_insertion - start_time_insertion

# Measure memory and time usage for Merge Sort
arr_merge = random_array.copy()
memory_before_merge = process.memory_info().rss
start_time_merge = time.time()
merge_sort(arr_merge)
end_time_merge = time.time()
memory_after_merge = process.memory_info().rss
time_taken_merge = end_time_merge - start_time_merge

# Measure memory and time usage for Hybrid Sort
arr_hybrid = random_array.copy()
memory_before_hybrid = process.memory_info().rss
start_time_hybrid = time.time()
hybrid_sort(arr_hybrid, threshold=10)
end_time_hybrid = time.time()
memory_after_hybrid = process.memory_info().rss
time_taken_hybrid = end_time_hybrid - start_time_hybrid

print(f"Memory usage for Insertion Sort: {memory_before_insertion} -> {memory_after_insertion} bytes")
print("Additional memory needed for insertion sort: ", memory_after_insertion - memory_before_insertion)
print(f"Time taken for Insertion Sort: {time_taken_insertion} seconds")
print("")

print(f"Memory usage for Merge Sort: {memory_before_merge} -> {memory_after_merge} bytes")
print("Additional memory needed for merge sort: ", memory_after_merge - memory_before_merge)
print(f"Time taken for Merge Sort: {time_taken_merge} seconds")
print("")

print(f"Memory usage for Hybrid Sort: {memory_before_hybrid} -> {memory_after_hybrid} bytes")
print("Additional memory needed for hybrid sort: ", memory_after_hybrid - memory_before_hybrid)
print(f"Time taken for Hybrid Sort: {time_taken_hybrid} seconds")

