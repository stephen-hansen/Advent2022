import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *

def main():
    return sum(map(lambda z: int(not (z[0][0] > z[1][1] or z[1][0] > z[0][1])), map(lambda x: list(map(lambda y: list(map(int, y.split('-'))), x.split(','))), getlines())))

if __name__ == "__main__":
    p(main())

