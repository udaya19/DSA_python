#binary_search.py

array = [1,2,3,4,5,6]
key = int(input("Enter value to be searched:"))
n = len(array)
low = 0
high = n-1
while low<=high:
    mid = (low+high)//2
    if array[mid] == key:
        flag = 1
        break
    elif array[mid]<key:
        low = mid+1
    else:
        high = mid-1

if flag:
    print("Element found at index ",mid)
else:
    print("Element not found!!!")