import array

def returnIndex(arr, key):
    n = len(arr)
    for i in range(0, n):
        if arr[i] == key:
            return i
    return -1

def insertElement(arr, key):
    arr.append(key)

def removeElement(arr, key):
    arr.remove(key)

if __name__ == "__main__":
    arr = array.array('i', [2, 4, 6, 8, 3])
    key = 8
    result = returnIndex(arr, key)
    print("result: ", result)

    insertElement(arr, key)
    print("On insertion:", arr)

    removeElement(arr, key)
    print("On removal: ", arr)