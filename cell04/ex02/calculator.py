def main():
    try:
        num1_str = input("Give me the first number: ")
        num2_str = input("Give me the second number: ")
        
        num1 = int(num1_str)
        num2 = int(num2_str)
        
        print("Thank you!")
        
        print(f"{num1} + {num2} = {num1 + num2}")
        print(f"{num1} - {num2} = {num1 - num2}")
        print(f"{num1} / {num2} = {int(num1 / num2)}")
        print(f"{num1} * {num2} = {num1 * num2}")
        
    except ValueError:
        print("Error: Please enter valid numerical values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    main()