import os, sys, string, re
from collections import defaultdict
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *
sys.setrecursionlimit(9999999)

def main():
    return '\n'.join(map(lambda x:''.join(x),(lambda x,c,r,l:(r,[([(r[(c[0]-1)//40].__setitem__((c[0]-1)%40,'#'if (c[0]-1)%40 in range(x[0]-1,x[0]+2) else '.'),c.__setitem__(0,c[0]+1))for _ in range(1 if q[0]=='noop'else 2)], x.__setitem__(0,x[0]+q[1])if q[0]=='addx'else None) for q in l]))([1],[1],[['.']*40 for _ in range(6)],list(map(lambda x:tuple(map(lambda y:int(y) if y.lstrip('-').isdigit()else y,x)),map(lambda x:x.split(),getlines()))))[0]))

if __name__ == "__main__":
    p(main())

