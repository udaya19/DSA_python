#selectionsort.py

a = [245,5,2,15,6,53,634,64,63]
n = len(a)
for i in range(0,n):
    min = i
    for j in range(i+1,n):
        if a[j]<a[min]:
            min = j
    temp = a[i]
    a[i] = a[min]
    a[min] = temp

print(a)