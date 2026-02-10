#!/usr/bin/env python3
import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    needed = 8 - len(s)
    print(s + ('Z' * needed))

def main():
    params = sys.argv[1:]
    if not params:
        print("none")
    else:
        for p in params:
            if len(p) > 8:
                shrink(p)
            elif len(p) < 8:
                enlarge(p)
            else:
                print(p)

if __name__ == "__main__":
    main()