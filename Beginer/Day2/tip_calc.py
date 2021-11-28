print("Welcome to the tip calculator.")
bill = float(input("What's the total bill? "))
percent = int(input("What's the percentage tip would you like to give? [10, 12, or 15] "))
people = int(input("How many people to split the bill? "))

pay_per_person = (bill * (percent / 100) + bill) / people

print(f"Each person should pay: ${pay_per_person:.2f}")

