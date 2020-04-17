Program had 2 codes use Sort.py to use only sort it means only options 1 and 2 will be available(no libraries needed)

To see the full Program launch Sorts.py

To launch program add this args to console:    --type insertion|quick|merge|mergequick|radix|selection|randselection|binarysearch|quickselect --comp >=|<= 1

Example: --type merge --comp >= 1

Full example: python3 Sorts.py --type merge --comp >= 1
sys.argv[1] = --type
sys.argv[2] = type of sort  (insertion|quick|merge|mergequick|radix|selection|randselection|binarysearch|quickselect)
sys.argv[3] = --comp
sys.argv[4] = order of sort (>= | <=)
sys.argv[5] = amount of times array will be sorted at given length(1-100) optimal


After launch, program asks for an input: 1.Enter numbers manually(Enter numbers and split them with space)
                                         2.Randomly generate it
                                         3.Save to file
                                         4.Load from file and build a graph

Example: 15 16 19 4 11 10 8 14 3 0 21 1

To use 4 option, firstly you must to save data to file, it means use 3 option at first.
Then you can build the data based graph
Note: Option 3 and 4 makes or reads argv[2].xls file, it means if yours argv[2] is "quick", it will make or read file named quick.xls