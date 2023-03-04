import numpy


n, m, p = map(int, input().split())

ncolumn = []
mcolumn = []




for i in range(n):
    ncolumn = input().split()
    if len(ncolumn) == p:
        ncolumn = list(map(int, ncolumn))
        print(ncolumn)
        #nlist.append(ncolumn)
        #print(nlist)
    #if len(ncolumn) == p:


for i in range(m):
    mcolumn = input().split()
    if len(mcolumn) == p:
        mcolumn = list(map(int, mcolumn))
        print(mcolumn)
        #print(mlist)

#print(map(int,ncol))
#print(mcol)
#print(numpy.concatenate((ncol, mcol), axis = 0))