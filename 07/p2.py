import os, sys, string, re
from collections import defaultdict
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *

def main():
    return min((lambda c,t: filter(lambda k:k[1]>=t,c.items()))(*(lambda c: (c,30000000-(70000000-c['/'])))((lambda c,d,_: (c,(lambda f,*a: f(f,*a))(lambda r,s: ([r(r,y) for y in d[s]],c.update({s:c[s]+sum([c[y] for y in d[s]])})),'/')))(*(lambda s,c,d:(c,d,list(map(lambda a:(s.append(a[2]) if len(a) == 3 and a[2] != '..' else (s.pop() if a[1] == 'cd' else None)) if a[0] == '$' else (c.update({'/'.join(s):c['/'.join(s)]+int(a[0])}) if a[0].isdigit() else d['/'.join(s)].append('/'.join(s)+'/'+a[1])),map(lambda l: l.split(' '),getlines())))))([],defaultdict(int),defaultdict(list)))[0])),key=lambda k:k[1])[1]

if __name__ == "__main__":
    p(main())

