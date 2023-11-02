from functools import *

nums=[2,3,4,5,6,7,8,9]


even = list(filter(lambda a : a%2==0, nums))

double = list(map(lambda a : a*2, even))

sum = reduce(lambda a,b : a+b, double)

print(even)
print(double)
print(sum)


