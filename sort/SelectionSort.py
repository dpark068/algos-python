# Selection Sort - similar to bubble sort but only makes a single exchange per pass through
# O(n^2)

def SelectionSort(arr):
    size = len(arr)

    if size <= 1:
        return arr

    #Loop through arr from end to front
    for i in range(size-1,0,-1):
        
        # default high pos as 0
        high = 0
        for j in range(i+1):
            if arr[j] > arr[high]:
                high = j
            
        print(arr[high])
        
        #after each pass, must set it in proper place (always at end)
        arr[high],arr[i] = arr[i],arr[high]
        print(arr)
    return arr

# Test
arr = [3,6,1,0,7,4]
print (SelectionSort(arr))