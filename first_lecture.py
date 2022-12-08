2.1 Fill in the blanks in each of the following:
a) print 
b) string
c) reference variable
d) % (percentage)
e) comments
f) if , condition, 
g) int()
h) \n
i) parenthesis ()
j) variable or instances
2.2 State whether each of the following is true or false. If false, explain why
a) The Python function get_input requests input from the user
Ans)false, in python to get input from user input() function is used.
b) A valid Python arithmetic expression with no parentheses is evaluated left to right.
Ans) False, if there is no prentheses, then next precendece is for exponent.
c) The following are invalid variable names: 3g, 87 and 2h.
Ans) True: A variable name cannot start with a number
d) The operator != is an example of a relational operator.
Ans) True: not equal to is a relational operaor in python. it is used to compare values
e) A variable name identifies the kind of information stored in the object
Ans) False: it is a type () function which tells the user the data type stored
f) In Python, the programmer must declare the object type before using the object in
the program
Ans) False: Object type is never defined in python
g) If parentheses are nested, the expression in the innermost pair is evaluated first.
Ans) True
h) Python treats the variable names, a1 and A1, as the same variable
Ans) False: variable names a1 and A1 are not same , because one is lower case and other one is upper case character
i) The backslash character is called an escape sequence.
Ans) True
j) The relational operators all have the same level of precedence and evaluate left to
right
Ans) False: First, less than ( < ), less than or equal to ( <= ), greater than ( > ), and greater than or equal to ( >= ). Then, equal to ( = ) and not equal to ( != ).
2.3 State the order of evaluation of the operators in each of the following Python
statements and show the value of x after each statement is performed.
a) x = 7 + 3 * 6 / 2 - 1 
x = 7 + 18/2 -1
x = 7 + 9 -1
x = 16 - 1
x = 15

b) x = 2 % 2 + 2 * 2 - 2 / 2
b = 2 % 2 + 4- 2 / 2
b = 0 + 4 - 1
b =  4 -1
b = 3

c) x = ( 3 * 9 * ( 3 + ( 9 * 3 / ( 3 ) ) ) )
x = ( 3 * 9 * ( 3 + ( 9 * 3 /  3  ) ) )
x = ( 3 * 9 * ( 3 + ( 27 /  3  ) ) )
x = ( 3 * 9 * ( 3 + ( 27 /  3  ) ) )
x = ( 3 * 9 * ( 3 +  9 ) )
x  = ( 3 * 9 * 12 )
x = 27 * 12
x = 324

2.4 Write a program that requests the user to enter two numbers and prints the sum,
product, difference and quotient of the two numbers.
x = int(input("enter first number : "))
y = int(input("enter first number : "))
sum = x + y
product = x*y
difference = x - y
quotient = x/y
print(f"(sum = {sum} , product = {product}, difference = {difference}, quotient = {quotient:.2f})")
2.5 Write a program that reads in the radius of a circle and prints the circle’s diameter,
circum-ference and area. Use the constant value 3.14159 for π. Do these calculations in
output statements
pi = 3.14159
r = int(input("enter any value for radius of a circle = "))
d = 2 * r
c = 2*pi*r
a = pi*r**2
print(f"Diameter of circle : {d},  Circumferece of circle : {c:.2f}, area of circle : {a:.2f}")
2.7 Write a program that reads in two integers and determines and prints whether the first is a multiple of the second. (Hint: Use the modulus operator.)

a = int(input("Enter first number a: "))
b = int(input("Enter 2nd number b: "))
print(f"a = {a},b = {b}")

if a % b == 0:
    print(f"a = {a} is multiple of b = {b}")
else:
    print(f"a = {a} is not multiple of b = {b}")
2.8 Write a python program to check if the user input number is even or odd using if
else

a = int(input("Enter any integer number :"))
if a % 2 == 0:
    print(f"a = {a} is an even Number")
else:
    print(f"a = {a} is an odd Number")

2.9 Write a temperature-conversion program that gives the user the option of
converting Fahrenheit to Celsius or Celsius to Fahrenheit. Then carry out the
conversion,Using if else



a = int(input("Enter Fahrenheit temperature value : "))
print(f"a = {a}°F ")
b = (a - 32) * 5/9
print(f"Fahrenheit a = {a}°F equal to Centigrade b = {b:.2f}°C")

print("----------------------------------------------------------------------------------------------")

c = int(input("Enter Centigrade temperature value : "))
print(f"a = {c}°C ")
d = (a * 9/5) + 32
print(f"Centigrade c = {c}°C equal to Fahrenheit d = {d:.2f}°F")

2.10 Give a brief answer to each of the following “object think” questions:
a) Why does this text choose to discuss structured programming in detail before
proceeding with an in-depth treatment of object-oriented programming?
in my understanding when we get the functional programming concept then we will better understand the OOP concept

b) What aspects of an object need to be determined before an object-oriented program
can be built?
every object has a properties and some behaviours

2.11 Write a Python program to calculate the factorial of a number (a non-negative
integer) using the if else statement.

2.12 Take two inputs from user base and exponent and then print the power of base
using if else statement.

a = int(input("Enter base number = "))
b = int(input("Enter exponent number = "))

c = a ** b
print(f"power of base {a} using exponent {b} = {c}")

2.13 Take values of length and breadth of a rectangle from the user and check if it is
square or not.


l = int(input("Enter the value of length = "))
B = int(input("Enter the value of Breadth = "))
print(f"length = {l} , Breadth = {B}" )
if l == B:
    print("It is a square")
else:
    print("It is not a square")
2.14 A school has following rules for grading system:
1. Below 30 - F
2. 30 to 40 - E
3. 40 to 50 - D
4. 50 to 60 - C
5. 60 to 80 - B
6. Above 80 - A
Ask users to enter marks and print the corresponding grade.
marks = int(input("Enter Marks = "))
if marks < 30:
    print(f"Below 30 - F" )
elif    30 <= marks <= 40:
    print("30 to 40 - E")
elif    40 <= marks <= 50:
    print("40 to 50 - D")
elif    50 <= marks <= 60:
    print("50 to 60-C")
elif    60 <= marks <= 80:
    print("60 to 80 - B")
elif    marks >= 80:
    print("Above 80 - A")
else:
    print("FAIL")
2.15 Write a program to check if a year is a leap year or not.
If a year is divisible by 4 then it is a leap year but if the year is a century year like
2000, 1900, 2100 then it must be divisible by 400.
2.16 Write a program to accept two numbers and a mathematical operators and
then perform operation accordingly :
Example :
Enter first number : 8
Enter the operator : /
Enter second number : 2
Your answer is : 4
a = int(input("Enter first number : "))
operator = print("Enter the operatir : /")
b = int(input("Enter 2nd number = "))
formula = (a/b)
print(f"your answer is : {formula:.2f}")






