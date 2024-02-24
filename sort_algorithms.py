import random
import timeit


def insertion_sort(arr_):
    arr = arr_[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr_):
    arr = arr_[:]
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1
    # result += left[left_index:]
    # result += right[right_index:]
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def bubble_sort(arr_):
    arr = arr_[:]
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


small_data = [random.randint(0, 1000) for i in range(100)]
medium_data = [random.randint(0, 1000) for i in range(1000)]
large_data = [random.randint(0, 1000) for i in range(10000)]

ts_insertion = timeit.timeit(lambda: insertion_sort(small_data), number=30)
ts_merge_sort = timeit.timeit(lambda: merge_sort(small_data), number=30)
ts_quick_sort = timeit.timeit(lambda: quick_sort(small_data), number=30)
ts_bubble_sort = timeit.timeit(lambda: bubble_sort(small_data), number=30)
ts_sorted = timeit.timeit(lambda: sorted(small_data), number=30)
ts_sort = timeit.timeit(lambda: small_data[:].sort(), number=30)

tm_insertion = timeit.timeit(lambda: insertion_sort(medium_data), number=30)
tm_merge_sort = timeit.timeit(lambda: merge_sort(medium_data), number=30)
tm_quick_sort = timeit.timeit(lambda: quick_sort(medium_data), number=30)
tm_bubble_sort = timeit.timeit(lambda: bubble_sort(medium_data), number=30)
tm_sorted = timeit.timeit(lambda: sorted(medium_data), number=30)
tm_sort = timeit.timeit(lambda: medium_data[:].sort(), number=30)

tl_insertion = timeit.timeit(lambda: insertion_sort(large_data), number=30)
tl_merge_sort = timeit.timeit(lambda: merge_sort(large_data), number=30)
tl_quick_sort = timeit.timeit(lambda: quick_sort(large_data), number=30)
tl_bubble_sort = timeit.timeit(lambda: bubble_sort(large_data), number=30)
tl_sorted = timeit.timeit(lambda: sorted(large_data), number=30)
tl_sort = timeit.timeit(lambda: large_data[:].sort(), number=30)

print(f"| {'Algorithm':<20} | {'Small':<20} | {'Medium':<20} | {'Large':<20} |")
print(f"| {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} |")
print(
    f"| {'Insertion Sort':<20} | {ts_insertion:20.5f} | {tm_insertion:20.5f} | {tl_insertion:20.5f} |"
)
print(
    f"| {'Merge Sort':<20} | {ts_merge_sort:20.5f} | {tm_merge_sort:20.5f} | {tl_merge_sort:20.5f} |"
)
print(
    f"| {'Quicksort':<20} | {ts_quick_sort:20.5f} | {tm_quick_sort:20.5f} | {tl_quick_sort:20.5f} |"
)
print(
    f"| {'Bubble Sort':<20} | {ts_bubble_sort:20.5f} | {tm_bubble_sort:20.5f} | {tl_bubble_sort:20.5f} |"
)
print(
    f"| {'Timsorted':<20} | {ts_sorted:20.5f} | {tm_sorted:20.5f} | {tl_sorted:20.5f} |"
)
print(f"| {'Timsort':<20} | {ts_sort:20.5f} | {tm_sort:20.5f} | {tl_sort:20.5f} |")
