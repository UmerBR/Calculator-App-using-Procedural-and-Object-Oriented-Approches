class My_Calculator:
    def __init__(self):
        self.result=None
    def add(self, a, b):
        self.result=a+b
    def sub(self, a, b):
        self.result=a-b
    def mul(self, a, b):
        self.result=a*b
    def div(self,a ,b):
        if b==0:
            raise ValueError("Can't divide by '0'. Please enter another value.")        
        else:
            self.result=a/b
        
    def cal(self):
        print('''
            Welcome to the simple calculator. Functions available are:
                Addition (+),           Subtraction (-),
                Multiplication (*),     Division (/)
        ''')

        op =int(input('''Enter operation to perform
                    For Addition (+) press 1,
                    For Subtraction (-) press 2,
                    For Multiplication (*) press 3,
                    For Division (/) press 4 :
                    '''))
        
        a=float(input('please enter first value :'))
        b=float(input('please enter second value :'))


        try:
            if op==1:
                self.add(a,b)
                print(f'Answer is :{self.result}')
            elif op==2:
                self.sub(a,b)
                print(f'Answer is :{self.result}')
            elif op==3:
                self.mul(a,b)
                print(f'Answer is :{self.result}')
            elif op==4:
                self.div(a,b)
                print(f'Answer is :{self.result}')
            else:
                print('Invalid Operator Input')
        except ValueError:
            print(f'{ValueError}')

if __name__ == "__main__":
    calculator=My_Calculator()
    calculator.cal()
    