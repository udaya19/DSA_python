#insertionsort.py

a = [2,5,3,24,768,64,76,54]
n = len(a)
for i in range(0,n):
    print(a[i])
for i in range(1,n):
    temp = a[i]
    j = i
    while j>0 and temp<a[j-1]:
        a[j] = a[j-1]
        j = j-1
    a[j] = temp
print("Elements of array after sorting")
for i in range(0,n):
    print(a[i])