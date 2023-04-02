#Write a program to find binary search in a list.
def binarySearch(arr,n,x):
    low = 0
    high = n-1
    while low<high:
        mid = (low+high)//2
        if(arr[mid]==x):
            return mid
        elif(arr[mid]<x):
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [19,22,32,40,8,21,34,12,45]
arr.sort()
res = binarySearch(arr,9,34)
if(res==-1):
    print("The element in not in the list ")
else:
    print("The element is found at index ",res)