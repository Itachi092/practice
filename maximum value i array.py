from array import *

arr=array('i',[2,3,4,5,6,7])

max= arr[0]

for i in arr:
    if i>max:
        max=i



print(max)