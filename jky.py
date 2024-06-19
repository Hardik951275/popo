def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def perform_operations(a, b, *operations):
    results = []
    for operation in operations:
        if operation == 'add':
            results.append(add(a, b))
        elif operation == 'subtract':
            results.append(subtract(a, b))
        elif operation == 'multiply':
            results.append(multiply(a, b))
        elif operation == 'divide':
            results.append(divide(a, b))
        else:
            results.append(f"Invalid operation: {operation}")
    return results

def main():
    try:
        a = float(input("Enter the first value: "))
        b = float(input("Enter the second value: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print("Choose operations to perform (comma-separated): add, subtract, multiply, divide")
    operations = input("Enter your choices: ").split(',')

    operations = [op.strip() for op in operations]  # Remove any leading/trailing spaces

    results = perform_operations(a, b, *operations)
    
    for op, result in zip(operations, results):
        print(f"The result of {op} is: {result}")

if __name__ == "__main__":
    main()
