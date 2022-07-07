import array

def returnIndex(arr, key):
    n = len(arr)
    midpt = n/2
    if key == arr[midpt]:
        return midpt
    
