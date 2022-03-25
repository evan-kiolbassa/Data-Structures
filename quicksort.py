def quickSort(array):
    quickSortRecursive(array, 0, len(array) - 1)
	return array
def quickSortRecursive(array, startidx, endidx):
	if startidx >= endidx:
		return
	pivot = startidx
	leftPointer = startidx + 1
	rightPointer = endidx
	while rightPointer >= leftPointer:
		if array[leftPointer] > array[pivot] and array[rightPointer] < array[pivot]:
			array = nodeSwap(leftPointer, rightPointer, array)
		if array[rightPointer] >= array[pivot]:
			rightPointer  -= 1
		if array[leftPointer] <= array[pivot]:
			leftPointer += 1
	array = nodeSwap(pivot, rightPointer, array)
	leftArraySmaller = rightPointer - 1  - startidx < endidx - leftPointer
	if leftArraySmaller:
		quickSortRecursive(array, startidx, rightPointer - 1)
		quickSortRecursive(array, rightPointer + 1, endidx)
	else:
		quickSortRecursive(array, rightPointer + 1, endidx)
		quickSortRecursive(array, startidx, rightPointer - 1)				
				
def nodeSwap(leftPointer, rightPointer, array):
	leftValue = array[leftPointer]
	rightValue = array[rightPointer]
	array[rightPointer] = leftValue
	array[leftPointer] = rightValue
	return array
