def calculator():
    while True:
        operation = input("Enter an operation (+, -, *, /, %, **): ")
        if operation in ('+', '-', '*', '/', '%', '**'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if operation == '+':
                print(num1 + num2)
            elif operation == '-':
                print(num1 - num2)
            elif operation == '*':
                print(num1 * num2)
            elif operation == '/':
                print(num1 / num2)
            elif operation == '%':
                print(num1 % num2)
            elif operation == '**':
                print(num1 ** num2)
            else:
                print("Invalid input")
        else:
            print("Invalid input")

calculator()
