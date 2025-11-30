import timeit
import random

'''
test results

Algorithm            | Size       | Time (sec)     
--------------------------------------------------
Insertion Sort       | 100        | 0.00018
Merge Sort           | 100        | 0.00012
Timsort (Built-in)   | 100        | 0.00001
--------------------------------------------------
Insertion Sort       | 1000       | 0.01961
Merge Sort           | 1000       | 0.00134
Timsort (Built-in)   | 1000       | 0.00008
--------------------------------------------------
Insertion Sort       | 5000       | 0.43700
Merge Sort           | 5000       | 0.00711
Timsort (Built-in)   | 5000       | 0.00040
--------------------------------------------------
Insertion Sort       | 30000      | 16.30380
Merge Sort           | 30000      | 0.05214
Timsort (Built-in)   | 30000      | 0.00287
--------------------------------------------------
'''


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def get_data(size, order="random"):
    if order == "random":
        return [random.randint(0, 10000) for _ in range(size)]
    elif order == "sorted":
        return list(range(size))
    elif order == "reversed":
        return list(range(size, 0, -1))


def compare_algorithms():
    sizes = [100, 1000, 5000, 30000]

    print(f"{'Algorithm':<20} | {'Size':<10} | {'Time (sec)':<15}")
    print("-" * 50)

    for size in sizes:
        data = get_data(size)

        t_insert = timeit.timeit(lambda: insertion_sort(data[:]), number=1)
        print(f"{'Insertion Sort':<20} | {size:<10} | {t_insert:.5f}")

        t_merge = timeit.timeit(lambda: merge_sort(data[:]), number=1)
        print(f"{'Merge Sort':<20} | {size:<10} | {t_merge:.5f}")

        t_tim = timeit.timeit(lambda: sorted(data[:]), number=1)
        print(f"{'Timsort (Built-in)':<20} | {size:<10} | {t_tim:.5f}")

        print("-" * 50)


if __name__ == "__main__":
    compare_algorithms()