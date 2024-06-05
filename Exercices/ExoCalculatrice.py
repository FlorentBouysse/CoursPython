# EXO calculatrice

number_one = input("Enter a number: ");
number_two = input("Enter a number: ");

if number_one.isdigit() and number_two.isdigit():
    print(f"Addition: {int(number_one) + int(number_two)}");
else:
    print("Error: Please enter a number");