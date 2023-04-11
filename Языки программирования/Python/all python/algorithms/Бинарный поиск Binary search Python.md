```python
def binary_search(arr, match):
	low = 0
	high = len(arr)-1 # Длина списка
	while low <= high: # Продолжать код пока high больше или равно low
		mid = (low + high) // 2
		if arr[mid] < match:
			low = mid + 1 # Убрать правую часть
		elif arr[mid] > match:
			high = mid - 1 # Убрать левую часть
		else:
			return mid
	return None # Если не найдено то вернуть None
```