print("Enter number1: ")
num1=int(input())

cpn=int(input("Enter phone number: "))

print("Entre your name: ")
name=input()

last=(input("Enter Lastname: "))

print(f"Your number is {num1}")
print(f"Your name is {name}")

print(f"Your phone number: {cpn}")
print(f"Your lastname is: {last}")

num2=int(input("Enter num1: "))
num3=int(input("Enter num2: "))
operation=(input("Enter Operation: "))

if operation == "+":
    result = num2 + num3
elif operation == "*":
    result = num2 * num3
elif operation == "-":
    result = num2 - num3
elif operation == "/":
    result = num2 / num3 
else:
    print("Wrong operator") 

print(f"Total is: {result}")

for x in range(1,11):
    print(f"{x}", end=" ")
    if x%5==0:
        print()

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()





