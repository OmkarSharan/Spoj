class Deque:
    def __init__(self):
        self.items = []
        self.size = 0

    def isEmpty(self):
        return self.items == []
    def parent(self, i):
        return (i - 1)//2

    def insertRear(self, item):
        self.size = len(self.items)
        self.size = self.size + 1
        i = self.size - 1
        self.items.insert(0, item)
        while i != 0 and self.items[self.parent(i)] > self.items[i]:
            self.items[self.parent(i)], self.items[i] = self.items[i], self.items[self.parent(i)]
            i = self.parent(i)

    def BuildDepq(self, file):
        fp = open(file, "r")
        i = 0
        for line in fp:
            if i == 0:
                i = 1
                continue
            self.insertRear(line.strip('\n'))
           # self.items.insert(0, line.strip('\n'))

    def Minheapify(self, i):
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < len(self.items) and self.items[i] > self.items[l]:
            smallest = l
        if r < len(self.items) and self.items[smallest] > self.items[r]:
            smallest = r
        if smallest != i:
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            self.Maxheapify(smallest)


    def Maxheapify(self, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < len(self.items) and self.items[i] < self.items[l]:
            largest = l

        # See if right child of root exists and is
        # greater than root
        if r < len(self.items) and self.items[largest] < self.items[r]:
            largest = r

        # Change root, if needed
        if largest != i:
            self.items[i], self.items[largest] = self.items[largest], self.items[i]  # swap

            # Heapify the root.
            self.Maxheapify(largest)

    # The main function to sort an array of given size
    def heapSort(self, arr):
        n = len(arr)

        # Build a maxheap.
        for i in range(n, -1, -1):
            self.Maxheapify(arr, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.Maxheapify(arr, i, 0)

    def getMin(self):
        return self.items[0]


    def getMax(self):
        return self.items[0]

    def removeFront(self):
        self.items.pop()
    def extractMin(self):
        if len(self.items) == 1:
            self.size = self.size - 1
            return self.items[0]
        root = self.items[0]
        self.items.remove(self.items[0])
        self.items[0] = self.items[self.size - 1]
        self.size = self.size - 1
        self.Minheapify(0)
        self.Maxheapify(0)
        return root

    def extractMax(self):
        if len(self.items) == 1:
            self.size = self.size - 1
            return self.items[0]
        root = self.items[0]
        self.items.remove(self.items[0])
        self.items[0] = self.items[self.size - 1]
        self.size = self.size - 1
        self.Maxheapify(0)
        self.Minheapify(0)
        return root

    def removeRear(self):
        self.items.pop(0)

    def printQue(self):
        print(self.items)

    def size(self):
        return len(self.items)

    def IsContain(self, x):
        if x in self.items:
            return True
        else:
            return False


q = Deque()

while True:
    print("enter your choise: 1.IsEmpty  2.insert  3.getMin  4.getMax  5.RemoveMin  6.RemoveMax  7.size  8.printQue  9.Buildenque 10.Isconatain")
    choice = int(input())
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
        print(q.extractMin())
    if choice == 4:
        print(q.extractMax())
    if choice == 5:
        q.removeFront()
    if choice == 6:
        q.removeRear()
    if choice == 7:
        print(q.size())
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
