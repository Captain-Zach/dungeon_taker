arr = [1,2,3,5,6,8,13,15,16,19,22]

def binSearchRec(arr, target, index = None):
    index = int(len(arr)/2)
    print(index)
    if arr[index] == target:
        return index

    if arr[index] > target:
        index = binSearchRec(arr[0:index],target, index = int(index/2),)
    elif arr[index] < target:
        index = binSearchRec(arr[index:len(arr)],target, index = int(index + ((len(arr)-index)* 0.5)), )
    return index
    

index = binSearchRec(arr, index = None, target = 3)
print(index)
index = binSearchRec(arr, 6)