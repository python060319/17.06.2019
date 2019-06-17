
x = int(input("Please enter a number:"))
if x > 0:
    # do this if x is bigger than 0
    print(f'{x} is bigger than zero')
    print('this is all i want to do if > 0');
elif x == 0:
    print (f'{x} is zero')
else:
    print(f'{x} is smaller than zero')

print('back to normal........')

# read string from user
# check if the letter 'a' appears
# if so, print how many times 'a' appears
# elif check if letter 'b' appears
# if so, print how many times 'b' appears
# else print 'no!'
name = input("Enter you name:")
if name.upper().count('A') > 0:
    print(f"'a' appears {name.upper().count('A')} times")
elif name.upper().count('B') > 0:
    print(f"'b' appears {name.upper().count('B')} times")
else:
    print('no')


# read age (int) from the user
# 0-3 print 'baby'
# 4-12 print 'child'
# 13-18 print 'teenager'
# 18+ print grownup
age = int(input("Please enter your age: "))
if age >= 0 and age <= 3:
    print('you are a baby')
elif age <= 12:
    print('you are a child')
elif age <= 18:
    print('you are a teenager')
else:
    print('you are a grown-up')

#if a <= >=  == != 0 and or
#if age >= 0 and age <= 3


#x = 1
#e1 = input("Enter command:")
#eval(e1)

#33.92 * 8.5
#+ - * / **
formula = input("Enter calculation , format: X + Y:")
lst = formula.split()
oper = lst[1];
x = float(lst[0])
y = float(lst[2])

if oper in ["+", "-", "/", "*"]:
    print("{} is legal operator".format(oper))
    if oper == "+":
        print(f"{x} + {y} = {x + y}")
    elif oper == "-":
        print(f"{x} - {y} = {x - y}")
    elif oper == "*":
        print(f"{x} * {y} = {x * y}")
    elif oper == "/":
        print(f"{x} / {y} = {x / y}")
else:
    print(f"{lst[1]} is an illegal operator")
