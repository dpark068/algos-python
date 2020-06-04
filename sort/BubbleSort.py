# Bubble Sort makes multiple passes to sort items in proper position
# O(n^2)

def BubbleSort(arr):
    if len(arr) <= 1:
        return arr
    
    size = len(arr)
    for i in range(size):
        for j in range(size):

            #swaps if num in position i is less than pos j
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j],arr[i]

    return arr

# Test

arr = [3,6,1,9,6,6,8,7,0]
print (BubbleSort(arr))