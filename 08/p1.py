import os, sys, string, re
from collections import defaultdict
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *

def main():
    return sum((lambda l: [(x==0 or x==len(l[0])-1 or y==0 or y==len(l)-1 or all([l[z][y] < l[x][y] for z in range(0,x)]) or all([l[z][y] < l[x][y] for z in range(x+1,len(l[0]))]) or all([l[x][z] < l[x][y] for z in range(0,y)]) or all([l[x][z] < l[x][y] for z in range(y+1,len(l))])) for x in range(len(l[0])) for y in range(len(l))])(list(map(lambda x:list(map(int,x)),map(list,getlines())))))

if __name__ == "__main__":
    p(main())

