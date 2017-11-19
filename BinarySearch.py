t = int(input())
while t:
    def BinarySearch(arr, number, left, right):
        if left > right:
            return False
        mid = int((left + right) // 2)
        if arr[mid] == number:
            return mid
        elif number > arr[mid]:
            return BinarySearch(arr, number, mid + 1, right)
        elif number < arr[mid]:
            return BinarySearch(arr, number, left, mid - 1)


    print("enter the array elements !")
    a = [int(i) for i in input().split()]
    index = BinarySearch(a, 3, 0, 4)
    print(index)
    t -= 1

