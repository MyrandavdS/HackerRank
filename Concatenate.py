import numpy


n, m, p = map(int, input().split())

nlist = []
mlist = []




for i in range(n):
    ncolumn = input().split()
    if len(ncolumn) == p:
        ncolumn = list(map(int, ncolumn))
        nlist.append(ncolumn)



for i in range(m):
    mcolumn = input().split()
    if len(mcolumn) == p:
        mcolumn = list(map(int, mcolumn))
        mlist.append(mcolumn)


array_n = numpy.array(nlist)
array_m = numpy.array(mlist)
#print(array_n)
#print(array_m)
print(numpy.concatenate((array_n, array_m), axis = 0))