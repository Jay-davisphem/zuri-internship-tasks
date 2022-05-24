"""A cli Calculator app"""


def add(first_num: float, second_num: float) -> float:
    """Add"""
    return first_num + second_num


def subtract(first_num: float, second_num: float) -> float:
    """subtract"""
    return first_num - second_num


def multiply(first_num: float, second_num: float) -> float:
    """Multiply"""
    return first_num * second_num


def divide(first_num: float, second_num: float) -> float:
    """Divide"""
    return first_num / second_num


def modulus(first_num: float, second_num: float) -> float:
    """Modulus"""
    return first_num % second_num


def none_zero_number() -> float:
    """Returns when num is not zero"""
    num = float(input("Enter second number: "))
    while num == 0:
        print("\nDenominator cannot be zero!")
        num = float(input("Please reenter the second number: "))
    return num


def compute_answer(entry: str, num1: float, num2: float) -> float or None:
    """Compute answer"""
    if entry == "+":
        answer = num1 + num2
    elif entry == "-":
        answer = num1 - num2
    elif entry == "*":
        answer = num1 * num2
    elif entry == "/":
        answer = num1 / num2
    else:
        answer = num1 % num2
    return answer


def calculator() -> None:
    """Converge all functions to implement the calculator"""
    message = """
    Enter:
    + to do addition
    - to do subtraction
    * to do multiplication
    / to do division
    mod to do modulus operation.
    """

    operations = ("+", "-", "*", "/", "mod")
    error_on_zero = ("/", "mod")

    print(message)
    entry = input("Enter an operation + or - or * or / or mod: ")

    if entry in operations:
        try:
            num1 = float(input("\nEnter first number: "))
            if entry in error_on_zero:
                num2 = none_zero_number()
            else:
                num2 = float(input("Enter second number: "))
            answer = compute_answer(entry, num1, num2)
            print(f"\n{num1} {entry} {num2} = {answer}\n")
        except ValueError:
            print("Input not a number type!\n")
    else:
        print("Sorry, operation not not available\n")


def retry() -> None:
    """Retry calculator"""
    y_or_n = "y"
    while y_or_n == "y":
        calculator()
        y_or_n = input("Do you want to continue(y/n): ")
        while not(y_or_n in ('n', 'y')):
            print("Invalid response!\n")
            y_or_n = input("Do you want to continue(y/n): ")
            if y_or_n in ('y', 'n'):
                break
    print('\nGoodbye techie! ')
if __name__ == '__main__':
    retry()
