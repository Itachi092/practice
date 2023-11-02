from array import *

arr1=array('i',[])
arr2=array('i',[])

le = int(input("enter the length of array"))

for i in range(le):
    x=int(input('enter the arr1 values'))
    arr1.append(x)

for e in range(le):
    y=int(input("enter the arr2 values"))
    arr2.append(y)

print(arr1)
print(arr2)


arr_result=array('i',[])

for i in range(len(arr1)):

    result= arr1[i]+arr2[i]
    arr_result.append(result)

print(arr_result)
