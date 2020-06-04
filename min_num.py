arrList = [11, 4, 5, 3, 10, 1, 140]

def commpare_num(arr):
    lowestNum = arr[0]
    for x in arr:
        if (lowestNum > x):
            lowestNum = x
    return lowestNum

print(commpare_num(arrList))