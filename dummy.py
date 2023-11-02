from numpy import *
arr = array([1, 2, 3, 4, 5, 6])
arr2 = arr.view()

arr[1] = 8

print(arr)
print(arr2)

print("hello")
