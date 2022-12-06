import os, sys, string, re
from collections import defaultdict
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *

def main():
    return (lambda s: [i+14 for i in range(len(s)-14) if len(set(s[i:i+14])) == 14])(getlines()[0])[0]

if __name__ == "__main__":
    p(main())

