import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *

def main():
    return sum(map(lambda l: 1 + (ord(l[2]) - ord('X')) + ((1 + (((ord(l[2]) - ord('X')) - (ord(l[0]) - ord('A'))) % 3)) % 3) * 3, getlines()))

if __name__ == "__main__":
    p(main())

