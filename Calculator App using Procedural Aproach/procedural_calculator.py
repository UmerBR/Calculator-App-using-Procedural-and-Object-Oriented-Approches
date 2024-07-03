def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        raise ValueError("Cant divite by '0' add other value")
    else:
        return a/b

def cal():
    print('''
            Welcome to simple calculator, functions availabe are:
                Addition (+),           Subtraction (-),
                Multiplication (*),     Division (/)
    ''')

    op= int(input('''Enter operation to perform
                    For Addition (+) press 1,
                    For Subtraction (-) press 2,
                    For Multiplication (*) press 3,
                    For Division (/) press 4
                    '''))

    a= float(input('Please enter first value'))
    b= float(input('Please enter second value'))

    try:
        if op==1:
            result=add(a,b)
            print(f'Answer is:{result}')
            
        elif op==2:
            result=sub(a,b)
            print(f'Answer is:{result}')
            
        elif op==3:
            result=mul(a,b)
            print(f'Answer is:{result}')
            
        elif op==4:
            result=div(a,b)
            print(f'Answer is:{result}')
            
        else:
            print('Invalid operator input')

    except ValueError:
        print(f'{ValueError}')

cal()


