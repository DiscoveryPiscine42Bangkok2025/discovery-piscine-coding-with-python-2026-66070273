#!/usr/bin/env python3
import sys

def upcase_it(s):
    return s.upper()

def main():
    if len(sys.argv) == 2:
        result = upcase_it(sys.argv[1])
        print(result)
    else:
        print("none")

if __name__ == "__main__":
    main()