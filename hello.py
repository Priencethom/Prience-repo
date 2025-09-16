#1Enter number and determine if divisible by 5/6
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 6 == 0:
    print("Dividible both.")
elif num % 5 == 0:
    print("Divisible by 5.")
elif num % 6 == 0:
    print("Divisible by 6.")
else:
    print("Not divisible both.")

#2Display 200 and error
for i in range (1, 1001):
    if i == 200:
        print("Error: Reached 200")
        break
    print(i)

#3Display 1-100 and Error to 200 and continue
for num in range(1, 1001):
    if num == 200:
        print("Error: Reached 200!")
    else:
        print(num)














