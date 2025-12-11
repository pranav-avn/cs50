expression = input("Expression: ")
op1, sym, op2 = expression.split(" ")
op1, op2 = float(op1), float(op2)
if sym == "+":
    print(op1 + op2)
elif sym == "-":
    print(op1 - op2)
elif sym == "*":
    print(op1 * op2)
elif sym == "/":
    print(op1 / op2)
else:
    print("Unknown operator")
