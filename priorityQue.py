class Deque:
    def BuildDepq(self, file):
        fp = open(file, "r")
        i = 0
        for line in fp:
            if i == 0:
                i = 1
                continue
            self.items.insert(0, line.strip('\n'))
        self.heapSort(self.items)

    def heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l

        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r

        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap

            # Heapify the root.
            self.heapify(arr, n, largest)

    # The main function to sort an array of given size
    def heapSort(self, arr):
        n = len(arr)

        # Build a maxheap.
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.heapify(arr, i, 0)

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insertRear(self, item):
        self.items.insert(0,item)
        self.heapSort(self.items)

    def getMin(self):
        return self.items[len(self.items) - 1]

    def getMax(self):
        return self.items[0]

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)

    def printQue(self):
        print("----------------------------------------------------------------------------")
        print(self.items)
        print("----------------------------------------------------------------------------")

    def size(self):
        return len(self.items)

    def IsContain(self, x):
        if x in self.items:
            return True
        else:
            return False


q = Deque()

while True:
    print("enter your choise: \n1.IsEmpty\n2.insert\n3.getMin\n4.getMax\n5.RemoveMin\n6.RemoveMax \n7.size\n8.printQue\n9.Buildenque\n10.Isconatain")
    choice = int(input())
    print(" ")
    if choice == 1:
        if q.isEmpty():
            print("list is empty")
        else:
            print("list is not empty")

    if choice == 2:
        print("enter the value to be inserted")
        item = input()
        q.insertRear(item)
    if choice == 3:
        print(q.getMin())
        print("\n")
    if choice == 4:
        print(q.getMax())
        print('\n')
    if choice == 5:
        q.removeFront()
    if choice == 6:
        q.removeRear()
    if choice == 7:
        print(q.size())
        print("\n")
    if choice == 8:
        q.printQue()
    if choice == 9:
        print("enter the file name")
        file = input()
        q.BuildDepq(file)
    if choice == 10:
        print("ente the key to search")
        key = input()
        if q.IsContain(key):
            print("Present")
        else:
            print("not Present")

