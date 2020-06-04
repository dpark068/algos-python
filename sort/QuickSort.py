""" 
Quicksort uses divide and conquer but without extra space
Time Complexity: O(n log n)
Space Complexity: O(1) - in place sorting
Algorithm:
    1) Choose a pivot point in array
    2) Two pointers - swap (Left side > pivot) with (Right Side < Pivot)
    3) Once right pointer < left pointer, swap value at right pointer with pivot pos value
    4) repeat for subarray left and right of pivot (we know pivot is in right location)
"""
def QuickSort(arr):

    if len(arr) <= 1:
        return arr

    def sort(arr, left, right):
        if right < left:
            return
        if (right-left)<= 1:
            return       

        pivotPos = left
        pivot = arr[left]
        left += 1
        print("pivot: " + str(pivot))
        print("left original: " + str(left))
        print(arr[left])
        print("right original: " + str(right))
        print(arr[right])
        done = False
        while not done:

            # Iterate left pointer until it finds value greater than pivot point
            while left <= right and arr[left] <= pivot:
                left += 1
            
            # Same for right pointer find value less than pivot
            while left <= right and arr[right] >= pivot:
                right -= 1

            if right < left:
                done = True
            else:
                
                arr[left], arr[right] = arr[right], arr[left]
        
        # When right > left, swap pivot and right
        arr[pivotPos], arr[right] = arr[right], arr[pivotPos]

        # recurse into left and right
        sort(arr, 0, right-1)
        sort(arr, right+1, len(arr)-1)
    
    sort(arr,0, len(arr)-1)
    return arr

# Test the quick Sort
#arr = [1,4,3,2]
arr = [6,5,4,8]
#arr = [6,5,4,8,9,10,0,100]
print(QuickSort(arr))