import sys

def main():
    params = sys.argv[1:]
    
    if not params:
        print("none")
    else:
        for p in params:
            if not p.endswith("ism"):
                print(f"{p}ism")

if __name__ == "__main__":
    main()