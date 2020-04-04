import random
import sys
import timeit
import pandas
from xlwt import Workbook
import matplotlib.pyplot as plot

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
        print("Sort was completed in", '{:.10f}'.format(time).rstrip('0'), "seconds")
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


def writeToFile():
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
        else:
            print("To proper use of program use --type insertion|quick|merge --comp >=|<=")

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
    return pandas.read_excel(filename + ".xls")


def main():
    global ascending
    chosen = int(input("Choose option:\n"
                       "1:To enter an array manually\n"
                       "2:To randomly generate 15 numbers and sort it\n"
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
        print("Given array: ", arr, "\nArray length:", arrLen + 1)

        if sys.argv[2] == "insertion":
            insertion(arr, arrLen + 1, ascending)
            print("Sorted with insertion sort:" if ascending else "Reversed insertion sort:", arr, "\nDone in",
                  '{:.10f}'.format(time).rstrip('0'), "seconds, with",
                  compares,
                  "compares and", transpositions, "transpositions")
        elif sys.argv[2] == "merge":
            merge(arr, ascending)
            print("Sorted with merge sort:" if ascending else "Reversed merge sort:", arr, "\nDone in",
                  '{:.10f}'.format(time).rstrip('0'), "seconds, with", compares,
                  "compares and", transpositions, "transpositions")
        elif sys.argv[2] == "quick":
            quick(arr, 0, arrLen, ascending)
            print("Sorted with quick sort:" if ascending else "Reversed quick sort:", arr, "\nDone in",
                  '{:.10f}'.format(time).rstrip('0'), "seconds, with", compares,
                  "compares and", transpositions, "transpositions")
        elif sys.argv[2] == "dual-pivot":
            qsdp(arr, 0, arrLen, ascending)
            print("Sorted with dual pivot quick sort:" if ascending else "Reversed dual pivot quick sort:", arr,
                  "\nDone in", '{:.10f}'.format(time).rstrip('0'), "seconds, with", compares, "compares and",
                  transpositions, "transpositions")
        elif sys.argv[2] == "mergequick":
            mqs(arr, 0, arrLen, ascending)
            print("Sorted with merge and quick sort:" if ascending else "Reversed merge and quick sort:", arr,
                  "\nDone in",
                  compares, "compares and", transpositions, "transpositions")
        else:
            print("To proper use of program use --type insertion|quick|merge --comp >=|<=")

    elif chosen == 2:
        rnd = random.sample(range(100), 15)
        arr = [int(x) for x in rnd]
        arrLen = len(arr) - 1
        print("Given array: ", arr, "\nArray length:", arrLen + 1)

        if sys.argv[2] == "insertion":
            insertion(arr, arrLen + 1, ascending)
            print("Sorted with insertion sort:" if ascending else "Reversed insertion sort:", arr, "\nDone in",
                  '{:.10f}'.format(time).rstrip('0'), "seconds, with",
                  compares, "compares and", transpositions, "transpositions")
        elif sys.argv[2] == "merge":
            merge(arr, ascending)
            print("Sorted with merge sort:" if ascending else "Reversed merge sort:", arr, "\nDone in",
                  '{:.10f}'.format(time).rstrip('0'), "seconds, with", compares,
                  "compares and", transpositions, "transpositions")
        elif sys.argv[2] == "quick":
            quick(arr, 0, arrLen, ascending)
            print("Sorted with quick sort:" if ascending else "Reversed quick sort:", arr, "\nDone in",
                  '{:.10f}'.format(time).rstrip('0'), "seconds, with", compares,
                  "compares and", transpositions, "transpositions")
        elif sys.argv[2] == "dual-pivot":
            qsdp(arr, 0, arrLen, ascending)
            print("Sorted with dual pivot quick sort:" if ascending else "Reversed dual pivot quick sort:", arr,
                  "\nDone in", '{:.10f}'.format(time).rstrip('0'), "seconds, with", compares,
                  "compares and", transpositions, "transpositions")
        elif sys.argv[2] == "mergequick":
            mqs(arr, 0, arrLen, ascending)
            print("Sorted with merge and quick sort:" if ascending else "Reversed merge and quick sort:", arr,
                  "\nDone in", '{:.10f}'.format(time).rstrip('0'), "seconds, with", compares, "compares and",
                  transpositions, "transpositions")
        else:
            print("To proper use of program use --type insertion|quick|merge --comp >=|<=")

    elif chosen == 3:
        writeToFile()

    elif chosen == 4:
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
