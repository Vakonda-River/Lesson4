from itertools import count

def ci_le(a):
    for el in count(a):
        if el > 10:
            break
        else:
            print(el)