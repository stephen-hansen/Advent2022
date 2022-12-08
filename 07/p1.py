import os, sys, string, re
from collections import defaultdict
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *

def main():
    return sum(map(lambda v:v[1],filter(lambda v:v[1]<=100000,(lambda c,d,_: (c,(lambda f,*a: f(f,*a))(lambda r,s: ([r(r,y) for y in d[s]],c.update({s:c[s]+sum([c[y] for y in d[s]])})),'/')))(*(lambda s,c,d:(c,d,list(map(lambda a:(s.append(a[2]) if len(a) == 3 and a[2] != '..' else (s.pop() if a[1] == 'cd' else None)) if a[0] == '$' else (c.update({'/'.join(s):c['/'.join(s)]+int(a[0])}) if a[0].isdigit() else d['/'.join(s)].append('/'.join(s)+'/'+a[1])),map(lambda l: l.split(' '),getlines())))))([],defaultdict(int),defaultdict(list)))[0].items())))

if __name__ == "__main__":
    p(main())

