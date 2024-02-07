First = input("Enter the first number : ")
operator = input("Enter operator (+,-,*,/,%)")
Second = input("Enter the second number : ")
First = int(First)
Second = int(Second)

if operator == "+":
    print(First + Second)
elif operator == "-":
    print(First - Second)
elif operator == "*":
    print(First * Second)
elif operator == "/":
    print(First / Second)
elif operator == "%":
    print(First % Second)
else:
	print("INVALID OPERATION")
