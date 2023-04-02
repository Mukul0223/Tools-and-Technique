#Write a program to implement merge sort.
def merge_sort(arr):
    n = len(arr)

    # Base case: a list of 0 or 1 elements is already sorted
    if n <= 1:
        return arr

    # Recursive case: divide the list into two halves and sort each half
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merge the two sorted halves
    i = j = 0
    merged = []
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1
    merged += left_sorted[i:]
    merged += right_sorted[j:]

    return merged

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = merge_sort(arr)
print(sorted_arr)
