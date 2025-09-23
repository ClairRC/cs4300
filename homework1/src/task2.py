def main():
    choice = input(
        "1: Integer Multiplication\n" +
        "2: Float addition\n" +
        "3: Print \"Hello\"\n" +
        "4: Negate a Boolean\n")

    if choice == '1':
        var1 = input("Enter first integer: ")
        var2 = input("Enter second integer: ")
        print(int_multiplication(int(var1), int(var2)))

    elif choice == '2':
        var1 = input("Enter first float: ")
        var2 = input("Enter second float: ")
        print(float_addition(float(var1), float(var2)))
    
    elif choice == '3':
        print_hello()

    elif choice == '4':
        var1 = input("Enter \"True\" or \"False\" ")
        actual_var1 = False if var1 == "false" or var1 == "False" else True
        print(not_gate(actual_var1))

    else:
        print("Invalid choice womp womp too bad")

def int_multiplication(a, b):
    return a * b

def float_addition(a, b):
    return a + b

def print_hello():
    print("Hello")

def not_gate(a):
    return not a

if __name__ == "__main__":
    main()