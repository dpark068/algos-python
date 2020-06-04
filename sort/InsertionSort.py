# Insertion Sort - Maintains sorted sublist in lower positions
# Each new item is inserted back into sublist
# O(n^2)

def InsertionSort(arr):
    size = len(arr)

    if len(arr) <= 1:
        return arr

    for i in range(size):
        
        # Loop through subarray to find position
        for j in range(i-1,-1,-1):
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
                
                #track the swap so it compares properly
                i = j
        print(arr)
    return arr

# Test
arr = [3,6,1,0,7,4]
print (InsertionSort(arr))