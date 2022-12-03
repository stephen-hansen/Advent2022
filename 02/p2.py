import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *

def main():
    return sum(map(lambda l: 1 + ((ord(l[0]) - ord('A')) + ((ord(l[2]) - ord('Y')) % 3)) % 3 + (ord(l[2]) - ord('X')) * 3, getlines()))

if __name__ == "__main__":
    p(main())

