a = float(input("Enter value: "))  # Convert input to float

while True:
    b = input("Enter the next value (or '=' to stop): ")
    
    if b == "=":
        print("Final result:", a)
        break  # Exit the loop

    try:
        b = float(b)  # Convert b to float
    except ValueError:
        print("Invalid number. Please enter a numeric value.")
        continue  # Skip to next iteration

    operator = input("Enter operation (+, -, *, /, %): ")
    operator_list = ['-', '+', '/', '%', '*']

    if operator in operator_list:
        if operator == "-":
            a -= b
        elif operator == "+":
            a += b
        elif operator == "*":
            a *= b
        elif operator == "/":
            if b == 0:
                print("Error: Division by zero is not allowed.")
                continue
            a /= b
        elif operator == "%":
            if b == 0:
                print("Error: Modulo by zero is not allowed.")
                continue
            a %= b
    else:
        print("Invalid operator. Please enter a valid operation.")

