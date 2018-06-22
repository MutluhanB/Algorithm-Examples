#Mutluhan Boz Merge Sort 12.06.2018
"""
with open("C:\\Users\Mutluhan\Desktop/IntegerArray.txt") as array:
    myList = array.read().splitlines()
!!You must adjust the path
""""
def mergeSort(list):
    
    mid = len(list) // 2
    leftside = list[:mid]
    rightside = list[mid:]

    if len(list) > 1:

        mergeSort(leftside)
        mergeSort(rightside)

        i=0
        j=0
        k=0
        while i < len(leftside) and j < len(rightside):
            if leftside[i] < rightside [j]:
                list[k]=leftside[i]
                i+=1
                k+=1
            else:
                list[k] = rightside[j]
                j+=1
                k+=1
        while i < len(leftside):
            list[k] = leftside[i]
            i += 1
            k += 1
        while j < len(rightside):
            list[k] = rightside[j]
            j+=1
            k+=1
print(myList)           
mergeSort(myList)
print(myList)
input()
