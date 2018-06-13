#Mutluhan Boz Merge Sort 12.06.2018
def mergeSort(list):

    if len(list)>1:
        mid = len(list) // 2
        leftArr = list[:mid]
        rightArr = list[mid:]
        print("left :" + str(leftArr))
        print("right :" + str(rightArr))
        print("Recursing through left side")
        mergeSort(leftArr)
        print("Recursing through right side")
        mergeSort(rightArr)
        i=0 #counters for left,right and output array
        j=0
        k=0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                list[k]=leftArr[i]
                i+=1
            else:
                list[k] = rightArr[j]
                j+=1
            k+=1
        while i < len(leftArr):
            list[k] = leftArr[i]
            i+=1
            k+=1
        while j < len(rightArr):
            list[k] = rightArr[j]
            j+=1
            k+=1
    print("Current state of the ordered sub-list : "+str(list))

alist = [5,1,9,4,6] #our unsorted array
print(alist)
mergeSort(alist)
print("--------")
print("Ordering Complete :")
print(alist)
input()
