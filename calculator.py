def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    while True:
        print("\nSimple Calculator")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        try:
            choice = int(input("Enter choice (1/2/3/4/5): "))
            if choice == 5:
                print("The program is terminated.Thank You!")
                break
            elif choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please select a valid operation.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == 2:
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == 3:
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == 4:
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()