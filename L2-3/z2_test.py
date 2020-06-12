import random
import sys
import numpy as np
import math

repeats = 1000
sys.setrecursionlimit(1100)
compares = 0
standardDeviation = 0
standardDeviationRand = 0
n = int(input("Please enter an amount of elements: "))
k = int(input("Please enter an element to find: "))
arr1 = []
arr2 = []
selectSortCompares = []
randomizedSelectSortCompares = []


def selectSort(arr):
    global compares
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            compares += 1
            if arr[j] < arr[min_index]:
                min_index = j
        compares += 1
        selectSortCompares.append(compares)
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def partition(arr, left, right):
    global compares
    x = arr[right]
    i = left
    for j in range(left, right):
        compares += 1
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i


def randomizedSelectSort(arr, k):
    return randomizedSelectSortAct(arr, 0, len(arr) - 1, k)


def randomizedSelectSortAct(arr, left, right, k):
    global compares

    compares += 1
    if 0 < k <= right - left + 1:

        pivot = partition(arr, left, right)

        compares += 1
        if pivot - left == k - 1:
            return arr[pivot]

        compares += 1
        if pivot - left > k - 1:
            return randomizedSelectSortAct(arr, left, pivot - 1, k)

        return randomizedSelectSortAct(arr, pivot + 1, right, k - pivot + left - 1)


for i in range(repeats):
    if sys.argv[1] == '-r':
        arr1 = random.sample(range(100), n)
        arr2 = arr1.copy()

    if sys.argv[1] == '-p':
        arr1 = np.random.permutation(n)
        arr2 = arr1.copy()

    selectSort(arr1)
    compares = 0

    randomizedSelectSort(arr2, k)
    randomizedSelectSortCompares.append(compares)
    compares = 0

comparesMin = min(selectSortCompares)
comparesMax = max(selectSortCompares)
print("SELECT: Min compares for ", n, " elements ", comparesMin)
print("SELECT: Max compares for ", n, " elements ", comparesMax, end="\n")

comparesMin = min(randomizedSelectSortCompares)
comparesMax = max(randomizedSelectSortCompares)
print("\nRANDOMIZED SELECT: Min compares for ", n, " elements ", comparesMin)
print("RANDOMIZED SELECT: Max compares for ", n, " elements ", comparesMax, end="\n")

average1 = sum(selectSortCompares) // repeats
average2 = sum(randomizedSelectSortCompares) // repeats

for i in range(repeats):
    standardDeviation += (selectSortCompares[i] - average1) ** 2
    standardDeviationRand += (randomizedSelectSortCompares[i] - average2) ** 2

standardDeviation = math.sqrt(standardDeviation // repeats)
standardDeviationRand = math.sqrt(standardDeviationRand // repeats)

print("\nSELECT: Average compares for ", n, " elements is ", average1)
print("SELECT: Standard deviation for ", n, " elements is ", standardDeviation, end="\n")

print("\nRANDOMIZED SELECT: Average compares for ", n, " elements is ", average2)
print("RANDOMIZED SELECT: Standard deviation for ", n, " elements is ", standardDeviationRand, end="\n")


