try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Select operation:")
    print("press + for Addition")
    print("press - for Subtract")
    print("press * for Multiply")
    print("press / for Divide")
    o = input("Enter operation: ")
    match o:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "*":
            print(f"The result is: {a * b}")
        case "/":
            if b != 0:
                print(f"The result is: {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation selected.")
except Exception as e:
    print(f"An error occurred: {e}")