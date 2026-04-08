def myfunction():
    print('This is my function')

print(myfunction, type(myfunction), id(myfunction))
a = myfunction
print(a, type(a), id(a))

myfunction()
a()

def funpar(a, b):
    print(f'a: {a} b: {b}')
    print(f'ref in func a: {id(fa)} sa: {id(sa)}')
    funpar(fa, sa)

def tripar(a, b, c):
    print(f'tripar: a: {a} b: {b} b: {c}')

tripar(3, 7, 2)
tripar(1, 2, 4)

def getsth(a, b)
    c = a + b
    return c

res = getsth(5, 2)
print(res)

v = 10
print(f'ref v before call: {id(v)}')

def incv(v):
    print(f'ref v before call: {id(v)}')
    v = v + 1
    print(f'ref v inside after add: {id(v)}')
    
incv(v)
print(f'ref after call: {id(v)}')
print(v)

def chgli(ourlist):
    ourlist[1] = 7

li1 = [3, 6, 8]
print(li1)
chgli(li1)
print(li1)

v = 10
def incv2(v):
    v = v + 1
    return v

v = incv2(v)
print(v)

def multi(a, b, c, d=1, e=4):
    print(f'multi: {a} {b} {c} {d} {e}')

multi(5, 2, 6)
multi(5, 2, 6, 7, 4)
multi(5, 2, 6, 7)

def many(a, b, c=0, d=0, e=0, f=0, g=0):
    print(f'many: {a} {b} {c} {d} {e} {f} {g}')

many(3, 8)
many(3, 8, 4, 6)
many(5, 3, 0, 0, 0, 0, 8)
many(5, 3, e=6, g=8)

def evenmore(a, *b):
    print('evenmore')
    print(a)
    print(b)

evenmore(3,8)
evenmore(3, 8, 4, 7)
evenmore(3, 8, 4, 7, 8, 3, 4, 6, 8)

def moredef(a, b, **d):
    print('moredef')
    print(a)
    print(b)
    print(d)

moredef(1, b=6, d=7)
moredef(3, b=2, d=8, e=9, w=1)

def anynumtype(*a, **b,):
    print(a)
    print(b)
anynumtype(3, b=2, d=8, e=9, w=1)
anynumtype(3, 5, 7, e=9, w=1)
anynumtype()
anynumtype(7, 2)

def unifun(*args, **kwargs):
    pass
