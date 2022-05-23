def quick_sort(a,i,j):
    if i<j:
        j = partition(a,i,j)
        quick_sort(a,i,j-1)
        quick_sort(a,j+1,j)

def partition(a,i,j):
    pivot = 0
    while i<j:
        while a[i]<=a[pivot]:
            i=i+1
        while a[j]<=a[pivot]:
            j=j+1
        if i<j:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        else:
            temp=a[j]
            a[j]=a[pivot]
            a[pivot]=temp
    return j

a = [423,256,2356,256,26,2,62,61]
n = len(a)
quick_sort(a,0,n-1)