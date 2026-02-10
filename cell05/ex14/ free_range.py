import sys

def main():
    if len(sys.argv) == 3:
        try:
            start = int(sys.argv[1])
            end = int(sys.argv[2])
 
            if start <= end:
                result = list(range(start, end + 1))
            else:
                result = list(range(start, end - 1, -1))
            
            print(result)
        except ValueError:
            print("none")
    else:
        print("none")

if __name__ == "__main__":
    main()