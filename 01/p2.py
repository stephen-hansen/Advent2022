import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *

def main():
    p(sum(sorted(map(lambda x: sum(map(int, x)), getdbnldata()), reverse=True)[0:3]))

if __name__ == "__main__":
    main()

