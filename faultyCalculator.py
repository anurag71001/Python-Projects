# Faulty Calculator is designed for the purpose to stop students from cheating
# in their examinations in some different way.
a= int(input("Enter the first number: "))
operator=  str(input("Enter the operator(+, -, /, *, %): "))
b= int(input("Enter the second number: "))

if operator == '+':
    print(a*b)
elif operator == '-':
    print(a/b)
elif operator == '*':
    print(a+b)
elif operator == '/':
    print(a%b)
else:
    print(a-b)
