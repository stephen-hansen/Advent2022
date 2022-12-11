import os, sys, string, re
from collections import defaultdict
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *
sys.setrecursionlimit(9999999)

def main():
    return len((lambda f,*a:f(f,*a))(lambda f,l,s,p,u,x,y,i,c,d: None if i>=len(l) else (f(f,l,s,p,u,x,y,i+1,0,d) if c>=l[i][1] else (s,(s.add((x,y)),f(f,l,s,x,y,x+d[l[i][0]][0],y+d[l[i][0]][1],i,c+1,d))if(i==0 and c==0)or(abs(x+d[l[i][0]][0]-p)>1)or(abs(y+d[l[i][0]][1]-u)>1)else f(f,l,s,p,u,x+d[l[i][0]][0],y+d[l[i][0]][1],i,c+1,d))),list(map(lambda x:(x[0],int(x[1])),map(lambda x:x.split(),getlines()))),set(),0,0,0,0,0,0,{'L':(-1,0),'R':(1,0),'U':(0,-1),'D':(0,1)})[0])

if __name__ == "__main__":
    p(main())

