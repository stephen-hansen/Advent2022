import os, sys, string, re
from collections import defaultdict
from functools import reduce
from operator import mul
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *

def main():
    return max((lambda l,f:[reduce(mul, (f(f,l,x,y,x-1,y,-1,0,False),f(f,l,x,y,x+1,y,1,0,False),f(f,l,x,y,x,y-1,0,-1,False),f(f,l,x,y,x,y+1,0,1,False)),1) for x in range(len(l[0])) for y in range(len(l))])(list(map(lambda x:list(map(int,x)),map(list,getlines()))),lambda f,l,q,w,x,y,a,b,s:0 if (s or x<0 or x>=len(l[0]) or y<0 or y>=len(l)) else 1+f(f,l,q,w,x+a,y+b,a,b,l[q][w]<=l[x][y])))

if __name__ == "__main__":
    p(main())

