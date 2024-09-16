# Find a peak element that is not smaller than its neighbors.

def peak(arr):
    n=len(arr)
    if n == 1 or arr[0] >= arr[1]:
        return 0
    if arr[n - 1] >= arr[n - 2]:
        return n - 1
    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
             return i
        
my_array = [1, 3, 20, 40, 1, 0]
peak_index = peak(my_array)
print(f"Index of a peak point is {peak_index}")