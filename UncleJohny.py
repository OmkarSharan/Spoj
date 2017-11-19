TestCase = int(input())
while TestCase > 0:

    def binarysearch(Arr, Number, lo, high):
        mid = (lo + high) // 2
        if Arr[mid] == Number:
            return mid
        elif Number > Arr[mid]:
            return binarysearch(Arr, Number, mid + 1, high)
        else:
            return binarysearch(Arr, Number, lo, mid - 1)


    n = int(input())
    Arr = [int(i) for i in input().split()]
    k = int(input())
    temp = Arr[k - 1]
    Arr.sort(key=int)


    pos = binarysearch(Arr, temp, 0, len(Arr) - 1)
    print(pos + 1)
    TestCase -= 1
