import numpy as np

def task(a, l):
    result = np.array([], dtype=object)
    for i in a:
        b = np.array(i)
        if len(b) == l:
            result = np.append(result,b)
    return np.array(result)

arr = [[1, 2, 3, 4, 5],[10, 20, 30],[100, 200, 300, 400]]
length = 5
print(task(arr, length))
