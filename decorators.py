def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):

        if a<d:
            a,b = b,a

        return func(a,d)

    return inner

div = smart_div(func)

div(2,4)
