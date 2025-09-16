def converter(dollars):
    inr = dollars * 88.12
    gbp = dollars * 0.74
    cny = dollars * 7.12

    return inr, gbp, cny

print("Enter dollar ($) (* to exit): ", end="")
user_input = input()

while user_input != "*":
    list = user_input.split("@")
    
    print("\nDollar ($)\tIndian Rupee (R)\tBritish Pound (P)\tChina (Y)")
    
    for d_str in list:
        dollar = float(d_str.strip())
        # Call the function and unpack the returned tuple
        inr, gbp, cny = converter(dollar)
        print(f"{dollar}\t\t {inr:.2f}\t\t{gbp:.2f}\t\t\t{cny:.2f}")
 
    print("\nEnter dollar ($) (* to exit): ", end="")
    user_input = input()

print("Bye")