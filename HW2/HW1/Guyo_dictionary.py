list = []

size = int(input("Matrix size: "))
for x in range (size):
    item_input = input(f"Shopping items {x+1}: ") 
    list.append(item_input)

print(f"\nYou have {len(list)} items in the cart\n")

while True:
    option = input("What would you like to do [C]hange [R]emove [D]isplay S[earch] ? ").lower()

    #CHANGE
    if option == 'c':
        try: 
            keys = int(input("\nEnter key to search: "))
            if 0 <= keys < len(list):
                print(f"Found {list[keys]} item")
                list[keys] = input("Enter value: ")
                print()
            else:
                print("Im sorry, not in the cart\n")
        except:
            print("Invalid key\n")

    #REMOVE
    elif option == 'r':
        try:
            keys = int(input("\nEnter key to search: "))
            if 0 <= keys < len(list):
                print (f"The key {keys} with value {list[keys]} has been deleted\n")
                del list[keys]
            else:
                print("Im sorry, not in the cart\n")
        except:
            print("Key not found\n")

    #DISPLAY
    elif option == 'd':
        print("\nDisplaying Values")
        print("Key      Value")
        for key, value in enumerate(list):
            print(f"{key:<9}{value}")
        print()

    #SEARCH
    elif option == 's':
        search = input("\nEnter item to search: ").strip().lower()
        found = False

        for item in list:
            if item.lower() == search:
                print(f"Found {search} item\n")
                found = True
                break
        if not found: 
            print("I'm sorry, not in the cart\n")

    elif option == '*':
        print("Bye")
        break

    else:
        print("Invalid option\n")
    





        
