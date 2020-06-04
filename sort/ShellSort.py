# Shell sort is like insertion sort by with gap, i
# will sort one by one after

def ShellSort(arr):
    
    def gapInsertSort(arr, startPosition, gap):

        for i in range(startPosition + gap, len(arr), gap):
            
            currentValue = arr[i]
            pos = i

            while pos >= gap and arr[pos-gap] > currentValue:
                arr[pos] = arr[pos-gap]
                pos = pos-gap
            
            arr[pos] = currentValue

    gap = len(arr) // 2

    while gap > 0:

        for i in range(gap):
            gapInsertSort(arr,i,gap)
        
        gap = gap // 2
    
    return arr
    
    

print(ShellSort([3,5,1]))