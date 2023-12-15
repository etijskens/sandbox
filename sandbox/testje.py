import re
import sys

def testje(n,mn):
    ncores_list = [n]
    while ncores_list[0] != 1:
        ncores_list.insert(0, ncores_list[0] // 2)
    nnodes_list = [1] * len(ncores_list)
    while nnodes_list[-1] < mn:
        nnodes_list.append(nnodes_list[-1] * 2)
        ncores_list .append(ncores_list [-1] * 2)
    print(ncores_list)
    print(nnodes_list)
    for nc,nn in zip(ncores_list, nnodes_list):
        print('   ', nc, nn)


if __name__=="__main__":
    for n in range(64):
        testje(n+1,3)
    print("-*# ok #*-")