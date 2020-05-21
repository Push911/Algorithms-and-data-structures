import datetime
from random import randint

route = []
countInsert = countDelete = countFind = countFindMin = countFindMax = countInOrder = countPostOrder = countTreeCreate \
    = countDeleteTree = rt = 0


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree:
    def __init__(self):
        self.data = Node(0)
        self.data.color = 0
        self.data.left = None
        self.data.right = None
        self.root = self.data

    def __findElement(self, root, key):
        global countFind
        countFind += 1
        if root is None:
            print("Key doesn't exist")
            return root
        if root.data == key:
            route.append(key)
            print("Key {} found.Route is: ".format(key), route)
            return root

        if root.data < key:
            route.append(root.data)
            return self.__findElement(root.right, key)

        route.append(root.data)
        return self.__findElement(root.left, key)

    def __fix_delete(self, node):
        while node is not self.root and node.color is 0:
            if node is node.parent.left:
                parent = node.parent.right
                if parent.color is 1:
                    parent.color = 0
                    node.parent.color = 1
                    self.rotateLeft(node.parent)
                    parent = node.parent.right

                if parent.left.color is 0 and parent.right.color is 0:
                    parent.color = 1
                    node = node.parent
                else:
                    if parent.right.color is 0:
                        parent.left.color = 0
                        parent.color = 1
                        self.rotateRight(parent)
                        parent = node.parent.right
                    parent.color = node.parent.color
                    node.parent.color = 0
                    parent.right.color = 0
                    self.rotateLeft(node.parent)
                    node = self.root
            else:
                parent = node.parent.left
                if parent.color is 1:
                    parent.color = 0
                    node.parent.color = 1
                    self.rotateRight(node.parent)
                    parent = node.parent.left

                if parent.left.color is 0 and parent.right.color is 0:
                    parent.color = 1
                    node = node.parent
                else:
                    if parent.left.color is 0:
                        parent.right.color = 0
                        parent.color = 1
                        self.rotateLeft(parent)
                        parent = node.parent.left
                    parent.color = node.parent.color
                    node.parent.color = 0
                    parent.left.color = 0
                    self.rotateRight(node.parent)
                    node = self.root
        node.color = 0

    def __rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __deleteNode(self, node, key):
        global countDelete
        countDelete += 1
        data = self.data
        while node is not self.data:
            if node.data is key:
                data = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if data is self.data:
            print("Couldn't find key in the tree")
            return

        dt = data
        dataColor = dt.color
        if data.left is self.data:
            x = data.right
            self.__rb_transplant(data, data.right)
        elif data.right is self.data:
            x = data.left
            self.__rb_transplant(data, data.left)
        else:
            dt = self.__minElement(data.right)
            dataColor = dt.color
            x = dt.right
            if dt.parent is data:
                x.parent = dt
            else:
                self.__rb_transplant(dt, dt.right)
                dt.right = data.right
                dt.right.parent = dt

            self.__rb_transplant(data, dt)
            dt.left = data.left
            dt.left.parent = dt
            dt.color = data.color
        if dataColor is 0:
            self.__fix_delete(x)

    def __fixInsert(self, key):
        while key.parent.color is 1:
            if key.parent is key.parent.parent.right:
                u = key.parent.parent.left  # uncle
                if u.color is 1:
                    u.color = 0
                    key.parent.color = 0
                    key.parent.parent.color = 1
                    key = key.parent.parent
                else:
                    if key is key.parent.left:
                        key = key.parent
                        self.rotateRight(key)
                    key.parent.color = 0
                    key.parent.parent.color = 1
                    self.rotateLeft(key.parent.parent)
            else:
                u = key.parent.parent.right  # uncle

                if u.color is 1:
                    u.color = 0
                    key.parent.color = 0
                    key.parent.parent.color = 1
                    key = key.parent.parent
                else:
                    if key is key.parent.right:
                        key = key.parent
                        self.rotateLeft(key)
                    key.parent.color = 0
                    key.parent.parent.color = 1
                    self.rotateRight(key.parent.parent)
            if key is self.root:
                break
        self.root.color = 0

    def __print(self, node, indent, last):
        if node is not self.data:
            print(indent, end="")
            if last:
                print("R---", end="")
                indent += "    "
            else:
                print("L---", end="")
                indent += "|   "

            color = "RED" if node.color is 1 else "BLACK"
            print(str(node.data) + "({})".format(color))
            self.__print(node.left, indent, False)
            self.__print(node.right, indent, True)

    def __inOrder(self, node):
        global countInOrder
        countInOrder += 1
        if node is not self.data:
            self.__inOrder(node.left)
            print(node.data, end=" ")
            self.__inOrder(node.right)

    def __postOrder(self, node):
        global countPostOrder
        countPostOrder += 1
        if node is not self.data:
            self.__postOrder(node.right)
            print(node.data, end=" ")
            self.__postOrder(node.left)

    def inOrder(self):
        self.__inOrder(self.root)

    def postOrder(self):
        self.__postOrder(self.root)

    def search(self, key):
        return self.__findElement(self.root, key)

    def __minElement(self, node):
        global countFindMin
        countFindMin += 1
        while node.left is not None:
            route.append(node.data)
            node = node.left
        return node

    def minElement(self):
        self.__minElement(self.root)

    def __maxElement(self, node):
        global countFindMax
        countFindMax += 1
        while node.right is not None:
            route.append(node.data)
            node = node.right
        return node.data

    def maxElement(self):
        self.__maxElement(self.root)

    def successor(self, node):
        if node.right is not self.data:
            return self.__minElement(node.right)
        parent = node.parent
        while parent is not self.data and node is parent.right:
            node = parent
            parent = parent.parent
        return parent

    def predecessor(self, node):
        if node.left is not self.data:
            return self.__maxElement(node.left)
        parent = node.parent
        while parent is not self.data and node is parent.left:
            node = parent
            parent = parent.parent
        return parent

    def rotateLeft(self, node):
        right = node.right
        node.right = right.left
        if right.left is not self.data:
            right.left.parent = node
        right.parent = node.parent
        if node.parent is None:
            self.root = right
        elif node is node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right
        right.left = node
        node.parent = right

    def rotateRight(self, node):
        left = node.left
        node.left = left.right
        if left.right is not self.data:
            left.right.parent = node

        left.parent = node.parent
        if node.parent is None:
            self.root = left
        elif node is node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left
        left.right = node
        node.parent = left

    def insert(self, key):
        global countInsert
        countInsert += 1
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.data
        node.right = self.data
        node.color = 1

        rt = None
        root = self.root
        while root is not self.data:
            rt = root
            if node.data < root.data:
                root = root.left
            else:
                root = root.right

        node.parent = rt
        if rt is None:
            self.root = node
        elif node.data < rt.data:
            rt.left = node
        else:
            rt.right = node

        if node.parent is None:
            node.color = 0
            return 0

        if node.parent.parent is None:
            return 0
        self.__fixInsert(node)

    def __height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.__height(node.left), self.__height(node.right))

    def height(self):
        return self.__height(self.root)

    def deleteNode(self, data):
        self.__deleteNode(self.root, data)

    def prettyPrint(self):
        self.__print(self.root, "", True)

    def __deleteTree(self, node):
        global countDeleteTree
        countDeleteTree += 1
        if node is None:
            return 0

        self.__deleteTree(node.left)
        self.__deleteTree(node.right)
        print("Deleting node:", node.data)
        self.root = None
        node.data = None

    def deleteTree(self):
        return self.__deleteTree(self.root)


def createTree(amountOfElements=20, rangeOfNumbers=100):
    global countTreeCreate
    countTreeCreate += 1
    for _ in range(amountOfElements):
        element = randint(amountOfElements, rangeOfNumbers)
        tree.insert(element)
    return tree


tree = RedBlackTree()
option = int(input("1: Create random tree\n2: Create tree manually\n3: Load data from file"))
if option is 1:
    start = datetime.datetime.now()
    createTree()
    print("Tree created within {} seconds".format(datetime.datetime.now() - start))
    print("Tree is: ")
    tree.prettyPrint()
    print("\nIn order traversal: ", end="")
    tree.inOrder()
    print("\nPost order traversal: ", end="")
    tree.postOrder()
    while True:
        route = []
        todo = int(input("\n\nEnter what you want to do:\n1: Find the element in tree\n2: Find min element in tree\n"
                         "3: Find max element in tree\n4: Tree height\n5: Delete tree in post order\n"
                         "6: Delete number from the tree\n7: Exit"))
        if todo is 1:
            value = int(input("Enter element which you want to find out: "))
            tree.search(value)
        elif todo is 2:
            start = datetime.datetime.now()
            tree.minElement()
            print("Min element in tree is:", route[-1], "\nRoute to min element is: ", route,
                  end="\nMin found within {} seconds\n".format(datetime.datetime.now() - start))
        elif todo is 3:
            start = datetime.datetime.now()
            tree.maxElement()
            print("Max element in tree is:", route[-1], "\nRoute to max element is: ", route,
                  end="\nMax found within {} seconds\n".format(datetime.datetime.now() - start))
        elif todo is 4:
            start = datetime.datetime.now()
            print("Height of tree is: ", tree.height(),
                  end="\nHeight found within {} seconds\n".format(datetime.datetime.now() - start))
        elif todo is 5:
            start = datetime.datetime.now()
            tree.deleteTree()
            print("Tree deleted in post order within {} seconds".format(datetime.datetime.now() - start),
                  end="\nYou can try to check that tree is removed or exit(7)")
        elif todo is 6:
            value = int(input("Enter element to delete from tree"))
            tree.deleteNode(value)
            tree.prettyPrint()
            print("\nIn order traversal: ", end="")
            tree.inOrder()
            print("\nPost order traversal: ", end="")
            tree.postOrder()
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
    start = datetime.datetime.now()
    amountOfNumbers = int(input("Enter the amount of numbers: "))
    for i in range(amountOfNumbers):
        element = int(input("Enter number which you want to add to the tree: "))
        tree.insert(element)
    start = datetime.datetime.now()
    print("Tree created within {} seconds".format(datetime.datetime.now() - start))
    print("Tree is: ")
    tree.prettyPrint()
    print("\nIn order traversal: ", end="")
    tree.inOrder()
    print("\nPost order traversal: ", end="")
    tree.postOrder()
    while True:
        route = []
        todo = int(input("\n\nEnter what you want to do:\n1: Find the element in tree\n2: Find min element in tree\n"
                         "3: Find max element in tree\n4: Tree height\n5: Delete tree in post order\n"
                         "6: Delete number from the tree\n7: Exit"))
        if todo is 1:
            value = int(input("Enter element which you want to find out: "))
            tree.search(value)
        elif todo is 2:
            start = datetime.datetime.now()
            tree.minElement()
            print("Min element in tree is:", route[-1], "\nRoute to min element is: ", route,
                  end="\nMin found within {} seconds\n".format(datetime.datetime.now() - start))
        elif todo is 3:
            start = datetime.datetime.now()
            tree.maxElement()
            print("Max element in tree is:", route[-1], "\nRoute to max element is: ", route,
                  end="\nMax found within {} seconds\n".format(datetime.datetime.now() - start))
        elif todo is 4:
            start = datetime.datetime.now()
            print("Height of tree is: ", tree.height(),
                  end="\nHeight found within {} seconds\n".format(datetime.datetime.now() - start))
        elif todo is 5:
            start = datetime.datetime.now()
            tree.deleteTree()
            print("Tree deleted in post order within {} seconds".format(datetime.datetime.now() - start),
                  end="\nYou can try to check that tree is removed or exit(7)")
        elif todo is 6:
            value = int(input("Enter element to delete from tree"))
            tree.deleteNode(value)
            tree.prettyPrint()
            print("\nIn order traversal: ", end="")
            tree.inOrder()
            print("\nPost order traversal: ", end="")
            tree.postOrder()
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
        numbers.remove(numbers[0])
        for number in numbers:
            tree.insert(int(number))
    print("Tree created within {} seconds".format(datetime.datetime.now() - start))
    print("Tree is: ")
    tree.prettyPrint()
    print("\nIn order traversal: ", end="")
    tree.inOrder()
    print("\nPost order traversal: ", end="")
    tree.postOrder()
    while True:
        route = []
        todo = int(input("\n\nEnter what you want to do:\n1: Find the element in tree\n2: Find min element in tree\n"
                         "3: Find max element in tree\n4: Tree height\n5: Delete tree in post order\n"
                         "6: Delete number from the tree\n7: Exit"))
        if todo is 1:
            value = int(input("Enter element which you want to find out: "))
            tree.search(value)
        elif todo is 2:
            start = datetime.datetime.now()
            tree.minElement()
            print("Min element in tree is:", route[-1], "\nRoute to min element is: ", route,
                  end="\nMin found within {} seconds\n".format(datetime.datetime.now() - start))
        elif todo is 3:
            start = datetime.datetime.now()
            tree.maxElement()
            print("Max element in tree is:", route[-1], "\nRoute to max element is: ", route,
                  end="\nMax found within {} seconds\n".format(datetime.datetime.now() - start))
        elif todo is 4:
            start = datetime.datetime.now()
            print("Height of tree is: ", tree.height(),
                  end="\nHeight found within {} seconds\n".format(datetime.datetime.now() - start))
        elif todo is 5:
            start = datetime.datetime.now()
            tree.deleteTree()
            print("Tree deleted in post order within {} seconds".format(datetime.datetime.now() - start),
                  end="\nYou can try to check that tree is removed or exit(7)")
        elif todo is 6:
            value = int(input("Enter element to delete from tree"))
            tree.deleteNode(value)
            tree.prettyPrint()
            print("\nIn order traversal: ", end="")
            tree.inOrder()
            print("\nPost order traversal: ", end="")
            tree.postOrder()
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
