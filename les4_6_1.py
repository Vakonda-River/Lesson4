from itertools import  cycle

def c_le(a):
    n = 0
    for el in cycle(a):
        if n > 10:
            break
        print(el)
        n += 1
