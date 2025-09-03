print("\nMultiplication Table\n")

while True:
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    search = int(input("Search: "))

    if row == 0 or col == 0 or search == 0:
        print("\nLoop Stopped...")
        break

    print()
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            result = i * j
            if result == search:
                print(f"[{result}]", end="\t")
            else:
                print(result, end="\t")
        print()
    print()

