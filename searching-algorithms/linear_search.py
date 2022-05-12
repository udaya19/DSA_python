a = [2,1,4,6,2]
n = len(a)
key = int(input("Enter value to be searched in the array:"))
for i in range(0,n):
    if(a[i] == key):
        print("Element found at index:",i)
        break
    else:
        print("Not found")
