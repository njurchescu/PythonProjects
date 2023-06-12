def add(n1, n2):
    return float(n1 + n2)

def substract(n1, n2):
    return float(n1 - n2)

def multiply(n1, n2):
    return float(n1 * n2)

def divide(n1, n2):
    return float(n1 / n2)

operations = {
 "+" : add,
 "-" : substract,
 "*" : multiply,
 "/" : divide,
}

# function = operations["*"]
# print(function(2, 3))

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    continue_operation = True
    while continue_operation:
        operation_symbol = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        function = operations[operation_symbol]
        answer = function(num1, next_number)
        print(f"{num1} {operation_symbol} {next_number} = {answer}")
        continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or 'n' to exit: ").lower()
        if continue_calculating == 'y':
            num1 = answer
        else:
            continue_operation = False
            calculator()



calculator()