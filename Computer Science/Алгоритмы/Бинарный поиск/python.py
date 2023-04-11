def binary_search(arr, match):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < match:
            low = mid + 1
        elif arr[mid] > match:
            high = mid - 1
        else:
            return mid

    return None