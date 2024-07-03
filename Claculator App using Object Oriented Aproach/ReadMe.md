# Simple Calculator (Using Object Oriented Approach)
This repository contains a simple calculator program implemented in Python using an object-oriented approach. The calculator supports basic arithmetic operations: addition, subtraction, multiplication, and division.


## Overview
This is a basic command-line calculator that allows users to perform simple arithmetic operations. The user is prompted to choose an operation and provide two numbers, and the program will display the result of the operation.

## Features
+ Addition
+ Subtraction
+ Multiplication
+ Division (with error handling for division by zero)

## Usage
To use the calculator, run the script in a Python environment. The script will prompt you to choose an operation and enter two numbers, then it will display the result of the operation.


Follow the on-screen prompts to perform calculations.

## Code Explanation

### Class Definition
My_Calculator: This class contains methods to perform the basic arithmetic operations and a method to handle user input and interaction.

### Methods
init(self): Initializes the result attribute to None.
add(self, a, b): Updates self.result with the sum of a and b.
sub(self, a, b): Updates self.result with the difference of a and b.
mul(self, a, b): Updates self.result with the product of a and b.
div(self, a, b): Updates self.result with the quotient of a and b. Raises a ValueError if b is zero.
cal(self): Displays a welcome message, prompts the user to select an operation and input two numbers, and then calls the appropriate method to perform the calculation. It handles invalid operator input and exceptions for division by zero.

### Example
```
class My_Calculator:
    def __init__(self):
        self.result = None
    
    def add(self, a, b):
        self.result = a + b
    
    def sub(self, a, b):
        self.result = a - b
    
    def mul(self, a, b):
        self.result = a * b
    
    def div(self, a, b):
        if b == 0:
            raise ValueError("Can't divide by '0'. Please enter another value.")
        else:
            self.result = a / b
        
    def cal(self):
        print('''
            Welcome to the simple calculator. Functions available are:
                Addition (+),           Subtraction (-),
                Multiplication (*),     Division (/)
        ''')

        op = int(input('''Enter operation to perform
                    For Addition (+) press 1,
                    For Subtraction (-) press 2,
                    For Multiplication (*) press 3,
                    For Division (/) press 4:
                    '''))
        
        a = float(input('Please enter the first value: '))
        b = float(input('Please enter the second value: '))

        try:
            if op == 1:
                self.add(a, b)
                print(f'Answer is: {self.result}')
            elif op == 2:
                self.sub(a, b)
                print(f'Answer is: {self.result}')
            elif op == 3:
                self.mul(a, b)
                print(f'Answer is: {self.result}')
            elif op == 4:
                self.div(a, b)
                print(f'Answer is: {self.result}')
            else:
                print('Invalid operator input')
        except ValueError as ve:
            print(ve)

if __name__ == "__main__":
    calculator = My_Calculator()
    calculator.cal()
```

## Exception Handling
The script includes basic error handling for division by zero. If the user attempts to divide by zero, a ValueError is raised, and an appropriate error message is displayed.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request.

## License
This project is licensed under the MIT License.

