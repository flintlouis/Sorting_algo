import sys

def swap_el(array, a, b):
	array[a], array[b] = array[b], array[a]

def quick_sort(array, low, high):
	if low < high:
		pivot = partition(array, low, high)

		quick_sort(array, low, pivot - 1)
		quick_sort(array, pivot + 1, high)

def partition(array, low, high):
	pivot = array[high]
	left = low

	for i in range(low, high):
		if array[i] < pivot:
			swap_el(array, left, i)
			left += 1
	swap_el(array, left, high)
	return left

if len(sys.argv) > 1:
	list = sys.argv[1].split()
	for i in range(len(list)):
		list[i] = int(list[i])
	print(list)
	quick_sort(list, 0, len(list) - 1)
	print(list)