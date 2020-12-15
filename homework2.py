from functools import reduce
def prod(a):
    def m(x,y):
        return x*y
    return reduce(m,a)
print(prod([1,4,7,10,13]))
