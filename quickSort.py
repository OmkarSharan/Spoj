def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

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
        arr[i],arr[largest] = arr[largest],arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)


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
def readFeli(file, start, count):
    fp = open(file, 'r')
    lis = []
    i = 0
    for line in fp:
        lis.insert(i, line.strip('\n'))
        i = i + 1
    heapSort(lis)
    fp = open('result.txt', 'w')
    for line in lis:
        fp.write(line)
        fp.write('\n')
    #print(lis)

def extractMin(arr):
    size = len(arr)
    if len(arr) == 1:
        size = size - 1
        return arr[0]
    root = arr[0]
    arr[0] = arr[size - 1]
    size = size - 1
    Minheapify(0)
    Maxheapify(0)
    return root


def extractMax(arr):
    size = len(arr)
    if len(arr) == 1:
        size = size - 1
        return arr[0]
    root = arr[0]
    arr[0] = arr[size - 1]
    size = size - 1
    Minheapify(0)
    Maxheapify(0)
    return root

def readFile(startend, lastend):
    f = open('file','r')
    l = open('left.txt','w')
    r = open('right.txt','w')
    arr = []
    i = 0
    count = 0
    for line in f:
        arr.insert(i, line.strip('\n'))
        i = i + 1
        if line == "" or i == 100:
            counr = count + 1
    heapSort(arr)
    if lastend - startend < 100: # base condition
        return
    smallest = arr[0]
    largest = arr[len(arr) - 1]
    flag = 0
    for line1 in f:
        count = count - 1
        if count > 0:
            continue
        if line < smallest:
            l.write(line.strip('\n'))
        if line > largest:
            r.write(line.strip('\n'))
        elif line > smallest and line < largest:
            if flag == 0:
                l.write(arr[0])
                arr[0] = line.strip('\n')
                flag = 1
            else:
                r.write(arr[len(arr) - 1])
                arr[len(arr) -1] = line.strip('\n')
                flag = 0
    f.seek(0)
    f.truncate()

    leftstart = 0
    leftLast = 0
    rightstart = 0
    rightlast = 0

    f = open('file', 'w')
    for line in l:
        f.write(line)
        leftlast = leftLast + 1
    leftL = leftLast
    for line in arr:
        f.write(line)
        leftLast = leftLast + 1
    rightstart = leftLast
    for line in r:
        f.write(line)
    readFile(leftstart, leftLast)
    readFile(rightstart, rightstart)

print("enter the file name")
file = input()
count = 0
fp = open(file, 'r')
l = open('left.txt','w')
r = open('right.txt','w')
for line in fp:
    count = count + 1

readFeli(file, 0, count)