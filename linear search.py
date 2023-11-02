
a = 0
def search(list):
    global a
    for i in list:

        if i == n:
            return True
        a= a+1

list = [5,6,7,8,9,2,3]
n = 2
if search(list):
    print("found",a)

else:
    print("not found")