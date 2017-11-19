class extrnalQuickSort:
    def __init__(self):
        self.arr = []

    def readfile(self,  file):
        fp = open(file, "r")
        fl = open('left.txt', "w")
        fr = open('right.txt', "w")
        fm = open('middle.txt', "w")
        i = 0
        for line in fp:
            self.arr.insert(0, line.strip('\n'))
            i = i + 1
            if i == 99:
                break
            i = 0
        for value in arr:
            fm.write(arr[i])
            i = i + 1
        i = 1
        leftStart = 0
        rightStart = 0
        flag = 0
        for line in fp:
            if i < 100:
                continue
            if self.arr[0] > line:
                fl.write(line.strip('\n'))
                leftStart = leftStart + 1
            elif self.arr[99] < line:
                fr.write(line.strip('\n'))
                rightStart = rightStart + 1
            elif line > self.arr[0] and line < self.arr[99]:
                if flag == 0:
                    fl.write(arr[0])
                    self.arr[0] = line.strip('\n')
                    flag = 1
                else:
                    fr.write(arr[99])
                    self.arr[99] = line.strip('\n')
                    flag = 0


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





s = extrnalQuickSort()
arr = [6,5,4,3,2]
s.quickSort(arr, 0, 4)
for i in arr:
    print(i,end=" ")
