import random
import timeit


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

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst

def _timer(sort_algorythm, array):
    start_time = timeit.default_timer()
    _ = sort_algorythm(array[:])
    end_time = timeit.default_timer()
    delta = end_time - start_time
    return delta

def run_sorts():
    array_sizes = [500, 5000, 50000]

    for array_size in array_sizes:
        test_data = [random.randint(0, 10000) for _ in range(array_size)]

        print(f"Number of elements: {array_size}")
        print(f"Insertion Sort: {_timer(insertion_sort, test_data)}")
        print(f"Merge Sort: {_timer(merge_sort, test_data)}")
        print(f"Timsort: {_timer(sorted, test_data)}")
        print()

if __name__ == '__main__':
    run_sorts()

