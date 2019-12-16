##normal
def squares(N):
    res=[]
    for i in range(N):
        res.append(i*i)
    return res

for item in squares(9):
    print(item)
##generator
def gensquares(N):
    for i in range(N):
        yield i**2

for item in gensquares(9):
    print(item)
##generator has less code than normal way. Lazy evaluation makes computer run better.