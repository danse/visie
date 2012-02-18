import datetime

def history(ll):
    '''
    >>> history((1, 1, 1, 1, 1))
    [1.0, 1.0, 1.0, 1.0, 1.0]
    >>> history((1, 2, 3, 4, 5, 6, 7))
    [4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]
    '''
    s = 0
    r = []
    for l in reversed(ll):
        s+=float(l)
        r.append(s/(len(r)+1))
    r.reverse()
    return r
