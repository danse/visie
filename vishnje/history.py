
def cumulate(aa):
    '''
    >>> [c for c in cumulate((1, 1, 1, 1, 1))]
    [1.0, 1.0, 1.0, 1.0, 1.0]
    >>> [c for c in cumulate((1, 2, 3, 4, 5, 6, 7))]
    [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    '''
    s = 0
    l = 0
    for a in aa:
        s += float(a)
        l += 1
        yield(s/l)

def history(l):
    '''
    >>> history((1, 1, 1, 1, 1))
    [1.0, 1.0, 1.0, 1.0, 1.0]
    >>> history((1, 2, 3, 4, 5, 6, 7))
    [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    '''
    return [c for c in cumulate(l)]

