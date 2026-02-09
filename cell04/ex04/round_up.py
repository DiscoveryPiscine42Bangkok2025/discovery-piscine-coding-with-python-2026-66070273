import math

def main():
    try:
        user_input = input("Give me a number: ")
        number = float(user_input)
        
        result = math.ceil(number)
        print(result)
        
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()