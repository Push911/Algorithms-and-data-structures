import random
import sys
import timeit
import os

global arr, arrLen, ascending
compares, transpositions, timeSpent, comp, trans, arLen = 0, 0, [], [], [], []
filename = sys.argv[2]


def timer(func):
    def tmr(*xs, **kws):
        global time
        start = timeit.default_timer()
        func(*xs, **kws)
        time = timeit.default_timer() - start
        # print("Function:", func.__name__, "was completed in", time, "seconds")
        # print("Sort was completed in", '{:.10f}'.format(time).rstrip('0'), "seconds")
        return '{:.10f}'.format(time).rstrip('0')

    return tmr


@timer
def insertion(array, arrLen, ascending):
    insertionSort(array, arrLen, ascending)


def insertionSort(array, arrLen, ascending=True):
    global compares, transpositions

    for i in range(1, arrLen):

        insertionSort(array, arrLen - 1)
        last = array[arrLen - 1]
        j = arrLen - 2
        compares += 1

        while j >= 0 and array[j] > last:
            transpositions += 1
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = last

        if ascending:
            return array
        else:
            return array.reverse()


@timer
def merge(array, ascending):
    mergeSort(array, ascending)


def mergeSort(array, ascending=True):
    global compares, transpositions

    compares += 1
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        compares += 1
        while i < len(left) and j < len(right):
            compares += 1
            if left[i] < right[j]:
                transpositions += 1
                array[k] = left[i]
                i += 1
            else:
                transpositions += 1
                array[k] = right[j]
                j += 1
            k += 1

        compares += 1
        while i < len(left):
            transpositions += 1
            array[k] = left[i]
            i += 1
            k += 1

        compares += 1
        while j < len(right):
            transpositions += 1
            array[k] = right[j]
            j += 1
            k += 1

    if ascending:
        return array
    else:
        return array.reverse()


def partition(array, low, high):
    global compares, transpositions
    i = low - 1
    center = array[high]
    transpositions += 1

    for j in range(low, high):
        compares += 1
        if array[j] <= center:
            transpositions += 1
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


@timer
def quick(array, low, high, ascending):
    quickSort(array, low, high, ascending)


def quickSort(array, low, high, ascending=True):
    global compares, transpositions

    compares += 1

    if low < high:
        index = partition(array, low, high)
        quickSort(array, low, index - 1)
        quickSort(array, index + 1, high)

    if ascending:
        return array
    else:
        return array.reverse()


@timer
def mqs(array, low, high, ascending):
    mergeQuickSort(array, low, high, ascending)


def mergeQuickSort(array, low, high, ascending=True):
    global compares, transpositions
    while low < high:
        compares += 1
        if high - low < 8:
            mergeSort(array, ascending)
            break
        else:
            p = partition(array, low, high)
            if p - low < high - p:
                compares += 1
                mergeQuickSort(array, low, p - 1)
                transpositions += 1
                low = p + 1
            else:
                compares += 1
                mergeQuickSort(array, p + 1, high)
                transpositions += 1
                high = p - 1
    if ascending:
        return array
    else:
        return array.reverse()


@timer
def qsdp(array, low, high, ascending):
    quickSortDualPivot(array, low, high, ascending)


def quickSortDualPivot(array, low, high, ascending=True):
    global compares, transpositions

    compares += 1
    if high <= low:
        return
    l = low + 1
    k = l
    h = high - 1
    if array[low] > array[high]:
        transpositions += 1
        array[low], array[high] = array[high], array[low]

    while l <= h:
        compares += 1
        if array[l] < array[low]:
            transpositions += 1
            array[k], array[l] = array[l], array[k]
            k += 1
            l += 1
        elif array[l] > array[high]:
            transpositions += 1
            array[l], array[h] = array[h], array[l]
            h -= 1
        else:
            l += 1

    k -= 1
    h += 1
    transpositions += 1
    array[low], array[k] = array[k], array[low]
    transpositions += 1
    array[high], array[h] = array[h], array[high]
    quickSortDualPivot(array, low, k - 1)
    quickSortDualPivot(array, k + 1, h - 1)
    quickSortDualPivot(array, h + 1, high)

    if ascending:
        return array
    else:
        return array.reverse()


def countingSort(array, exp):
    global compares, transpositions
    lenArr = len(array)
    output = [0] * lenArr
    count = [0] * 10

    for i in range(0, lenArr):
        index = (array[i] / exp)
        count[int(index) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = lenArr - 1
    while i >= 0:
        transpositions += 1
        index = (array[i] / exp)
        output[count[int(index) % 10] - 1] = array[i]
        count[int(index) % 10] -= 1
        i -= 1

    for i in range(0, len(array)):
        array[i] = output[i]


@timer
def radixSort(array, ascending=True):
    global compares, transpositions
    arrayMax = max(array)

    exp = 1
    while arrayMax / exp > 0:
        compares += 1
        countingSort(array, exp)
        exp *= 10

    if ascending:
        return array
    else:
        return array.reverse()


@timer
def selectionSort(array, ascending=True):
    global compares, transpositions
    file = open(filename + ".txt", "w+")
    for i in range(len(array)):
        min_idx = i
        file.write("\nIndex is: %d. Array is:   " % min_idx)
        for element in array:
            file.write("%d " % element)
        for j in range(i + 1, len(array)):
            compares += 1
            if array[min_idx] > array[j]:
                transpositions += 1
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    file.close()
    if ascending:
        return array
    else:
        return array.reverse()


@timer
def rSS(array, pivot):
    file = open(filename + ".txt", "w+")
    randomizedSelectSort(array, pivot, file)


def partitionRS(array, fl, pivot_index=0):
    global compares, transpositions
    newPivot = 0
    fl.write("\nIndex is: %d. Array is: " % pivot_index)
    for el in array:
        fl.write("%d " % el)
    if pivot_index != 0:
        transpositions += 2
        array[0], array[pivot_index] = array[pivot_index], array[0]
    for j in range(len(array) - 1):
        if array[j + 1] < array[0]:
            transpositions += 1
            array[j + 1], array[newPivot + 1] = array[newPivot + 1], array[j + 1]
            newPivot += 1
    array[0], array[newPivot] = array[newPivot], array[0]
    return array, newPivot


def randomizedSelectSort(array, pivot, file):
    global compares, transpositions
    compares += 1
    if len(array) == 1:
        return array[0]
    else:
        xpart = partitionRS(array, file, random.randrange(len(array)))
        x = xpart[0]
        j = xpart[1]
        if j == pivot:
            return x[j]
        elif j > pivot:
            return randomizedSelectSort(x[:j], pivot, file)
        else:
            k = pivot - j - 1
            return randomizedSelectSort(x[(j + 1):], k, file)


def binarySearch(array, left, right, element):
    global compares, transpositions
    if right >= left:
        mid = left + (right - left) // 2
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            return binarySearch(array, left, mid - 1, element)
        else:
            return binarySearch(array, mid + 1, right, element)
    else:
        return -1


@timer
def qSS(array, low, high, ascending):
    quickSelectSort(array, low, high, ascending)


def quickSelectSort(array, low, high, ascending=True):
    global compares, transpositions
    while low < high:
        compares += 1
        if high - low < 1000:
            selectionSort(array, ascending)
            break
        else:
            p = partition(array, low, high)
            if p - low < high - p:
                compares += 1
                quickSelectSort(array, low, p - 1)
                transpositions += 1
                low = p + 1
            else:
                compares += 1
                quickSelectSort(array, p + 1, high)
                transpositions += 1
                high = p - 1
    if ascending:
        return array
    else:
        return array.reverse()


# @timer
# def qRSS(array, low, high, ascending):
#     quickRandomizedSelectSort(array, low, high, ascending)
#
#
# def quickDualRandomizedSelectSort(array, low, high, ascending=True):
#     global compares, transpositions
#     while low < high:
#         compares += 1
#         if high - low < 1000:
#             for pivot in range(len(array)):
#                 randomizedSelectSort(array, pivot, ascending)
#             break
#         else:
#             p = partition(array, low, high)
#             compares += 1
#             if p - low < high - p:
#                 quickRandomizedSelectSort(array, low, p - 1)
#                 low = p + 1
#             else:
#                 quickRandomizedSelectSort(array, p + 1, high)
#                 high = p - 1
#     if ascending:
#         return array
#     else:
#         return array.reverse()


def writeToFile():
    from xlwt import Workbook
    import psutil
    global timeSpent, trans, comp, arLen
    sys.setrecursionlimit(10100)
    wb = Workbook()
    ws = wb.add_sheet("AiSD")
    header = ["Algorithm", "Array Length", "Time Spent", "Compares", "Transpositions"]
    for i in range(100, 10100, 100):
        arrays = random.sample(range(i), i)
        length = len(arrays)

        if filename == "insertion":
            for j in range(int(sys.argv[5])):
                insertion(arrays, length, ascending)
                timeSpent.append('{:.10f}'.format(time).rstrip('0'))
                trans.append(transpositions)
                comp.append(compares)
                arLen.append(length)
        elif filename == "merge":
            for j in range(int(sys.argv[5])):
                merge(arrays, ascending)
                timeSpent.append('{:.10f}'.format(time).rstrip('0'))
                trans.append(transpositions)
                comp.append(compares)
                arLen.append(length)
        elif filename == "quick":
            for j in range(int(sys.argv[5])):
                quick(arrays, 0, length - 1, ascending)
                timeSpent.append('{:.10f}'.format(time).rstrip('0'))
                trans.append(transpositions)
                comp.append(compares)
                arLen.append(length)
        elif filename == "mergequick":
            for j in range(int(sys.argv[5])):
                mqs(arrays, 0, length - 1, ascending)
                timeSpent.append('{:.10f}'.format(time).rstrip('0'))
                trans.append(transpositions)
                comp.append(compares)
                arLen.append(length)
        elif filename == "dual-pivot":
            for j in range(int(sys.argv[5])):
                qsdp(arrays, 0, length - 1, ascending)
                timeSpent.append('{:.10f}'.format(time).rstrip('0'))
                trans.append(transpositions)
                comp.append(compares)
                arLen.append(length)
        elif filename == "radix":
            for j in range(int(sys.argv[5])):
                radixSort(arrays, ascending)
                timeSpent.append('{:.10f}'.format(time).rstrip('0'))
                trans.append(transpositions)
                comp.append(compares)
                arLen.append(length)
        elif filename == "selection":
            for j in range(int(sys.argv[5])):
                selectionSort(arrays, ascending)
                timeSpent.append('{:.10f}'.format(time).rstrip('0'))
                trans.append(transpositions)
                comp.append(compares)
                arLen.append(length)
        elif filename == "randselection":
            for j in range(int(sys.argv[5])):
                for k in range(len(arrays)-1):
                    rSS(arrays, k)
                timeSpent.append('{:.10f}'.format(time).rstrip('0'))
                trans.append(transpositions)
                comp.append(compares)
                arLen.append(length)
        elif filename == "selection":
            for j in range(int(sys.argv[5])):
                selectionSort(arrays, ascending)
                timeSpent.append('{:.10f}'.format(time).rstrip('0'))
                trans.append(transpositions)
                comp.append(compares)
                arLen.append(length)
        elif filename == "quickselect":
            for j in range(int(sys.argv[5])):
                qSS(arrays, 0, length - 1, ascending)
                timeSpent.append('{:.10f}'.format(time).rstrip('0'))
                trans.append(transpositions)
                comp.append(compares)
                arLen.append(length)
        # elif filename == "qrdpselect":
        #     for j in range(int(sys.argv[5])):
        #         qSS(arrays, 0, length - 1, ascending)
        #         timeSpent.append('{:.10f}'.format(time).rstrip('0'))
        #         trans.append(transpositions)
        #         comp.append(compares)
        #         arLen.append(length)
        else:
            print("To proper use of program add arguments --type "
                  "insertion|quick|merge|mergequick|radix|selection|randselection|binarysearch|quickselect "
                  "--comp >=|<=")

    for cols, value in enumerate(header):
        ws.write(0, cols, value)

    rows = 1
    cols = 0

    for i in range(0, len(arLen)):
        ws.write(rows, cols, filename)
        rows += 1

    rows = 1
    cols += 1
    for items in arLen:
        ws.write(rows, cols, items)
        rows += 1

    rows = 1
    cols += 1
    for items in timeSpent:
        ws.write(rows, cols, items)
        rows += 1

    rows = 1
    cols += 1
    for items in comp:
        ws.write(rows, cols, items)
        rows += 1

    rows = 1
    cols += 1
    for items in trans:
        ws.write(rows, cols, items)
        rows += 1

    wb.save(filename + ".xls")



def readFromFile():
    import pandas
    return pandas.read_excel(filename + ".xls")


def main():
    global ascending
    chosen = int(input("Choose option:\n"
                       "1:To enter an array manually\n"
                       "2:To randomly generate numbers and sort it\n"
                       "3:To save data to file\n"
                       "4:To load data from file and build chosen graph\n"))

    if sys.argv[4] == ">=":
        ascending = True
    elif sys.argv[4] == "<=":
        ascending = False
    else:
        print("Enter correct value please")

    if chosen == 1:
        arr = [int(x) for x in input("Give an array: ").split()]
        arrLen = len(arr) - 1
        print("Given array: ", arr.sort() if filename == "binarysearch" else arr, "\nArray length:", arrLen + 1)

        if filename == "insertion":
            insertion(arr, arrLen + 1, ascending)
            print("Sorted with insertion sort:" if ascending else "Reversed insertion sort:", arr, "\nDone in",
                  '{:.10f}'.format(time).rstrip('0'), "seconds, with",
                  compares,
                  "compares and", transpositions, "transpositions")

        elif filename == "merge":
            merge(arr, ascending)
            print("Sorted with merge sort:" if ascending else "Reversed merge sort:", arr, "\nDone in",
                  '{:.10f}'.format(time).rstrip('0'), "seconds, with", compares,
                  "compares and", transpositions, "transpositions")

        elif filename == "quick":
            quick(arr, 0, arrLen, ascending)
            print("Sorted with quick sort:" if ascending else "Reversed quick sort:", arr, "\nDone in",
                  '{:.10f}'.format(time).rstrip('0'), "seconds, with", compares,
                  "compares and", transpositions, "transpositions")

        elif filename == "dual-pivot":
            qsdp(arr, 0, arrLen, ascending)
            print("Sorted with dual pivot quick sort:" if ascending else "Reversed dual pivot quick sort:", arr,
                  "\nDone in", '{:.10f}'.format(time).rstrip('0'), "seconds, with", compares, "compares and",
                  transpositions, "transpositions")

        elif filename == "mergequick":
            mqs(arr, 0, arrLen, ascending)
            print("Sorted with merge and quick sort:" if ascending else "Reversed merge and quick sort:", arr,
                  "\nDone in", '{:.10f}'.format(time).rstrip('0'), "seconds, with",
                  compares, "compares and", transpositions, "transpositions")

        elif filename == "radix":
            radixSort(arr, ascending)
            print("Sorted with radix sort:" if ascending else "Reversed radix sort:", arr,
                  "\nDone in", '{:.10f}'.format(time).rstrip('0'), "seconds, with",
                  compares, "compares and", transpositions, "transpositions")

        elif filename == "selection":
            selectionSort(arr, ascending)
            print("Sorted with selection sort:" if ascending else "Reversed selection sort:", arr,
                  "\nDone in", '{:.10f}'.format(time).rstrip('0'), "seconds, with",
                  compares, "compares and", transpositions, "transpositions")

        elif filename == "randselection":
            for i in range(len(arr) - 1):
                rSS(arr, i, ascending)
            print("Sorted with randomized selection sort:" if ascending else "Reversed randomized selection sort:", arr,
                  "\nDone in", '{:.10f}'.format(time).rstrip('0'), "seconds, with",
                  compares, "compares and", transpositions, "transpositions")

        elif filename == "binarysearch":
            element = int(input("Enter element you want to find: "))
            result = binarySearch(arr, 0, arrLen, element)

            if result != -1:
                print("Element is present at index % d" % result)
            else:
                print("Element is not present in array")
        elif filename == "qucikselect":
            qSS(arr, 0, arrLen, ascending)
            print("Sorted with quick selection sort:" if ascending else "Reversed quick selection sort:", arr,
                  "\nDone in", '{:.10f}'.format(time).rstrip('0'), "seconds, with",
                  compares, "compares and", transpositions, "transpositions")

        else:
            print("To proper use of program add arguments --type "
                  "insertion|quick|merge|mergequick|radix|selection|randselection|binarysearch|quickselect "
                  "--comp >=|<=")
    elif chosen == 2:
        ran = int(input("Enter the range of array(recommended to 10000): "))
        r = int(input("Enter the number of elements to be generated from 0 to %d: " % ran))
        rnd = random.sample(range(ran), r)
        arr = [int(x) for x in rnd]
        arrLen = len(arr) - 1

        print("Given array: ", arr, "\nArray length:", arrLen + 1)

        if filename == "insertion":
            insertion(arr, arrLen + 1, ascending)
            print("Sorted with insertion sort:" if ascending else "Reversed insertion sort:", arr, "\nDone in",
                  '{:.10f}'.format(time).rstrip('0'), "seconds, with",
                  compares, "compares and", transpositions, "transpositions")

        elif filename == "merge":
            merge(arr, ascending)
            print("Sorted with merge sort:" if ascending else "Reversed merge sort:", arr, "\nDone in",
                  '{:.10f}'.format(time).rstrip('0'), "seconds, with", compares,
                  "compares and", transpositions, "transpositions")

        elif filename == "quick":
            quick(arr, 0, arrLen, ascending)
            print("Sorted with quick sort:" if ascending else "Reversed quick sort:", arr, "\nDone in",
                  '{:.10f}'.format(time).rstrip('0'), "seconds, with", compares,
                  "compares and", transpositions, "transpositions")

        elif filename == "dual-pivot":
            qsdp(arr, 0, arrLen, ascending)
            print("Sorted with dual pivot quick sort:" if ascending else "Reversed dual pivot quick sort:", arr,
                  "\nDone in", '{:.10f}'.format(time).rstrip('0'), "seconds, with", compares,
                  "compares and", transpositions, "transpositions")

        elif filename == "mergequick":
            mqs(arr, 0, arrLen, ascending)
            print("Sorted with merge and quick sort:" if ascending else "Reversed merge and quick sort:", arr,
                  "\nDone in", '{:.10f}'.format(time).rstrip('0'), "seconds, with", compares, "compares and",
                  transpositions, "transpositions")

        elif filename == "radix":
            radixSort(arr, ascending)
            print("Sorted with radix sort:" if ascending else "Reversed radix sort:", arr,
                  "\nDone in", '{:.10f}'.format(time).rstrip('0'), "seconds, with",
                  compares, "compares and", transpositions, "transpositions")

        elif filename == "selection":
            selectionSort(arr, ascending)
            print("Sorted with selection sort:" if ascending else "Reversed selection sort:", arr,
                  "\nDone in", '{:.10f}'.format(time).rstrip('0'), "seconds, with",
                  compares, "compares and", transpositions, "transpositions")

        elif filename == "randselection":
            for i in range(len(arr)-1):
                rSS(arr, i)
            print("Sorted with randomized selection sort:" if ascending else "Reversed randomized selection sort:",
                  arr if ascending else arr.reverse(), "\nDone in", '{:.10f}'.format(time).rstrip('0'), "seconds, with",
                  compares, "compares and", transpositions, "transpositions")

        elif filename == "binarysearch":
            element = int(input("Enter element you want to find: "))
            result = binarySearch(arr, 0, len(arr) - 1, element)

            if result != -1:
                print("Element is present at index % d" % result)
            else:
                print("Element is not present in array")
        elif filename == "qucikselect":
            qSS(arr, 0, arrLen, ascending)
            print("Sorted with quick selection sort:" if ascending else "Reversed quick selection sort:", arr,
                  "\nDone in", '{:.10f}'.format(time).rstrip('0'), "seconds, with",
                  compares, "compares and", transpositions, "transpositions")
        else:
            print("To proper use of program add arguments --type "
                  "insertion|quick|merge|mergequick|radix|selection|randselection|binarysearch|quickselect "
                  "--comp >=|<=")

    elif chosen == 3:
        writeToFile()

    elif chosen == 4:
        import matplotlib.pyplot as plot
        graphNum = int(input(
            "1:To build graph which shows the dependence of transpositions divided by array length on array length\n"
            "2:To build graph which shows the dependence of compares divided by array length on array length\n"
            "3:To build graph which shows the dependence of time on array length\n"
            "4:To build graph which shows the dependence of transpositions on array length\n"
            "5:To build graph which shows the dependence of compares on array length\n"))
        file = readFromFile()

        if graphNum == 1:
            graph = file[['Transpositions', 'Array Length']]
            graph['Transpositions'] = file['Transpositions'].div(file['Array Length'])
            graph.plot(x='Array Length', y='Transpositions')
            plot.show()
        elif graphNum == 2:
            graph = file[['Compares', 'Array Length']]
            graph['Compares'] = file['Compares'].div(file['Array Length'])
            graph.plot(x='Array Length', y='Compares')
            plot.show()
        elif graphNum == 3:
            graph = file[['Time Spent', 'Array Length']]
            graph.plot(x='Array Length', y='Time Spent')
            plot.show()
        elif graphNum == 4:
            graph = file[['Transpositions', 'Array Length']]
            graph.plot(x='Array Length', y='Transpositions')
            plot.show()
        elif graphNum == 5:
            graph = file[['Compares', 'Array Length']]
            graph.plot(x='Array Length', y='Compares')
            plot.show()
        else:
            print("Enter correct value please")
    else:
        "Enter 1, 2, 3 or 4 please"

    # print(arr, arrLen, ascending, '{:.10f}'.format(time).rstrip('0'), compares, transpositions)


if __name__ == "__main__":
    main()
