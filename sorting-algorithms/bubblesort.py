#bubblesort.py

array = [24,5,134,635,12,689]
n = len(array)
for i in range(1,n):
    for j in range(0,n-i):
        if array[j]>array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp

for i in range(0,n):
    print(array[i])