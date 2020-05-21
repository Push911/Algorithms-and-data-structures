import datetime
from random import randint

route = []
countInsert = countDelete = countFind = countFindMin = countFindMax = countInOrder = countPostOrder = countTreeCreate \
    = countDeleteTree = 0


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


class treeBST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        global countInsert
        countInsert += 1
        if root.data < data.data:
            if root.right is None:
                root.right = data
            else:
                self.insert(root.right, data)
        else:
            if root.left is None:
                root.left = data
            else:
                self.insert(root.left, data)

    def search(self, root, key):
        global countFind
        countFind += 1
        if root is None:
            print("Key doesn't exist")
            return root
        if root.data == key:
            route.append(key)
            print("Route is: ", route)
            return root

        if root.data < key:
            route.append(root.data)
            return self.search(root.right, key)

        route.append(root.data)
        return self.search(root.left, key)

    def inOrder(self, root):
        global countInOrder
        countInOrder += 1
        if root:
            self.inOrder(root.left)
            print(root.data, end=" ")
            self.inOrder(root.right)

    def postOrder(self, root):
        global countPostOrder
        countPostOrder += 1
        if root:
            self.postOrder(root.right)
            print(root.data, end=" ")
            self.postOrder(root.left)


def createTree(root, amountOfElements=20, rangeOfNumbers=100):
    global countTreeCreate
    countTreeCreate += 1
    for _ in range(amountOfElements - 1):
        element = randint(10, rangeOfNumbers)
        tree.insert(root, Node(element))
    return tree


def minElement(key):
    global countFindMin
    countFindMin += 1
    while key.left is not None:
        key = key.left
    return key.data


def maxElement(key):
    global countFindMax
    countFindMax += 1
    while key.right is not None:
        key = key.right
    return key.data


def height(key):
    if key is None:
        return 0
    else:
        return 1 + max(height(key.left), height(key.right))


def deleteTree(key):
    global countDeleteTree
    countDeleteTree += 1
    if key is None:
        return 0

    deleteTree(key.left)
    deleteTree(key.right)
    print("Deleting node:", key.data)


def deleteNode(root, key):
    global countDelete
    countDelete += 1
    if root is None:
        return root

    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            return temp
        elif root.right is None:
            temp = root.left
            return temp

        temp = minElement(root.right)
        root.data = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root


tree = treeBST()
option = int(input("1: Create a random tree\n2: Enter the numbers manually\n3: Read from file"))
if option is 1:
    start = datetime.datetime.now()
    rt = Node(randint(1, 100))
    createTree(rt)
    print("Tree created within {} seconds".format(datetime.datetime.now() - start))
    print("\nIn order traversal: ", end="")
    tree.inOrder(rt)
    print("\nPost order traversal: ", end="")
    tree.postOrder(rt)
    while True:
        route = []
        todo = int(input("\n\nEnter what you want to do:\n1: Find the element in tree\n2: Find min element in tree\n"
                         "3: Find max element in tree\n4: Tree height\n5: Delete tree in post order\n"
                         "6: Delete number from the tree\n7: Exit"))
        if todo is 1:
            value = int(input("Enter element which you want to find out: "))
            tree.search(rt, value)
        elif todo is 2:
            start = datetime.datetime.now()
            print("Min element in tree is:", minElement(rt),
                  end="\nMin found within {} seconds\n".format(datetime.datetime.now() - start))
            tree.search(rt, minElement(rt))
        elif todo is 3:
            start = datetime.datetime.now()
            print("Max element in tree is:", maxElement(rt),
                  end="\nMax found within {} seconds\n".format(datetime.datetime.now() - start))
            tree.search(rt, maxElement(rt))
        elif todo is 4:
            start = datetime.datetime.now()
            print("Height of tree is: ", height(rt),
                  end="\nHeight found within {} seconds\n".format(datetime.datetime.now() - start))
        elif todo is 5:
            start = datetime.datetime.now()
            deleteTree(rt)
            rt = None
            print("Tree deleted in post order within {} seconds".format(datetime.datetime.now() - start),
                  end="\nYou can try to check that tree is removed or exit(7)")
        elif todo is 6:
            value = int(input("Enter element to delete from tree"))
            deleteNode(rt, value)
            print("\nIn order traversal: ", end="")
            tree.inOrder(rt)
            print("\nPost order traversal: ", end="")
            tree.postOrder(rt)
        elif todo is 7:
            print("\nProgram worked within ", datetime.datetime.now() - start,
                  " seconds.\nUsed function createTree ", countTreeCreate,
                  " times.\nUsed function insert ", countInsert,
                  " times.\nUsed function search(find element) ", countFind,
                  " times.\nUsed function minElement(find min) ", countFindMin,
                  " times.\nUsed function maxElement(find max) ", countFindMax,
                  " times.\nUsed function inOrder ", countInOrder,
                  " times.\nUsed function postOrder ", countPostOrder,
                  " times.\nUsed function deleteTree ", countDeleteTree,
                  " times.\nUsed function deleteNode ", countDelete, " times.")
            break
        else:
            print("Enter proper value please")

if option is 2:
    amountOfNumbers = int(input("Enter the amount of numbers: "))
    for i in range(amountOfNumbers):
        if i is 0:
            rt = Node(int(input("Enter number which you want to add to the tree: ")))
        elif i > 0:
            element = int(input("Enter number which you want to add to the tree: "))
            tree.insert(rt, Node(element))
        else:
            print("Enter number please")

    print("\nIn order traversal: ", end="")
    tree.inOrder(rt)
    print("\nPost order traversal: ", end="")
    tree.postOrder(rt)
    start = datetime.datetime.now()
    while True:
        route = []
        todo = int(input("\n\nEnter what you want to do:\n1: Find the element in tree\n2: Find min element in tree\n"
                         "3: Find max element in tree\n4: Tree height\n5: Delete tree in post order\n"
                         "6: Delete number from the tree\n7: Exit"))
        if todo is 1:
            start = datetime.datetime.now()
            value = int(input("Enter element which you want to find out: "))
            tree.search(rt, value)
            print("Found within {} seconds".format(datetime.datetime.now() - start))
        elif todo is 2:
            start = datetime.datetime.now()
            print("Min element in tree is:", minElement(rt),
                  end="\nMin found within {} seconds\n".format(datetime.datetime.now() - start))
            tree.search(rt, minElement(rt))
        elif todo is 3:
            start = datetime.datetime.now()
            print("Max element in tree is:", maxElement(rt),
                  end="\nMax found within {} seconds\n".format(datetime.datetime.now() - start))
            tree.search(rt, maxElement(rt))
        elif todo is 4:
            start = datetime.datetime.now()
            print("Height of tree is: ", height(rt),
                  end="\nHeight found within {} seconds\n".format(datetime.datetime.now() - start))
        elif todo is 5:
            start = datetime.datetime.now()
            deleteTree(rt)
            rt = None
            print("Tree deleted in post order within {} seconds".format(datetime.datetime.now() - start),
                  end="\nYou can try to check that tree is removed or exit(7)")
        elif todo is 6:
            value = int(input("Enter element to delete from tree"))
            deleteNode(rt, value)
            print("\nIn order traversal: ", end="")
            tree.inOrder(rt)
            print("\nPost order traversal: ", end="")
            tree.postOrder(rt)
        elif todo is 7:
            print("\nProgram worked within ", datetime.datetime.now() - start,
                  " seconds.\nUsed function createTree ", countTreeCreate,
                  " times.\nUsed function insert ", countInsert,
                  " times.\nUsed function search(find element) ", countFind,
                  " times.\nUsed function minElement(find min) ", countFindMin,
                  " times.\nUsed function maxElement(find max) ", countFindMax,
                  " times.\nUsed function inOrder ", countInOrder,
                  " times.\nUsed function postOrder ", countPostOrder,
                  " times.\nUsed function deleteTree ", countDeleteTree,
                  " times.\nUsed function deleteNode ", countDelete, " times.")
            break
        else:
            print("Enter proper value please")
if option is 3:
    start = datetime.datetime.now()
    file = open(input("Enter the file title with extension"))
    for line in file:
        numbers = line.split(" ")
        rt = Node(int(numbers[0]))
        numbers.remove(numbers[0])
        for number in numbers:
            tree.insert(rt, Node(int(number)))

    print("Tree created within {} seconds".format(datetime.datetime.now() - start))
    print("\nIn order traversal: ", end="")
    tree.inOrder(rt)
    print("\nPost order traversal: ", end="")
    tree.postOrder(rt)
    while True:
        route = []
        todo = int(input("\n\nEnter what you want to do:\n1: Find the element in tree\n2: Find min element in tree\n"
                         "3: Find max element in tree\n4: Tree height\n5: Delete tree in post order\n"
                         "6: Delete number from the tree\n7: Exit"))
        if todo is 1:
            value = int(input("Enter element which you want to find out: "))
            tree.search(rt, value)
        elif todo is 2:
            start = datetime.datetime.now()
            print("Min element in tree is:", minElement(rt),
                  end="\nMin found within {} seconds\n".format(datetime.datetime.now() - start))
            tree.search(rt, minElement(rt))
        elif todo is 3:
            start = datetime.datetime.now()
            print("Max element in tree is:", maxElement(rt),
                  end="\nMax found within {} seconds\n".format(datetime.datetime.now() - start))
            tree.search(rt, maxElement(rt))
        elif todo is 4:
            start = datetime.datetime.now()
            print("Height of tree is: ", height(rt),
                  end="\nHeight found within {} seconds\n".format(datetime.datetime.now() - start))
        elif todo is 5:
            start = datetime.datetime.now()
            deleteTree(rt)
            rt = None
            print("Tree deleted in post order within {} seconds".format(datetime.datetime.now() - start),
                  end="\nYou can try to check that tree is removed or exit(7)")
        elif todo is 6:
            value = int(input("Enter element to delete from tree"))
            deleteNode(rt, value)
            print("\nIn order traversal: ", end="")
            tree.inOrder(rt)
            print("\nPost order traversal: ", end="")
            tree.postOrder(rt)
        elif todo is 7:
            print("\nProgram worked within ", datetime.datetime.now() - start,
                  " seconds.\nUsed function createTree ", countTreeCreate,
                  " times.\nUsed function insert ", countInsert,
                  " times.\nUsed function search(find element) ", countFind,
                  " times.\nUsed function minElement(find min) ", countFindMin,
                  " times.\nUsed function maxElement(find max) ", countFindMax,
                  " times.\nUsed function inOrder ", countInOrder,
                  " times.\nUsed function postOrder ", countPostOrder,
                  " times.\nUsed function deleteTree ", countDeleteTree,
                  " times.\nUsed function deleteNode ", countDelete, " times.")
            break
        else:
            print("Enter proper value please")

