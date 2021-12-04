a_l = []
def mylist(a0, a1):  # function for create list of nums with Ar.Progress.
    c = a1 - a0
    d = 99 * (a1 - a0) + 2
    for i in range(a0, d, c):
        a_l.append(i)


