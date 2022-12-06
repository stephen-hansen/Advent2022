import os, sys, string, re
from collections import defaultdict
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *

def main():
    return ''.join((lambda l, s, r: (list(map(lambda x: [s[x[2]].insert(0, s[x[1]].pop(0)) for _ in range(x[0])], l)), [r.append(s[k][0]) for k in range(1,10)], r))(*(lambda l, s, _: ([list(map(int, filter(lambda t: len(t) > 0, re.split('[' + string.ascii_letters + '\s]', x)))) for x in l[10:]], s))(*(lambda l, s: (l, s, [s[1+((i-1)//4)].append(x[i]) if x[i] != ' ' else None for x in l[0:8] for i in range(1,len(x),4)]))(getlines(), defaultdict(list))), [])[2])

if __name__ == "__main__":
    p(main())

