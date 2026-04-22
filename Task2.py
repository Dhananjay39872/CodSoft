# Simple python calculator task2
# take user input
a = float(input("enter first number:"))
operator = input("enter operator(+ , - , * , /):")
b = float(input("enter second number:"))
# calculation
if operator == "+":
    print("result =", a+b)
elif operator == "-":
    print("result =", a-b)
elif operator == "*":
    print("result =", a*b)
elif operator == "/":
    if b != 0:
        print("result=", a/b)
    else:
        print("error: Division by zero!")
else:
    print("invalid operator")
