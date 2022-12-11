import os, sys, string, re
from collections import defaultdict
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *
sys.setrecursionlimit(9999999)

def main():
    return sum((lambda x,c,r,l:(r,[([(r.append(c[0]*x[0])if(c[0]-20)%40==0 else None,c.__setitem__(0,c[0]+1))for _ in range(1 if q[0]=='noop'else 2)],x.__setitem__(0,x[0]+q[1])if q[0]=='addx'else None)for q in l]))([1],[1],[],list(map(lambda x:tuple(map(lambda y:int(y) if y.lstrip('-').isdigit() else y,x)),map(lambda x:x.split(),getlines()))))[0])

if __name__ == "__main__":
    p(main())

