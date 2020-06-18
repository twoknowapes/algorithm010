def heapify(arr, n, i):
    # Initialize largest as root
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = 1

    # Right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Heapify the root
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Only by one extact elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)