print("Which operation(* or / or + or - or ** or root)")
operation = input()
print("a=")
a = float(input())
print("b=")
b = int(input())
if operation == "*":
    print("%f*%f=" %(a,b), a*b)
elif operation == "/":
    print("%f/%f=" %(a,b), a/b)
elif operation =="+":
    print("%f+%f=" %(a,b), a+b)
elif operation == "-":
    print("%f-%f=" %(a,b), a-b)
elif operation == "**":
    print("%f**%f=" %(a,b), a**b)
elif operation == "root":
    print("%a**0.5=" %(a), a**0.5)
else:
    print("Point the operation")
