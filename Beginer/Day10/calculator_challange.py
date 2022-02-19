def logo():
    return """
     _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculation():
    print(logo())
    number1 = float(input("Enter the 1st number: "))
    for key in operations:
        print(key)
    sig = input("Enter one of the operator above: ")
    number2 = float(input("Enter the 2nd number: "))

    oper = operations[sig]
    result = oper(number1, number2)
    print(f'{number1} {sig} {number2} = {result}')

    stop = False
    while not stop:
        cont_calc = input("Like to keep calculating [y/n] or 'r' to restart: ").lower()
        if cont_calc == 'y':
            sig = input("Enter the operator(+, -, *, /): ")
            oper = operations[sig]
            new_number = float(input("Enter a new number: "))
            new_result = oper(result, new_number)
            print(f'{result} {sig} {new_number} = {new_result}')
            result = new_result
        elif cont_calc == 'r':
            calculation()
        else:
            stop = True


calculation()
