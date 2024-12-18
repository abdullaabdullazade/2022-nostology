def min(list__):
    a = list__[0]
    for j in list__:
        if j < a:
            a = j

    return a


def max(list__):
    a = list__[0]
    for j in list__:
        if j > a:
            a = j

    return a


def sort_(list_, reverse=False):
    b = []
    list_ = list(list_)
    q = len(list_)
    for d in range(q):
        if reverse == False:
            v = min(list_)
        else:
            v = max(list_)
        b.append(v)
        list_.remove(v)

    return b


print(sort_([45,45,12,35,15,48,3,1,3,15,3,13,5,13,31,3,15,131,5,13,16,51,1,6,51,321,6,51,31,56,1,1,65,13,65,1,365]))
print(sorted([45,45,12,35,15,48,3,1,3,15,3,13,5,13,31,3,15,131,5,13,16,51,1,6,51,321,6,51,31,56,1,1,65,13,65,1,365],reverse=False))
