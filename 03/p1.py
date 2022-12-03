import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *

def main():
    return sum(map(lambda y: ord(y.lower()) - ord('a') + 1 + 26 * y.isupper(), map(lambda x: ''.join(set(x[:int(len(x)/2)]).intersection(x[int(len(x)/2):])), getlines())))

if __name__ == "__main__":
    p(main())

