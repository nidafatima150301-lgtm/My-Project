a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

op = input("Enter Operator (+, -, *, /): ")

if op == "+":
    print("Result =", a + b)

elif op == "-":
    print("Result =", a - b)

elif op == "*":
    print("Result =", a * b)

elif op == "/":
    print("Result = ",a/b)
else:
    print("Invalid Operator")