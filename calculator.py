from add import add
from mod import mod
from power import power
from subtract import subtract
from mult import mult
from div import div

if __name__ == "__main__":
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Mod")

    choice = input("Enter choice(1/2/3/4): ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == "1":
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == "2":
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == "3":
        print(num1, "*", num2, "=", mult(num1, num2))
    elif choice == "4":
        print(num1, "/", num2, "=", div(num1, num2))
    elif choice == "5":
        print(num1, "**", num2, "=", power(num1, num2))
    elif choice == "6":
        print(num1, "%", num2, "=", mod(num1, num2))
    else:
        print("Invalid input")
