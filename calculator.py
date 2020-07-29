#In the file we are creating a calculator with simple math operations like additton,multiplication etc.
print("Simple Calculator App")

#Below here we are defining some functions to do some specific operations.
#num_add() function performs addition of two numbers and like others performs their operations
def num_add():
    c=a+b
    return c
def num_sub():
    c=a-b
    return c
def num_mul():
    c=a*b
    return c
def num_div():
    c=a/b
    return c 
def num_sqr():
    c=a*a
    return c
#Here we are asking the user for waht operation to be performed and waht are the numbers    
x=input("what operation do you want to perform? ")
a=int(input("enter 1st value:"))
b=int(input("enter 2nd value:"))

#The user given input is compared with the below conditinal statements.And prints the favourable Output.
if x == 'add':
    print("The answer is:",num_add())
elif x == 'sub':
    print("The answer is:",num_sub())
elif x == 'mul':
    print("The answer is:",num_mul())
elif x == 'div':
    print("The answer is:",num_div())
elif x == 'sqr':
    print("The answer is:",num_sqr())
else:
    print("invalid operation")
    
