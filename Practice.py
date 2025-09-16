#create empty list to store
names=[]

print("Enter 5 names: ")
for i in range(5):
    name=input(f"Name {i+1}: ")
    names.append(name)

search = (input("Enter a name to search: "))

if search in names:
    print("Meron")
else: 
    print("Wala")

#Divisible by 5/6
num = int(input("Enter a number"))

if num % 5 == 0 and num % 6 == 0:
    print("Divisible both")
elif num % 5 == 0:
    print("Divisible by 5")
elif num % 6 == 0:
    print("Divisible by 6")
else:
    print("not divisible both")

#Calculator SWITCH
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
operation = (input("Enter operation: "))

operations = {
    "+": num1 + num2,
    "-": num1 - num2,
    "*": num1 * num2,
    "/": num1 / num2 if num2 != 0 else "Cannot divide by zero"
}
result = operations.get(operation, "Wrong operator")

print(f"Result: {result}")

#Calculator MATCH CASE 
num1=int(input("num1: "))
num2=int(input("num2: "))
ope=(input("Operator:" ))

match ope:
    case "+":
        res = num1 + num2
    case "-":
        res = num1 - num2
    case "*":
        res = num1 * num2
    case "/":
        res = num1 / num2 if num2 != 0 else "not divided by zero"
    case _:
        print("Wrong Operator")

print(f"Total: {res}")

#Diamond
n = int(input("Enter size of diamond: "))

# Upper half
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

