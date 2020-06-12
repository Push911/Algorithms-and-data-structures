import random
import sys
import numpy as np
import logging

length = 0
shiftCounter = 0
compares = 0
pivots = []
n = int(input("Please enter an amount of elements: "))
k = int(input("Please enter an element to find: "))
sortedList = []
sortedList1 = []


def selectSort(arr):
    global shiftCounter, compares
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            logging.info("Comparing...")
            compares += 1
            if arr[j] < arr[min_index]:
                min_index = j
        logging.info("Comparing...")
        compares += 1
        if min_index != i:
            logging.info("Shifting element...")
            shiftCounter += 1
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def partition(arr, left, right):
    global shiftCounter, compares
    x = arr[right]
    i = left
    for j in range(left, right):
        logging.info("Wykonujemy porównanie...")
        compares += 1
        if arr[j] <= x:
            logging.info("Shifting element...")
            shiftCounter += 1
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    logging.info("Shifting element...")
    shiftCounter += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def randomizedSelectSort(arr, k):
    return randomizedSelectSortAct(arr, 0, len(arr) - 1, k)


def randomizedSelectSortAct(arr, left, right, k):
    global compares

    logging.info("Comparing...")
    compares += 1
    if 0 < k <= right - left + 1:

        pivot = partition(arr, left, right)
        logging.info("Adding new pivot to array")
        pivots.append(pivot)

        logging.info("Comparing...")
        compares += 1
        if pivot - left == k - 1:
            return arr[pivot]

        logging.info("Comparing...")
        compares += 1
        if pivot - left > k - 1:
            return randomizedSelectSortAct(arr, left, pivot - 1, k)

        return randomizedSelectSortAct(arr, pivot + 1, right, k - pivot + left - 1)


logging.basicConfig(level=logging.INFO)

if sys.argv[1] == "-r":
    sortedList = random.sample(range(100), n)
    sortedList1 = sortedList.copy()

if sys.argv[1] == "-p":
    sortedList = np.random.permutation(n)
    sortedList1 = sortedList.copy()


selectSort(sortedList)
logging.info("List length: ", n)
logging.info("Amount of shifts: ", shiftCounter)
logging.info("Amount of compares: ", compares)
logging.info("Sorted list: ", sortedList)

shiftCounter = 0
compares = 0

previousArr = sortedList1.copy()

result = randomizedSelectSort(sortedList1, k)
logging.info("List length: ", n)
logging.info("Amount of shifts: ", shiftCounter)
logging.info("Amount of compares: ", compares)
logging.info("Pivots: ", pivots)

for i in range(len(previousArr)):
    if previousArr[i] == result:
        print("[", result, "]", end=" ")
    elif previousArr[i] != result:
        print(previousArr[i], end=" ")

