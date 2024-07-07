print("Welcome to the tip calculator!")

while True:
    try:
        bill = float(input("What was the total bill? $"))
        tip = float(input("How much tip would you like to give? 10, 12, or 15? %"))
        people = int(input("How many people to split the bill? "))
    except ValueError:
        print("Only numeric values allowed.")
    else:
        if bill and tip and people:
            print(f"Each person should pay: ${(bill + (tip * bill / 100)) / people:.2f}")
            break
        else:
            print("Messing Values! Try Again.")
