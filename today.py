# this line prints "Hello world!"
print("Hello world!")

'''
long comment
few lines.....
'''

name = input("Please enter your name:") # read input
print(name)
print(name.split())
print(type(name))


# your name is : ___ last name: ____
fname = name.split()[0]
lname = name.split()[1]
# 1
print("your name is:",fname, "last name:",lname);
# 2
print("your name is: {} last name: {}".\
      format(fname, lname))
# 3
print(f'your name is: {fname} last name: {lname}')


xStr = input("Please enter a number:")
x = int(xStr)
x = x + 1
print(x)

x = int(input("Please enter a number:"))
y = float(input("Please enter a float number:"))

# input 2 float numbers
# print 4 math + calculation!
# 2.5
# 3.7
# 2.5 + 3.7 = 6.2

#print("{:.2f}".format(3.445556))
#print(f'{(3.444+0.589374):.2f}')

x = float(input("Please 1st number:"))
y = float(input("Please 2nd number:"))
print(f'{x} +  {y} = {(x + y):10.5f}')
print(f'{x} -  {y} = {(x - y):10.5f}')
print(f'{x} *  {y} = {(x * y):10.5f}')
print(f'{x} /  {y} = {(x / y):10.5f}')
print(f'{x} ** {y} = {(x ** y):10.5f}')
print(f'{x} \u221A  {y} = {(x ** 1/y):10.5f}')




