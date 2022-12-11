import os, sys, string, re
from collections import defaultdict
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *
from operator import add, sub, le, ge, mul
sys.setrecursionlimit(9999999)

def main():
    return len((lambda f,*a:f(f,*a))(lambda f,l,s,m,i,c,j,d,h:None if i>=len(l) else f(f,l,s,m,i+1,0,0,d,h) if c>=l[i][1]else(s,s.add(m[-1]),f(f,l,s,m,i,c+1,0,d,h))if j>=10 else(s,m.__setitem__(0,tuple(map(add,m[0],d[l[i][0]]))),f(f,l,s,m,i,c,j+1,d,h))if j==0 else(s,h(m,j,tuple(map(sub,m[j-1],m[j]))),f(f,l,s,m,i,c,j+1,d,h)),list(map(lambda x:(x[0],int(x[1])),map(lambda x:x.split(),getlines()))),set(),[(0,0)]*10,0,0,0,{'L':(-1,0),'R':(1,0),'U':(0,-1),'D':(0,1)},lambda m,j,d:m.__setitem__(j,tuple(map(add,m[j],(0,0)if all(map(le,map(abs,d),(1,1)))else map(mul,map(lambda x:1 if x else-1,map(ge,d,(0,0))),map(min,map(abs,d),(1,1)))))))[0])

if __name__ == "__main__":
    p(main())

