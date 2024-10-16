def sum(num1, num2):
    s = str(num1 + num2).removesuffix(".0")
    return s


def subtract(num1, num2):
    su = str(num1 - num2).removesuffix(".0")
    return su


def multiple(num1, num2):
    m = str(num1 * num2).removesuffix(".0")
    return m


def divide(num1, num2):
    d = str(num1 / num2).removesuffix(".0")
    return d


while True:
    print('---Mini Calculator---')
    print('Enter your expression:')

    try:
        num1 = float(input('the first number: '))
        num2 = float(input('the sencond number: '))
        operators = input('sign(+, -, *, /): ')

        n1 = str(num1).removesuffix(".0")
        n2 = str(num2).removesuffix(".0")

        if operators == '+':
            print(f'result: {n1} {operators} {n2} =', sum(num1, num2))
        elif operators == '-':
            print(f'result: {n1} {operators} {n2} =', subtract(num1, num2))
        elif operators == '*':
            print(f'result: {n1} {operators} {n2} =', multiple(num1, num2))
        elif operators == '/':
            print(f'result: {n1} {operators} {n2} =', divide(num1, num2))
    except:
        print('Invalid values')
