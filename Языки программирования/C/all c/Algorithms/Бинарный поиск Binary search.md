```c
int binary_search(int* array, int match) {
	int length = sizeof(array)/sizeof(int);
	int low = 0;
	int high = length - 1;
	int mid;
	
	while (low <= high) {
		mid = (high + low) / 2;
		if (array[mid] < match)
			low = mid + 1
		else if (array[mid] > match)
			high = mid - 1
		else
			return mid
	}
	
	return -1;
}
```