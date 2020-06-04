# MergeSort divide and conquer 
#O(n log n)

def MergeSort(arr):

    # Base case if arr size == 1
    if len(arr) == 1:
        return arr
    
    # divide the arr
    midPoint = len(arr) // 2
    rightArr = arr[ :midPoint]
    leftArr = arr[midPoint: ]
    
    # Recursive left and right array
    leftSortedArr = MergeSort(rightArr)
    rightSortedArr = MergeSort(leftArr)

    # Left and right pointers
    i = 0
    j = 0

    sortedArr = []

    # Sort left and right Sorted Arr
    while i < len(leftSortedArr) and j < len(rightSortedArr):
        if leftSortedArr[i] <= rightSortedArr[j]:
            sortedArr.append(leftSortedArr[i])
            i += 1

        else:
            sortedArr.append(rightSortedArr[j])
            j += 1
    
    # Add in remaining array values
    while i < len(leftSortedArr):
        sortedArr.append(leftSortedArr[i])
        i += 1
    
    while j < len(rightSortedArr):
        sortedArr.append(rightSortedArr[j])
        j += 1
    
    return sortedArr


# Test the MergeSort
arr = [6,5,4,8,9,10,0,100]
print(MergeSort(arr))




