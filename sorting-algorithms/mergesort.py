#mergesort.py
def mergeSort(a,beg,end):
    if beg<end:
        mid = (beg+end)//2 
        mergeSort(a,beg,mid)
        mergeSort(a,mid+1,end)
        merge(a,beg,mid,end)

def merge(a,beg,mid,end):
    i = beg
    j = mid+1
    index = beg
    temp = []
    while (i<=mid) & (j<=end):
        if a[i]<a[j]:
            temp[index] = a[i]
            i = i+1
        else:
            temp[index] = a[j]
            j = j+1
        index = index+1
    if i>mid:
        while j<=end:
            temp[index] = a[j]
            j+=1
            index+=1
    else:
        while i<=mid:
            temp[index] = a[i]
            i+=1
            index+=1
    for k in range(beg,index):
        a[k] = temp[k]

a = [32,45,2,54,1,25,45,1,15,6]
print(a)
n = len(a)
mergeSort(a,0,n-1)
print(a)


