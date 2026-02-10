import sys

def main():
    if len(sys.argv) == 2:
        target_string = sys.argv[1]
        z_count = target_string.count('z')
        
        if z_count > 0:
            print('z' * z_count)
        else:
            print("none")
    else:
        print("none")

if __name__ == "__main__":
    main()