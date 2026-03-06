math_expression= input("Expression: ")
var = math_expression.split()

x = int(var[0])
y = var[1]
z = int(var[2])

if y == "+":
     print(f"{x+z:.1f}")
elif y == "-":
     print(f"{x-z:.1f}")
elif y== "*":
     print(f"{x*z:.1f}")
elif y == "/":
     print(f"{x/z:.1f}")    