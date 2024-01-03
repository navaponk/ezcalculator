#navapon kraitat coursework reuploaded
while True:
    print("Type 'cal' to perform a calculation or 'exit' to quit:")
    user_input = input()

    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "cal":
        print("Select an operation you want to perform:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input()

        if operation in ("1", "2", "3", "4"):
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")

            if operation == "1":
                result = int(num1) + int(num2)
                print("Addition: {} + {} = {}".format(num1, num2, result))
            elif operation == "2":
                result = int(num1) - int(num2)
                print("Subtraction: {} - {} = {}".format(num1, num2, result))
            elif operation == "3":
                result = int(num1) * int(num2)
                print("Multiplication: {} * {} = {}".format(num1, num2, result))
            elif operation == "4":
                if int(num2) != 0:
                    result = int(num1) / int(num2)
                    print("Division: {} / {} = {}".format(num1, num2, result))
                else:
                    print("Error: Division by zero.")
        else:
            print("Invalid operation. Please enter a valid operation (1, 2, 3, or 4).")

    else:
        print("Invalid input. Please type 'cal' to perform a calculation or 'exit' to quit.")
