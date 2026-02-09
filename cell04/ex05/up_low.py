def main():
    try:
        user_input = input()
        print(user_input.swapcase())
    except EOFError:
        pass

if __name__ == "__main__":
    main()