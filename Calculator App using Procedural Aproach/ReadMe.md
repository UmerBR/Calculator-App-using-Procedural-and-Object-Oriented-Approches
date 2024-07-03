
# Simple Calculator
This repository contains a simple calculator program implemented in Python. The calculator supports basic arithmetic operations: addition, subtraction, multiplication, and division.

Table of Contents
Overview
Features
Usage
Code Explanation
Exception Handling
Contributing
License
### Overview
This is a basic command-line calculator that allows users to perform simple arithmetic operations. The user is prompted to choose an operation and provide two numbers, and the program will display the result of the operation.

### Features
Addition
Subtraction
Multiplication
Division (with error handling for division by zero)

### Usage
To use the calculator, run the script in a Python environment. The script will prompt you to choose an operation and enter two numbers, then it will display the result of the operation.


##Code Explanation
### Functions

+ add(a, b): Returns the sum of a and b.
+ sub(a, b): Returns the difference of a and b.
+ mul(a, b): Returns the product of a and b.
+ div(a, b): Returns the quotient of a and b. Raises a ValueError if b is zero.

### Main Function
The cal() function is the main entry point of the script. It prints a welcome message, prompts the user to select an operation and input two numbers, and then calls the appropriate function to perform the calculation.

### Example
```
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Can't divide by '0'. Please enter another value.")
    else:
        return a / b

def cal():
    print('''
            Welcome to the simple calculator. Functions available are:
                Addition (+),           Subtraction (-),
                Multiplication (*),     Division (/)
    ''')

    op = int(input('''Enter operation to perform
                    For Addition (+) press 1,
                    For Subtraction (-) press 2,
                    For Multiplication (*) press 3,
                    For Division (/) press 4
                    '''))

    a = float(input('Please enter the first value: '))
    b = float(input('Please enter the second value: '))

    try:
        if op == 1:
            result = add(a, b)
            print(f'Answer is: {result}')
            
        elif op == 2:
            result = sub(a, b)
            print(f'Answer is: {result}')
            
        elif op == 3:
            result = mul(a, b)
            print(f'Answer is: {result}')
            
        elif op == 4:
            result = div(a, b)
            print(f'Answer is: {result}')
            
        else:
            print('Invalid operator input')

    except ValueError as e:
        print(e)

cal()
```

## Exception Handling
The script includes basic error handling for division by zero. If the user attempts to divide by zero, a ValueError is raised, and an appropriate error message is displayed.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request.

## License
This project is licensed under the MIT License.

