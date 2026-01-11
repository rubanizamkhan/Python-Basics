# Write a python program to read two numbers and display their sum, difference, product and quotient

a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

sum=a+b
diff=a-b
pro=a*b

print("Sum is:", sum)
print("Diff is:", diff)
print("Pro is:", pro)

if b!=0:
    quo=a/b
    print("Quotient is:", quo)
else:
    print("Divison is not possible")
