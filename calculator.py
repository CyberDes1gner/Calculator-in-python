print('please pick an operation')
print('1. Addition 2.Subtraction 3.Multiplication 4.Division')
operation = input('input here: ')
if operation == '1':
    firstnumber1 = input('input your first number: ')
    secondnumber1 = input('input your second number: ')
    print(int(firstnumber1) +int(secondnumber1))
elif operation == '2':
    firstnumber2 = input('input your first number: ')
    secondnumber2 = input('input your second number: ')
    print(int(firstnumber2) - int(secondnumber2))
elif operation == '3':
    firstnumber3 = input('input your first number: ')
    secondnumber3 = input('input your second number: ')
    print(int(firstnumber3) * int(secondnumber3))
elif operation == '4':
    firstnumber4 = input('input your first number: ')
    secondnumber4 = input('input your second number: ')
    print(int(firstnumber4) / int(secondnumber4))
else:
    print('Invalid Syntax')
    
