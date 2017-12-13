x = int(input('x = '))
op = input('operation(+,-,*,/): ')
y = int(input('y = '))

if op == '+':
    print(x, '+', y, '=', x + y)
elif op == "-":
    print(x, '-', y, '=', x - y)
elif op == '*':
    print(x, '*', y, '=', x * y)
else:
    print(x, '/', y, '=', x / y)
