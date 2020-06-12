import random
import timeit

comp = 0


def binarySearch(arr, left, right, v):
    global comp

    comp += 1
    if right >= left:

        mid = left + (right - left) // 2

        if arr[mid] == v:
            print("Element has been found!")
            return 1
        elif arr[mid] > v:
            return binarySearch(arr, left, mid - 1, v)
        else:
            return binarySearch(arr, mid + 1, right, v)
    else:
        print("Element hasn't been founded!")
        return 0


n = int(input("Enter the array size: "))
v = int(input("Enter element to find: "))

arr = sorted([random.randint(0, n) for i in range(n)])
arr1 = arr[:n//2]
print(arr, "\n", arr1)
timer1 = timeit.Timer(lambda: binarySearch(arr, 0, len(arr) - 1, v)).timeit(number=1)
compares1 = comp
comp = 0
timer2 = timeit.Timer(lambda: binarySearch(arr1, 0, len(arr1) - 1, v)).timeit(number=1)
compares = compares1 - comp
time = timer1 - timer2
print("O(1) for n = ", n, " amount of compares is: ", compares)
print("O(1) for n = ", n, " time is: ", time)
