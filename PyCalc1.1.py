import time
print("Initializing")
time.sleep(1)
print("Welcome to PyCalc 1.1!")
print("Created by Coke Unity")
def maincalc():
    inpute = input("Commands: Update Log, Calculate, Exit; ")
    if inpute == "Update Log":
        print("1.0: You can do Addition, Subtraction, Multiplication and Division with two numbers.")
        print("1.1: Minor update, Now it loops with Functions!")
        print("Planed:")
        print("    Operations: Modulus, Exponentiation and Floor division.")
        print("    Extras: Support for more than two number, GUI (If possible.)")
        maincalc()
    elif inpute == "Exit":
        print("Shutting down...")
        time.sleep(1)
    else:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        print("Operations: Addition, Subtraction, Multiplication, Division.")
        ##  Yes, I know I can put operations but I prefere Inpute because it's fancy
        inpute = input("What operation: ")
        time.sleep(1)
        ##  Calculations
        if inpute == "Addition" and num1 != 0 and num2 != 0:
            print(num1 + num2)
            maincalc()
        elif inpute == "Subtraction" and num1 != 0 and num2 != 0:
            print(num1 - num2)
            maincalc()
        elif inpute == "Multiplication" and num1 != 0 and num2 != 0:
            print(num1 * num2)
            maincalc()
        elif inpute == "Division" and num1 != 0 and num2 != 0:
            print(num1 / num2)
            maincalc()
        ##  Error Catcher
        elif inpute != "Multiplication" and num1 == 0 or inpute != "Multiplication" and num2 == 0:
            print("Cannot operate calculation with 0")
            maincalc()
        elif inpute == "Multiplication" and num1 == 0 or inpute == "Multiplication" and num2 == 0:
            print("Anything times 0 is 0")
            maincalc()
        else:
            print("Unknown Operation", inpute)
            maincalc()
maincalc()
