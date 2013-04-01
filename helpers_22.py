#!/usr/bin/python
# free software

def sorted(l):
    # compatibility with python2.2 (for pys60)
    l2 = l[:]
    l2.sort()
    return l2

def sum(l):
    # compatibility with python2.2 (for pys60)
    if len(l) > 0:
        return l[0] + sum(l[1:])
    return 0
